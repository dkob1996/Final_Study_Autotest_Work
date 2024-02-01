import yaml
from UI_functions.test_page import OperationsHelper
from path.static_paths import *

# Test commands:
## Start current test
### pytest test_1.py -vv

# Import test data
with open(yaml_ui_testdata()) as f:
    testdata = yaml.safe_load(f)
## Auth data
name = testdata["username"]
passwd = testdata["password"]
## Valid data
valid_user_name = testdata["hello_prefix"]
## Invalid data
invalid_login_data = testdata["invalid_login_data"]
## Errors data
error_401 = testdata['401_error']
## Setting-up data
site_address = testdata['address']


## Step 1: Login with invalid data
def test_step1(browser):
    page = OperationsHelper(address=site_address, driver= browser)
    page.go_to_site()
    page.enter_login(invalid_login_data)
    page.enter_password(invalid_login_data)
    page.click_login_button()
    assert page.get_error_text() == error_401

## Step 2: Login with valid data
def test_step2(browser):
    page = OperationsHelper(address=site_address, driver= browser)
    page.enter_login(name)
    page.enter_password(passwd)
    page.click_login_button()
    assert page.get_auth_text() == f'{valid_user_name}, {name}'
    