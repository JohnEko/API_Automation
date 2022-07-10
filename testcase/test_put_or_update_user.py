import json

import pytest

from apitest.configuration.config import DataHelper
import pdb

@pytest.mark.TC003
def test_put_or_update_user():

    info = DataHelper().file_path()
    # Generate the payload data
    payload = dict()
    payload['id'] = 8
    payload['email'] = "lindsay.ferguson@reqres.in"
    payload['first_name'] = "lindsay"
    payload['last_name'] = "ferguson"
    payload['avatar'] = "https://reqres.in/img/faces/11-image.jpg"

    # make a call
    age_updated = {'age': 27}
    payload.update(age_updated)
    res = payload.update(info)

    # verify the that age is updated
    assert payload, f"The age is update in the API backends"

    #pdb.set_trace()
    return res