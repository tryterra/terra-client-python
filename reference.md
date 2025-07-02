# Reference
## Authentication
<details><summary><code>client.authentication.<a href="src/terra/authentication/client.py">authenticateuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a login link that allows end users to connect their fitness tracking account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.authentication.authenticateuser(
    resource="FITBIT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource:** `str` — Provider resource identifier (e.g., 'FITBIT', 'GARMIN', 'OURA'). See "Get detailed list of integrations" for available providers
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_success_redirect_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_failure_redirect_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/terra/authentication/client.py">generatewidgetsession</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a link to redirect an end user to for them to select an integration and log in with their fitness data provider
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.authentication.generatewidgetsession()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**providers:** `typing.Optional[str]` — Comma separated list of providers to display on the device selection page. This overrides your selected sources on your dashboard
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Display language of the widget
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Identifier of the end user on your system, such as a user ID or email associated with them
    
</dd>
</dl>

<dl>
<dd>

**auth_success_redirect_url:** `typing.Optional[str]` — URL the user is redirected to upon successful authentication
    
</dd>
</dl>

<dl>
<dd>

**auth_failure_redirect_url:** `typing.Optional[str]` — URL the user is redirected to upon unsuccessful authentication
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/terra/authentication/client.py">deauthenticateuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all records of the user on Terra's end, revoking Terra's access to their data
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.authentication.deauthenticateuser(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to deauthenticate and remove from Terra system
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/terra/authentication/client.py">generateauthtoken</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a token to be used with initConnection() functions in the Terra mobile SDKs in order to create a user record for Apple Health or Samsung Health (or equivalent)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.authentication.generateauthtoken()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User
<details><summary><code>client.user.<a href="src/terra/user/client.py">modifyuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Terra user's reference_id or active status
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.user.modifyuser(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID to update
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Identifier on your system to associate with this user
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether the user should remain active
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/terra/user/client.py">getinfoforuserid</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to query for information on one Terra user ID, or to query for all registered Terra User objects under one reference ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.user.getinfoforuserid()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — user ID to query for
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — reference ID to query for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/terra/user/client.py">getalluserids</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to query for information for all Terra User IDs. Supports optional pagination via `page` and `per_page`. If `page` is not provided, it returns all users in one go (backwards compatibility).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.user.getalluserids()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page number. If omitted, results are not paginated.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page (default is 500).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/terra/user/client.py">getinfoformultipleuserids</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to query for information for multiple Terra User IDs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.user.getinfoformultipleuserids(
    request=["string"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Activity
<details><summary><code>client.activity.<a href="src/terra/activity/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches completed workout sessions, with a defined start and end time and activity type (e.g. running, cycling, etc.)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.activity.fetch(
    user_id="user_id",
    start_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `ActivityFetchRequestStartDate` — Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**with_samples:** `typing.Optional[bool]` — Boolean flag specifying whether to include detailed samples in the returned payload (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activity.<a href="src/terra/activity/client.py">write</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to post activity data to a provider. This endpoint only works for users connected via Wahoo. Returns error for other providers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Activity, ActivityMetadata, Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.activity.write(
    data=[
        Activity(
            metadata=ActivityMetadata(
                end_time="2022-10-28T10:00:00.000000+01:00",
                start_time="1999-11-23T09:00:00.000000+02:00",
                summary_id="123e4567-e89b-12d3-a456-426614174000",
                type=1.1,
                upload_type=1.1,
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[Activity]` — List of user-tracked workouts to post to data provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Athlete
<details><summary><code>client.athlete.<a href="src/terra/athlete/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches relevant profile info such as first & last name, birth date etc. for a given user ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.athlete.fetch(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Body
<details><summary><code>client.body.<a href="src/terra/body/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches body metrics such as weight, height, body fat percentage etc. for a given user ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.body.fetch(
    user_id="user_id",
    start_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `BodyFetchRequestStartDate` — Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**with_samples:** `typing.Optional[bool]` — Boolean flag specifying whether to include detailed samples in the returned payload (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.body.<a href="src/terra/body/client.py">write</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to post body data to a provider. This endpoint only works for users connected via Google Fit. Returns error for other providers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Body, BodyMetadata, Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.body.write(
    data=[
        Body(
            metadata=BodyMetadata(
                end_time="2022-10-28T10:00:00.000000+01:00",
                start_time="1999-11-23T09:00:00.000000+02:00",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[Body]` — Body measurement metrics to post to data provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.body.<a href="src/terra/body/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to delete Body metrics the user has registered on their account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.body.delete(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**log_ids:** `typing.Optional[typing.Sequence[str]]` — List of identifiers for body metrics entries to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Daily
<details><summary><code>client.daily.<a href="src/terra/daily/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches daily summaries of activity metrics such as steps, distance, calories burned etc. for a given user ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.daily.fetch(
    user_id="user_id",
    start_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `DailyFetchRequestStartDate` — Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**with_samples:** `typing.Optional[bool]` — Boolean flag specifying whether to include detailed samples in the returned payload (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Menstruation
<details><summary><code>client.menstruation.<a href="src/terra/menstruation/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches menstruation data such as cycle length, period length, ovulation date etc. for a given user ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.menstruation.fetch(
    user_id="user_id",
    start_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `MenstruationFetchRequestStartDate` — Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**with_samples:** `typing.Optional[bool]` — Boolean flag specifying whether to include detailed samples in the returned payload (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Nutrition
<details><summary><code>client.nutrition.<a href="src/terra/nutrition/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches nutrition log data such as meal type, calories, macronutrients etc. for a given user ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.nutrition.fetch(
    user_id="user_id",
    start_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `NutritionFetchRequestStartDate` — Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**with_samples:** `typing.Optional[bool]` — Boolean flag specifying whether to include detailed samples in the returned payload (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nutrition.<a href="src/terra/nutrition/client.py">write</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to post nutrition logs to a provider. This endpoint only works for users connected via Fitbit. Returns error for other providers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Nutrition, NutritionMetadata, Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.nutrition.write(
    data=[
        Nutrition(
            metadata=NutritionMetadata(
                end_time="2022-10-28T10:00:00.000000+01:00",
                start_time="1999-11-23T09:00:00.000000+02:00",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[Nutrition]` — Nutrition entry to post to data provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nutrition.<a href="src/terra/nutrition/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to delete nutrition logs the user has registered on their account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.nutrition.delete(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Sequence[str]]` — List of identifiers for nutrition entries to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sleep
<details><summary><code>client.sleep.<a href="src/terra/sleep/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches sleep data such as sleep duration, sleep stages, sleep quality etc. for a given user ID, for sleep sessions with a defined start and end time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.sleep.fetch(
    user_id="user_id",
    start_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `SleepFetchRequestStartDate` — Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**with_samples:** `typing.Optional[bool]` — Boolean flag specifying whether to include detailed samples in the returned payload (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Plannedworkout
<details><summary><code>client.plannedworkout.<a href="src/terra/plannedworkout/client.py">fetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to get workout plans the user has registered on their account. This can be strength workouts (sets, reps, weight lifted) or cardio workouts (warmup, intervals of different intensities, cooldown etc)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.plannedworkout.fetch(
    user_id="user_id",
    start_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `PlannedWorkoutFetchRequestStartDate` — Start date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for data query - either ISO8601 date (YYYY-MM-DD) or unix timestamp in seconds (10-digit)
    
</dd>
</dl>

<dl>
<dd>

**to_webhook:** `typing.Optional[bool]` — Boolean flag specifying whether to send the data retrieved to the webhook instead of in the response (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plannedworkout.<a href="src/terra/plannedworkout/client.py">write</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to post workout plans users can follow on their wearable. This can be strength workouts (sets, reps, weight lifted) or cardio workouts (warmup, intervals of different intensities, cooldown etc)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import PlannedWorkout, Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.plannedworkout.write(
    data=[PlannedWorkout()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[PlannedWorkout]` — PlannedWorkout entry to post to data provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plannedworkout.<a href="src/terra/plannedworkout/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Used to delete workout plans the user has registered on their account. This can be strength workouts (sets, reps, weight lifted) or cardio workouts (warmup, intervals of different intensities, cooldown etc)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.plannedworkout.delete(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Terra user ID (UUID format) to retrieve data for
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[typing.Sequence[str]]` — List of identifiers for planned workout entries to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Integrations
<details><summary><code>client.integrations.<a href="src/terra/integrations/client.py">fetch</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all available provider integrations on the API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.integrations.fetch()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/terra/integrations/client.py">detailedfetch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a detailed list of supported integrations, optionally filtered by the developer's enabled integrations and the requirement for SDK usage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from terra import Terra

client = Terra(
    dev_id="YOUR_DEV_ID",
    api_key="YOUR_API_KEY",
)
client.integrations.detailedfetch()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdk:** `typing.Optional[bool]` — If `true`, allows SDK integrations to be included in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

