import os

def take_screenshot(driver,filename):

    os.makedirs("screenshots",exist_ok = True)

    path = f"screenshots/{filename}.png"

    driver.save_screenshot(path)

    
