from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import *


def test_ecommerce_flow(driver):

#Login page

    login_page = LoginPage(driver)


    login_page.login(USERNAME,PASSWORD)

#Inventory page

    inventory_page = InventoryPage(driver)

    inventory_page.add_product_to_cart()
    inventory_page.go_to_cart()

#Cart page

    cart_page = CartPage(driver)

    
    cart_page.checkout_button()

#Checkout page

    checkout_page = CheckoutPage(driver)

    login_page.wait_for_page("checkout-step-one.html")
    checkout_page.enter_checkout_details(FIRST_NAME,LAST_NAME,POSTAL_CODE)
    checkout_page.click_continue_button()
    checkout_page.click_finish_button()
    
    assert "Thank you for your order!" in driver.page_source