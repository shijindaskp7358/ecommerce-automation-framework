# Ecommerce UI Automation Framework

I built this project to practice Selenium automation using 
Python. The target application is SauceDemo which is a demo 
ecommerce website used for testing practice.

## Why I Built This

After learning Selenium basics I wanted to build something 
structured. I followed Page Object Model pattern because it 
keeps locators and test logic separate which makes the code 
easier to maintain.

## What I Used
- Python
- Selenium
- Pytest
- WebDriver Manager
- pytest-html

## What I Tested

I focused on the login functionality covering:
- Valid login with correct credentials
- Invalid login with wrong credentials
- Empty username scenario
- Empty password scenario
- Multiple user types using parametrize

## What I Learned
- Page Object Model structure
- How BasePage helps avoid code repetition
- Using fixtures for driver setup and teardown
- Taking screenshots when tests fail
- Difference between smoke and regression tests

## How to Run

Install packages:
pip install -r requirements.txt

Run smoke tests only:
pytest -m smoke -v

Run regression tests:
pytest -m regression -v

Run all tests with report:
pytest -v --html=reports/report.html

## Author
Shijindas KP
github.com/shijindaskp7358
linkedin.com/in/shijindas-kp-19b631276