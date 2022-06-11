import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Открытие главной страницы
driver.get("https://stepik.org/catalog")
time.sleep(5)

# Ввод логина / пароля
#log_input = driver.find_element_by_id('ember363')
#log_input = driver.find_element_by_link_text('Войти')
log_input = driver.find_element(By.LINK_TEXT, 'Войти')
log_input.click()
time.sleep(2)

#email_input = driver.find_element_by_id('id_login_email')
email_input = driver.find_element(By.ID, 'id_login_email')
email_input.send_keys("yerr@mail.ru")
time.sleep(2)

#password_input = driver.find_element_by_id('id_login_password')
password_input = driver.find_element(By.ID, 'id_login_password')
password_input.send_keys("Zt")
time.sleep(2)


'''login_button = driver.find_element_by_class_name(
    'sign-form__btn.button_with-loader')'''
login_button = driver.find_element(
    By.CLASS_NAME, 'sign-form__btn.button_with-loader')
login_button.click()
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
try:
    textarea.send_keys("get()")
    time.sleep(5)
    # Найдем кнопку, которая отправляет введенное решение
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
    submit_button.click()
    time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
finally:
    driver.quit()
