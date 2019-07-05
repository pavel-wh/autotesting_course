from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome("D:\\Soft\\chromedriver_win32\\chromedriver.exe")
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_id("book")
data = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
)
button.click()


x = browser.find_element_by_id("input_value").text
inpute = browser.find_element_by_id("answer")
inpute.send_keys(calc(x))
sub = browser.find_element_by_id("solve")
sub.click()

# Обратите внимание, что в объекте WebDriverWait используется функция until, в которую передается правило ожидания, элемент, а так же значение, по которому мы будем искать элемент. В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
# Описание каждого правила можно найти на https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions.

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной

# button = WebDriverWait(browser, 5).until_not(
#     EC.element_to_be_clickable((By.ID, "check"))
# )

# В этом уроке мы постарались собрать ссылки на ресурсы, где вы сможете найти дополнительную информацию по использованию Selenium и о тонкостях при работе с ним:

# Общее

# https: // selenium-python.com/
# http: // selenium-python.readthedocs.io
# http: // chromedriver.chromium.org/getting-started
# https: // www.guru99.com/selenium-tutorial.html - Туториал на английском, ориентирован на Java.
# https: // www.guru99.com/live-selenium-project.html - Можно попробовать писать автотесты для демо-сайта банка. Тоже Java.
# Ожидания в Selenium WebDriver

# https: // docs.seleniumhq.org/docs/04_webdriver_advanced.jsp
# https: // selenium-python.readthedocs.io/waits.html
# module-selenium.webdriver.support.expected_condition...
# https: // selenium-python.readthedocs.io/api.html
# https: // stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
# https: // blog.codeship.com/get-selenium-to-wait-for-page-load/
