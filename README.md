[![GitHub license](https://img.shields.io/github/license/tryterra/terra-client-python)](https://github.com/tryterra/terra-client-python/blob/master/LICENSE)
[![docs](https://github.com/tryterra/terra-client-java/actions/workflows/docs.yml/badge.svg)](https://tryterra.github.io/terra-client-python/)

# Terra Python Package

A wrapper in python for the Terra endpoints and models.

User Guide: https://docs.tryterra.co/docs/python-project-1


Install using

```sh
pip install terra-python
```

Then import the `Terra` class from terra.base_client

Initialise a new Terra instance with:

```py
from terra.base_client import Terra

# For user authentication
terra = Terra(api_key='YOUR API KEY', dev_id='YOUR DEV ID');

# For web hook endpoints
terra = Terra(api_key='YOUR API KEY', dev_id='YOUR DEV ID', secret='YOUR TERRA SECRET');
```

Now you can call the following functions from the instance:

- `from_user_id`
- `get_activity_for_user`
- `get_body_for_user`
- `get_daily_for_user`
- `get_sleep_for_user`
- `get_athlete_for_user`
- `get_menstruation_for_user`
- `get_nutrition_for_user`
- `generate_widget_session`
- `generate_authentication_url`
- `get_user_info`
- `deauthenticate_user`
- `list_users`
- `list_providers`
- `check_terra_signature`
- `handle_flask_webhooks`
- `handle_webhooks`

The documentation for the wrapper is available here: https://tryterra.github.io/terra-client-python/

In addition, all the data models documented on [https://docs.tryterra.co/docs/data-models] are available to import and use.

The models support autocompleting the types to manipulate data coming from Terra
