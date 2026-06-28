from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_visibility

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
        postal_field = wait_for_visibility(self.driver,self.POSTAL_CODE)
        postal_field.submit()

    def click_finish_button(self):
        self.click(self.FINISH_BUTTON)

