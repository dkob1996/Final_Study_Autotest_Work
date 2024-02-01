import pytest
import yaml
import requests
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from path.static_paths import *


# Import setting-up data
with open(yaml_ui_testdata()) as f:
   testdata = yaml.safe_load(f)

## UI data
browser_name = testdata["browser"]
sleep_time = testdata["sleep_time"]

# Fixtures for UI testing
## Fuxture to set-up curtain browser where test
@pytest.fixture(scope='session')
def browser():
      if browser_name == "firefox":
         service = Service(executable_path=GeckoDriverManager().install())
         options = webdriver.FirefoxOptions()
         driver = webdriver.Firefox(service=service, options=options)
      elif browser_name == "chrome":
         service = Service(executable_path=ChromeDriverManager().install())
         options = webdriver.ChromeOptions()
         driver = webdriver.Chrome(service=service, options=options)
      driver.implicitly_wait(sleep_time)
      yield driver
      driver.quit()