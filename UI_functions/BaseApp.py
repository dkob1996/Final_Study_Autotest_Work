import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from path.static_paths import *

# Import setting-up data
with open(yaml_ui_testdata()) as f:
    testdata = yaml.safe_load(f)
    # Setting-up data
    wait = testdata["wait"]


class BasePage:
    def __init__(self, address, driver):
        self.address = address
        self.driver = driver
    
    # Func of finding elements by locator
    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator),
                                                message=f"{testdata['cant_find_element_by_locator']} {locator}")
        except:
            element = None
        return element

    # Func to get element property from element which we found
    def get_element_property(self, path, property):
        element = self.find_element(path)
        if element is None:
            return None
        else:
            return (element.value_of_css_property(property))
    
    # Func which open browser in curtain address
    def go_to_site(self):
        try:
            self.driver.get(self.address)
        except:
            return False
        return True
