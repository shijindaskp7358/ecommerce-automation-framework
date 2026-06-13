import pytest
from pages.login_page import LoginPage
from config.config import *

@pytest.mark.smoke
def test_valid_login(driver):

    login_page = LoginPage(driver)

    driver.get(BASE_URL)

    login_page.login(USERNAME,PASSWORD)
    
    assert "inventory" in driver.current_url

@pytest.mark.regression
def test_invalid_login(driver):

    login_page = LoginPage(driver)

    driver.get(BASE_URL)
    login_page.login("wrong_user","wrong_password")

    assert login_page.get_error_message() == \
    "Epic sadface: Username and password do not match any user in this service"    
@pytest.mark.regression
def test_empty_username(driver):

    login_page = LoginPage(driver)

    driver.get(BASE_URL)

    login_page.login("",PASSWORD)

    assert "Username is required" in login_page.get_error_message()
@pytest.mark.regression
def test_empty_password(driver):

    login_page = LoginPage(driver)

    driver.get(BASE_URL)

    login_page.login(USERNAME,"")

    assert "Password is required" in login_page.get_error_message()

#parametrized login
@pytest.mark.regression
@pytest.mark.parametrize("username,password",[
    ("standard_user","secret_sauce"),
    ("problem_user","secret_sauce"),
    ("performance_glitch_user","secret_sauce")
  ]
 )

def test_multiple_valid_users(driver,username,password):

    login_page = LoginPage(driver)

    driver.get(BASE_URL)

    login_page.login(username,password)

    assert "inventory" in driver.current_url
