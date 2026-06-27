import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.config import BASE_URL

@pytest.fixture

def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("remote-debugging-port-9222")
    options.add_argument("--disable_dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
    
    
    driver.get(BASE_URL)  

    yield driver

    driver.quit()