import os.path
import json
import pdb
#from apitest.src.utilities.payloadUtilities import PayloadUtility


class DataHelper(object):

    def __init__(self):
        self.current_file = os.path.dirname(os.path.realpath(__file__))
        #self.payload_helper = PayloadUtility()


    def file_path(self, endpoint=None):
        #self.args = None
        payload_json = os.path.join(self.current_file, "..", 'data', 'payload.json')

        with open(payload_json) as f:
            payload = json.load(f)
        #pdb.set_trace()
        if endpoint:
            assert isinstance(endpoint, dict)
            payload.update(endpoint)

        rs_api =payload    #(payload=payload, expected_status_code=201)

        #pdb.set_trace()

        return rs_api
        #api_response

#data = DataHelper()
#print(data.file_path(data))