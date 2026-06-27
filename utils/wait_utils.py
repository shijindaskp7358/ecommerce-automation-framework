from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_visibility(driver,locator,timeout=10):
    return WebDriverWait(driver,timeout).until(EC.visibility_of_element_located(locator))

def wait_for_presence(driver,locator,timeout=10):
    return WebDriverWait(driver,timeout).until(EC.presence_of_element_located(locator))

def wait_for_clickable(driver,locator,timeout=15):
    return WebDriverWait(driver,timeout).until(EC.element_to_be_clickable(locator))

def wait_for_url(driver,url,timeout=10):
    return WebDriverWait(driver,timeout).until(EC.url_contains(url))

def wait_for_text(driver,locator,text,timeout=10):
    return WebDriverWait(driver,timeout).until(EC.text_to_be_present_in_element(locator,text))

def wait_for_title(driver,title,timeout=10):
   return  WebDriverWait(driver,timeout).until(EC.title_contains(title))

def wait_for_alert(driver,timeout=10):
    return WebDriverWait(driver,timeout).until(EC.alert_is_present())