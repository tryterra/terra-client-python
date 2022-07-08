# Terra Python Package

A wrapper in python for the Terra endpoints and models.


Install using

```sh
pip install terra-client
```

Then import the `Terra` class from terra.base_client

Initialise a new Terra instance with:

```py
from terra.base_client import Terra

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
- `catch_flask_webhooks`
- `catch_webhooks`

In addition, all the data models documented on https://docs.tryterra.co/data-models are available to import and use.

The models support autocompleting the types to manipulate data coming from Terra
