import yaml
import time
from UI_functions.test_page import OperationsHelper
from path.static_paths import *

# Test commands:
## Start current test
### pytest test_2.py -vv

# Import test data
with open(yaml_ui_testdata()) as f:
    testdata = yaml.safe_load(f)
## Auth data
name = testdata["username"]
passwd = testdata["password"]
## Valid data
valid_user_name = testdata["hello_prefix"]
valid_about_page_name = testdata["valid_about_page_name"]
valid_title_font_size = testdata["valid_title_font_size"]
## Setting-up data
site_address = testdata['address']
sleep_time = testdata['sleep_time']

## Step 1: Press 'About' button and check page title
def test_step1(browser):
    page = OperationsHelper(address=site_address, driver= browser)
    page.go_to_site()
    page.click_about_button()
    time.sleep(sleep_time)
    assert page.get_about_page_name() == valid_about_page_name

## Step 2: Check front size in page title
def test_step2(browser):
    page = OperationsHelper(address=site_address, driver= browser)
    assert page.take_title_font_size() == valid_title_font_size
    