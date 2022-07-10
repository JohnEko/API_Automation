
from apitest.src.utilities.payloadUtilities import PayloadUtility

import pdb

class CustomerHelper():

    def __init__(self):

        self.customer_helper = PayloadUtility()

    def create_payload(self, id=None, email=None, first_name=None, last_name=None, avatar=None, **kwargs):

      #creating new json payload
        if not id:
            id='id'
        if not email:
            email = 'email'
        if not first_name:
            first_name='first_name'
        if not last_name:
            last_name = 'last_name'
        if not avatar:
            avatar = 'avatar'


        payload = dict()
        payload['id'] = id
        payload['email'] = email
        payload['first_name'] = first_name
        payload['last_name'] = last_name
        payload['avatar'] = avatar
        payload.update(**kwargs)

        #make a call from the payloads

        payload_created = self.customer_helper.post("data", payload=payload, expected_status_code=201)
        #pdb.set_trace()
        return payload_created