from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    n1 = int(browser.find_element(By.ID, 'num1').text)
    n2 = int(browser.find_element(By.ID, 'num2').text)
    s = n1 + n2

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(s))
    time.sleep(2)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(10)

finally:
    browser.quit()


