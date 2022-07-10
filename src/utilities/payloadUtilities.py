
from apitest.configuration.config import DataHelper
#from apitest.helperclass.customerHelper import CustomerHelper
import os
import json
import requests
import pdb


class PayloadUtility(object):

    def __init__(self):

        self.env = os.environ.get('ENV', 'test')
        self.payloads_utility = DataHelper().file_path()



    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code." \
        f"Expected is {self.expected_status_code}, Actual status code:{self.status_code}" \
        f"URL:{self.endpoint}, Response json:{self.rs_json}"  # make sure the endpoint here is pass to the function created , post, get, update and delete

    def getAPI(self, get_endpoint, payload=None, expected_status_code=200):

        rs_api = self.payloads_utility.get(get_endpoint, payload)
        self.endpoint = get_endpoint
        #pdb.set_trace()
        self.status_code = expected_status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api #.json()
        #pdb.set_trace()
        assert rs_api

        return self.rs_json




    def post(self, endpoint, payload=None, header=None, expected_status_code=201):


        rs_api = requests.post(endpoint, data=json.dumps(payload))
        self.status_code = expected_status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api
        self.endpoint = endpoint
        pdb.set_trace()
        assert rs_api

        return self.rs_json

    def put(self, endpoint, payload, expected_status_code=201):

        rs_api = self.payloads_utility.get(endpoint, payload)

        self.status_code = rs_api
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api
        self.endpoint = endpoint
        assert self.rs_json

        pdb.set_trace()

    def deleteAPI(self):

        pass