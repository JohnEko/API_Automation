import pytest
from apitest.helperclass.customerHelper import CustomerHelper
from apitest.helperclass.payloadhelper import PayloadUtility
from apitest.helperclass.payloadhelper import PayloadHelper
from apitest.configuration.config import DataHelper
import pdb
import requests


@pytest.mark.TC002
def test_create_payload():

    info = DataHelper().file_path()
    #Generate the payload data
    payload = dict()
    payload['id'] = 13
    payload['email'] = "automation@gov.com"
    payload['first_name'] = "John"
    payload['last_name'] = "naija"
    payload['avatar'] = "https://reqres.in/img/faces/11-image.jpg"

    # make a call
    res_info = payload.update(info)


   # verify the status code
    assert payload, f"New payload created on the backend{res_info}"
    assert payload['email'] == "automation@gov.com", f"Payload created on the backend{res_info}"

    return res_info
    #pdb.set_trace()
    # verify the email response

# verify customer is created on dbc