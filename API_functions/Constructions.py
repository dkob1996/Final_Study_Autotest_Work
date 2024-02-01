import yaml
import requests
from path.static_paths import *

# Import setting-up data
with open(yaml_api_config()) as f:
   data = yaml.safe_load(f)

## API data
api_login_url = data['login_url']
api_username = data['username']
api_password = data['password']
## Create post data
api_post_url = data['posts_url']
api_post_title = data['title']
api_post_description = data['description']
api_post_content = data['content']
## Profile
profile_url = data['profile_url']

## Func which takes user auth token
def take_auth_token():
    response = requests.post(api_login_url, data={'username':api_username, 'password': api_password})
    token = response.json()['token']
    data['token']=token
    return token

def post_item(token):
    item_data = requests.post(api_post_url, headers={'X-Auth-Token': token},data={
        'username': api_username,
        'password': api_password,
        'title': api_post_title,
        'description': api_post_description,
        'content':api_post_content})
    return item_data

def get_author_id_from_post(token):
    data = post_item(token)
    return data.json()['authorId']

def get_author_info(token, authorID):
    user_data = requests.get(f'{profile_url}{authorID}/', headers={'X-Auth-Token': token})
    return user_data

def get_author_username(token, authorID):
    data = get_author_info(token, authorID)
    return data.json()["item"]['username']