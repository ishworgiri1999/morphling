# -*- coding: utf-8 -*-

import sys
import gevent
import json
import signal
import logging
import time
import os
from locust import events
from locust.env import Environment
from locust.log import setup_logging
from locust.stats import stats_printer
from locust.util.timespan import parse_timespan
from .prometheus_exporter import metrics_export # import the event hook

setup_logging("INFO", None)
logger = logging.getLogger(__name__)


def sig_term_handler():
    logger.info("Got SIGTERM signal")
    sys.exit(0)


class LocustLoadTest(object):
    """
    Runs a Locust load test and returns statistics
    """

    def __init__(self, settings):
        self.settings = settings
        self.start_time = None
        self.end_time = None
        self.web_ui = None
        self.collects = {}
        gevent.signal_handler(signal.SIGTERM, sig_term_handler)

    def stats(self):
        """
        Returns the statistics from the load test in JSON
        """
        statistics = {
            "requests": {},
            "failures": {},
            "num_requests": self.env.runner.stats.num_requests,
            "num_requests_fail": self.env.runner.stats.num_failures,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "fail_ratio": self.env.runner.stats.total.fail_ratio,
            "gpu_statics": self.collects
        }

        for name, value in self.env.runner.stats.entries.items():
            locust_task_name = "{0}_{1}".format(name[1], name[0])
            statistics["requests"][locust_task_name] = {
                "request_type": name[1],
                "num_requests": value.num_requests,
                "min_response_time": value.min_response_time,
                "median_response_time": value.median_response_time,
                "avg_response_time": value.avg_response_time,
                "max_response_time": value.max_response_time,
                "response_times": value.response_times,
                "response_time_percentiles": {
                    55: value.get_response_time_percentile(0.55),
                    65: value.get_response_time_percentile(0.65),
                    75: value.get_response_time_percentile(0.75),
                    85: value.get_response_time_percentile(0.85),
                    95: value.get_response_time_percentile(0.95),
                },
                "total_rps": value.total_rps,
                "total_rpm": value.total_rps * 60,
            }

        for id, error in self.env.runner.errors.items():
            error_dict = error.to_dict()
            locust_task_name = "{0}_{1}".format(
                error_dict["method"], error_dict["name"]
            )
            statistics["failures"][locust_task_name] = error_dict

        return statistics

    def set_run_time_in_sec(self, run_time_str):
        try:
            self.run_time_in_sec = parse_timespan(run_time_str)
        except ValueError:
            logger.error(
                "Invalid format for `run_time` parameter: '%s', "
                "Valid formats are: 20s, 3m, 2h, 1h20m, 3h30m10s, etc." % run_time_str
            )
            sys.exit(1)
        except TypeError:
            logger.error(
                "`run_time` must be a string, not %s. Received value: % "
                % (type(run_time_str), run_time_str)
            )
            sys.exit(1)

    def run(self):
        """
        Run the load test.
        """

        if self.settings.run_time:
            self.set_run_time_in_sec(run_time_str=self.settings.run_time)

            logger.info("Run time limit set to %s seconds" % self.run_time_in_sec)

            def timelimit_stop():
                logger.info(
                    "Run time limit reached: %s seconds. Stopping Locust Runner."
                    % self.run_time_in_sec
                )
                self.env.runner.quit()
                self.end_time = time.time()
                logger.info(
                    "Locust completed %s requests with %s errors"
                    % (self.env.runner.stats.num_requests, len(self.env.runner.errors))
                )
                logger.info(json.dumps(self.stats()))

            gevent.spawn_later(self.run_time_in_sec, timelimit_stop)

        try:
            logger.info("Starting Locust with settings %s " % vars(self.settings))

            self.env = Environment(
                user_classes=self.settings.classes,
                reset_stats=self.settings.reset_stats,
                tags=self.settings.tags,
                events=events,
                exclude_tags=self.settings.exclude_tags,
                stop_timeout=self.settings.stop_timeout,
            )

            self.env.create_local_runner()
            # gevent.spawn(stats_printer(self.env.stats)) # need to be stopped properly

            if self.web_ui == None and self.settings.metrics_export: # reuse the exist web_ui
                self.web_ui = self.env.create_web_ui()

            self.env.events.init.fire(environment=self.env, runner=self.env.runner, web_ui=self.web_ui) # fire event hooks

            def collectGPUMetrics():
                from prometheus_client.parser import text_string_to_metric_families
                import requests
                target_metrics = ["DCGM_FI_DEV_GPU_UTIL", "DCGM_FI_DEV_MEM_COPY_UTIL", "DCGM_FI_PROF_SM_ACTIVE", "DCGM_FI_PROF_SM_OCCUPANCY", "DCGM_FI_PROF_DRAM_ACTIVE"]
                dcgm_endpoint = os.getenv("DCGM_ENDPOINT", "")
                if dcgm_endpoint == "":
                    return
                import time
                end_time = time.time() + self.run_time_in_sec
                for item in target_metrics:
                    self.collects[item] = 0.0

                while time.time() < end_time: 
                    metrics = requests.get(dcgm_endpoint).content.decode('ascii')

                    for family in text_string_to_metric_families(metrics):
                      for sample in family.samples:
                        if sample[0] in target_metrics:
                          self.collects[sample[0]] = max(float(sample[2]), self.collects[sample[0]])
                    time.sleep(0.1)

            gevent.spawn(collectGPUMetrics)

            self.env.runner.start(
                user_count=self.settings.num_users, spawn_rate=self.settings.spawn_rate
            )

            self.start_time = time.time()
            self.env.runner.greenlet.join()

        except Exception as e:
            logger.error("Locust exception {0}".format(repr(e)))

        finally:
            self.env.events.quitting.fire()
