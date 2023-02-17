import os
from locust import HttpUser, task
import json

default_host = os.environ["ServiceName"]
if not default_host.startswith('http://'):
    default_host = 'http://' + default_host
model = os.environ["MODEL_NAME"]

def reservedModel(model):
    method, page, params, data, filename = 'Get', '/', None, None, None
    if model == "MLPerf-FaaS-3DUNet":
        method = 'POST'
        page = '/predict'
        filename = 'reserved_model_data/sample.pkl'
    elif model == "MLPerf-FaaS-BERT":
        method = 'GET'
        params = {'question' : 'What%20food%20does%20Harry%20like?', 
                  'context'  : 'My%20name%20is%20Harry%20and%20I%20grew%20up%20in%20Canada.%20I%20love%20bananas.'}
    elif model == "MLPerf-FaaS-GNMT":
        method = 'POST'
        page = '/v1/models/gnmt:predict'
        seq = "He has a doctorate in technical sciences."
        data = json.dumps({'inputs': seq})
    elif model == "MLPerf-FaaS-ResNet":
        method = 'POST'
        filename = 'reserved_model_data/car.jpg'
        page = '/predict'
    elif model == "MLPerf-FaaS-RetinaNet":
        method = 'POST'
        filename = 'reserved_model_data/car.jpg'
        page = '/predict'
    elif model == "MLPerf-FaaS-RNNT":
        method = 'POST'
        filename = 'reserved_model_data/en.wav'
        page = '/predict'
    return method, page, params, data, filename

class MyHttpUser(HttpUser):
    method, page, params, data, filename = reservedModel(model)
    host = os.getenv("HTTP_HOST", default_host)
    assert host != ""

    @task
    def access(self):
        files = None
        if self.filename != None:
          payload = open(self.filename, 'rb')
          files = {'payload': payload}

        self.client.request(method=self.method, url=self.page, params=self.params, data=self.data, files=files)
