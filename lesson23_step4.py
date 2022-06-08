import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *


def calc(x):
    f = log(abs(12 * sin(x)))
    return f


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    browser.switch_to.alert.accept()
    x1 = int(browser.find_element(By.ID, 'input_value').text)
    f1 = calc(x1)
    browser.find_element(By.ID, 'answer').send_keys(f1)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
