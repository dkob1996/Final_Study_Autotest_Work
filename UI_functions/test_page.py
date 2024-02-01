import yaml
from selenium.webdriver.common.by import By
from UI_functions.BaseApp import BasePage
from path.static_paths import *

class TestSearchLocator:
    # Parse data from yaml files
    with open(yaml_ui_locators()) as f:
    ## Parse locators from yaml file to dictionary
        locators = yaml.safe_load(f)
    ids = dict()
    for locator in locators['Xpath'].keys():
        ids[locator] = (By.XPATH, locators['Xpath'][locator])
    for locator in locators['CSS_SELECTOR'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['CSS_SELECTOR'][locator])

class OperationsHelper(BasePage):
    # Func which enter text into fields with curtain locator
    def enter_text(self, locator, word):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(word)

    # Func which get text from fields with curtain locator
    def get_text(self, locator):    
        try:
            field = self.find_element(locator)
            text = field.text
        except:
            text = None
        return text

    # Func which does click to button with curtain locator
    def click_button(self, locator):
        field = self.find_element(locator)
        field.click()

    # Func which return property of css style
    def take_css_property(self, locator, property):
        field = self.get_element_property(locator, property)
        return field
    
    def get_attribute_by_xpath(self, locator, attribute):
        field = self.find_element(locator).get_attribute(attribute)
        return field
            

    # Functions which use main functions and transfer to them curtain locators
    ## Login functions                
    def enter_login(self, word):
        self.enter_text(TestSearchLocator.ids['LOGIN_FIELD'], word)
    
    def enter_password(self, word):
        self.enter_text(TestSearchLocator.ids['PASS_FIELD'], word)

    def click_login_button(self):
        self.click_button(TestSearchLocator.ids['LOGIN_BUTTON_FIELD'])

    def get_error_text(self):
        text = self.get_text(TestSearchLocator.ids['ERROR_FIELD'])
        return text
        
    def get_auth_text(self):
        return self.get_text(TestSearchLocator.ids['HELLO_USERNAME_SEPECTOR'])
    
    ## About page functions
    def click_about_button(self):
        self.click_button(TestSearchLocator.ids['ABOUT_BUTTON'])

    def get_about_page_name(self):
        return self.get_text(TestSearchLocator.ids['ABOUT_PAGENAME'])
    
    def take_title_font_size(self):
        return self.take_css_property(TestSearchLocator.ids['ABOUT_PAGENAME'], 'font-size')

