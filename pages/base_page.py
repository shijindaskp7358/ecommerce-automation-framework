from utils.wait_utils import *
from utils.screenshot_utils import take_screenshot

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def click(self,locator):
        wait_for_clickable(self.driver,locator).click()

    def type_text(self,locator,text):
        element = wait_for_clickable(self.driver,locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return wait_for_clickable(self.driver,locator).text
    
    def is_displayed(self,locator):
        return wait_for_visibility(self.driver,locator).is_displayed()
    
    def wait_for_page(self,url):
        wait_for_url(self.driver,url)

    def wait_for_message(self,locator,text):
        wait_for_text(self.driver,locator,text)

    def get_title(self):
       return self.driver.title
    
    def take_screenshot(self,filename):
        take_screenshot(self.driver,filename)