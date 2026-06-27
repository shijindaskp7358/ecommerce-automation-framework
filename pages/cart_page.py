from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    PRODUCT_NAME = (By.CLASS_NAME,"inventory_item_name")
    
    CHECKOUT_BUTTON = (By.ID,"checkout")


    def checkout_button(self):

        button = self.click(self.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();",button)
    
        