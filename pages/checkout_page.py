from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID,"first-name")
    LAST_NAME = (By.ID,"last-name")
    POSTAL_CODE = (By.ID,"postal-code")
    CONTINUE_BUTTON = (By.ID,"continue")
    FINISH_BUTTON = (By.ID,"finish")

    def enter_checkout_details(self,firstname,lastname,postalcode):
        self.type_text(self.FIRST_NAME,firstname)
        self.type_text(self.LAST_NAME,lastname)
        self.type_text(self.POSTAL_CODE,postalcode)

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish_button(self):
        self.click(self.FINISH_BUTTON)