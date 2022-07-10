import pytest
import logging as logger
from apitest.src.utilities.payloadUtilities import PayloadUtility
import pdb


@pytest.mark.TC001
def test_get_payload():
    logger.info("***************New Customer Created*********************")

    request_payloads = PayloadUtility()
    #pdb.set_trace()
    response = request_payloads.getAPI("data")
    assert response

    return response

    #create a payload
    #rs_response = PayloadHelper()
    #pld_api = rs_response.get()

    #make a call

    #verify the status code

    #verify the email response

    #verify customer is created on db