import yaml
from path.static_paths import *
from API_functions.Constructions import *

with open(yaml_api_config()) as f:
    data = yaml.safe_load(f)

## API data
api_username = data['username']


## Step 1: Check username from request and testdata
def test_step1():
    token = take_auth_token()
    authorID = get_author_id_from_post(token)
    assert get_author_username(token, authorID) == api_username

