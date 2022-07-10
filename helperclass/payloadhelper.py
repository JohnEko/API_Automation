
from apitest.src.utilities.payloadUtilities import PayloadUtility
import requests
from apitest.configuration.config import DataHelper


class PayloadHelper(object):

    def __init__(self):

        self.payloadUtility = PayloadUtility()
        self.data_info = DataHelper().file_path()

    def get_payload(self, payload_get):

        return self.payloadUtility.get(f"payload {payload_get}")

    def call_create_payload(self, payload):
        #return self.payloadUtility.post('data', payload=payload, expected_status_code=201)


         # Need to write some code to add the post data to the database.
        return self.payloadUtility.post('data', payload=payload, expected_status_code=201)


    def put_payload(self, payload):
        return self.payloadUtility.put('payload', payload, expected_status_code=201)
