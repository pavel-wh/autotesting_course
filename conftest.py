# Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py, который должен лежать в директории верхнего уровня в вашем проекте с тестами. Можно создавать дополнительные файлы conftest.py в других директориях, но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.
from selenium.webdriver.chrome.options import Options
import pytest
import settings
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(
            settings.BROWSER_DRIVER_CHROME, options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(
            executable_path=settings.BROWSER_DRIVER_FIREFOX, firefox_profile=fp)
    else:
        print(f"Browser {browser_name} still is not implemented")
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()

# Встроенная фикстура request позволяет получать данные о текущем запущенном тесте, что позволяет, например, сохранять дополнительные данные в отчёт, а также делать многие другие интересные вещи. В этом шаге мы хотим показать, как можно настраивать тестовые окружения с помощью передачи параметров через командную строку. Это делается с помощью встроенной функции pytest_addoption и фикстуры request.
# https: // docs.pytest.org/en/latest/example/simple.html?highlight = addoption
# Добавим логику обработки командной строки в conftest.py. Для запроса значения параметра мы можем вызвать команду:
# browser_name = request.config.getoption("browser_name")
# Запустим тесты на Firefox:
# pytest -s -v --browser_name=firefox test_conftest.py

# Плагины и перезапуск тестов
# Для PyTest написано большое количество (https://docs.pytest.org/en/latest/plugins.html), т.е. дополнительных модулей, которые расширяют возможности этого фреймворка. Полный список доступных плагинов доступен здесь (https://plugincompat.herokuapp.com/).

# Поэтому мы будем перезапускать упавший тест, чтобы еще раз убедиться, что он действительно нашел баг, а не упал случайно.
# Это сделать очень просто. Для этого мы будем использовать плагин pytest-rerunfailures.
# Сначала установим плагин в нашем виртуальном окружении. После установки плагин будет автоматически найден PyTest, и можно будет пользоваться его функциональностью без дополнительных изменений кода:
# pip install pytest-rerunfailures == 3.1
# Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:
# "--reruns n", где n - это количество перезапусков. Если при повторных запусках тесты пройдут успешно, то и прогон тестов будет считаться успешным. Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать проблемные тесты.﻿﻿
# Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста. Можете почитать подробнее про настройку вывода в документации PyTest:
# pytest - v - -tb = line - -reruns 1 - -browser_name = chrome test_rerun.py


# Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option, как указано в примере ниже:

# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
# browser = webdriver.Chrome(options=options)
# Для Firefox объявление нужного языка будет выглядеть немного иначе:

# fp = webdriver.FirefoxProfile()
# fp.set_preference("intl.accept_languages", user_language)
# browser = webdriver.Firefox(firefox_profile=fp)
# В конструктор webdriver.Chrome или webdriver.Firefox вы можете добавлять разные аргументы, расширяя возможности тестирования ваших веб-приложений: можно указывать прокси-сервер для контроля сетевого трафика или запускать разные версии браузера, указывая локальный путь к файлу браузера. Предполагаем, что эти возможности вам понадобятся позже и вы сами сможете найти настройки для этих задач.

# pytest --browser_name=firefox --language=es test_items.py
