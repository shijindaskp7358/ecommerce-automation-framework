from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    PRODUCT_NAME = (By.CLASS_NAME,"inventory_item_name")
    
    CHECKOUT_BUTTON = (By.ID,"checkout")


    def checkout_button(self):
       self.wait_for_page("cart.html")
       self.click(self.CHECKOUT_BUTTON)
    
    
    
        