from __future__ import print_function

import math
import os
import threading
import time
import numpy as np

import grpc
import api_pb2
import api_pb2_grpc


# ResultDB Settings
db_name = "morphling-db-manager"
db_namespace = "morphling-system"
db_port = 6799 
#manager_server = "%s.%s:%s" % (
#    db_name,
#    db_namespace,
manager_server = "%s:%s" % (
    "10.110.124.79",
    db_port,
)  # "morphling-db-manager.morphling-system:6799"
channel_manager = grpc.insecure_channel(manager_server)

def main():
    mls = []
    
    gpu_stats = {"bbq":54.5,"zzz":234}
    import json
    gpu_stats = json.dumps(gpu_stats)
    ml = api_pb2.KeyValue(key="qps", value=str(113))
    mls.append(ml)

    stub_ = api_pb2_grpc.DBStub(channel_manager)
    result = stub_.SaveResult(
        api_pb2.SaveResultRequest(
            trial_name="mysql_test_py",
            namespace="default",
            results=mls,
            other_metrics=gpu_stats,
        ),
        timeout=5,
    )
    print(result)
    result = stub_.GetResult(
           api_pb2.GetResultRequest(
             trial_name="deas",
             namespace="default",
           ),
    )
    print(result)

if __name__ == "__main__":
    main()
