import datetime

import pytest

from terra import exceptions
from terra.models.user import User


def test_parsing_user():
    filled = User().from_dict({"user_id": "lmao"})
    assert filled.user_id == "lmao"


def test_no_client_user():
    user = User()
    with pytest.raises(exceptions.NoClientAvailable):
        user.get_activity(datetime.datetime.today())
