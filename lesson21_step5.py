from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

try: 
    link = "http://suninjuly.github.io/math.html"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value')
    x1 = int(x.text)
    f = log(abs(12 * sin(x1)))
    
    field = browser.find_element(By.ID, 'answer')
    field.send_keys(str(f))
    time.sleep(2)
    
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    time.sleep(2)
    
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    time.sleep(2)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    time.sleep(10)
finally:
    browser.quit()
    
    