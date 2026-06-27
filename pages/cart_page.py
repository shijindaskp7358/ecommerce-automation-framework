from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_clickable

class CartPage(BasePage):

    PRODUCT_NAME = (By.CLASS_NAME,"inventory_item_name")
    
    CHECKOUT_BUTTON = (By.ID,"checkout")


    def checkout_button(self):

        button = wait_for_clickable(self.driver,self.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();",button)
    
        