import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('Egor')
    browser.find_element(By.NAME, 'lastname').send_keys('Rub')
    browser.find_element(By.NAME, 'email').send_keys('aa@gmail.com')
    choose = browser.find_element(By.CSS_SELECTOR, 'input#file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    choose.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()
