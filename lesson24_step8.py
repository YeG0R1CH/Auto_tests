import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *


def calc(x):
    f = log(abs(12 * sin(x)))
    return f


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
    browser.find_element(By.CSS_SELECTOR, 'button#book').click()
    x1 = int(browser.find_element(By.ID, 'input_value').text)
    f1 = calc(x1)
    browser.find_element(By.ID, 'answer').send_keys(f1)
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()