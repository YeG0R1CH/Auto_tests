from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    im = browser.find_element(By.CSS_SELECTOR, 'img')
    im_valuex = im.get_attribute("valuex")
    x = int(im_valuex)
    f = str(calc(x))

    field = browser.find_element(By.ID, 'answer')
    field.send_keys(f)
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
