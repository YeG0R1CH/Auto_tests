import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *


def calc(x):
    f = log(abs(12 * sin(x)))
    return f


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    f1 = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, 'answer').send_keys(f1)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(10)
finally:
    browser.quit()
