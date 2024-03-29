from selenium import webdriver
import time
import settings
import pytest


def test_registration_1():
    browser = webdriver.Chrome(settings.BROWSER_DRIVER)

    # Настраиваем WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(1)
    browser.get(settings.PAGE_1)
    # Код, который заполняет обязательные поля
    element1 = browser.find_element_by_css_selector(".first:required")
    element1.send_keys("Василий")
    element2 = browser.find_element_by_css_selector(".second:required")
    element2.send_keys("Тёркин")
    element3 = browser.find_element_by_css_selector(".third:required")
    element3.send_keys("test@mail.test")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


def test_registration_2():
    browser = webdriver.Chrome(settings.BROWSER_DRIVER)
    browser.get(settings.PAGE_2)
    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element_by_css_selector(".first:required")
    element1.send_keys("Василий")
    element2 = browser.find_element_by_css_selector(".second:required")
    element2.send_keys("Тёркин")
    element3 = browser.find_element_by_css_selector(".third:required")
    element3.send_keys("test@mail.test")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


if __name__ == "__main__":
    test_registration_1()
    test_registration_2()


# Если нужно проверить, что тест вызывает ожидаемое исключение (довольно редкая ситуация для UI-тестов, и вам этот способ скорее всего никогда не пригодится), мы можем использовать специальную конструкцию with pytest.raises(). Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:
# import pytest

# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException

# browser = webdriver.Chrome()

# def test_exception():
#     browser.get("http://selenium1py.pythonanywhere.com/")
#     with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить"):
#         browser.find_element_by_css_selector("button.btn")
# Если элемент будет найден, то ошибка NoSuchElementException не возникнет, и тест упадёт.

# Traceback (most recent call last):
#   ...
# Failed: Не должно быть кнопки Отправить
