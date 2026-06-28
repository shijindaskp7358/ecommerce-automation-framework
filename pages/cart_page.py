from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    PRODUCT_NAME = (By.CLASS_NAME,"inventory_item_name")
    
    CHECKOUT_BUTTON = (By.NAME,"checkout")
    
    def get_product_name(self):
        return self.get_text(self.PRODUCT)

    def checkout_button(self):

       self.click(self.CHECKOUT_BUTTON)
    
    
    
        