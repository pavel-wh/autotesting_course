import settings
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную маркировку:
# pytest -s -v -m smoke test_fixture3.py
# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
# pytest -s -v -m "not smoke" test_fixture3.py
# Объединение тестов с разными маркировками Для запуска тестов с разными маркировками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:
# pytest -s -v -m "smoke or regression" test_fixture3.py
# Чтобы запустить только smoke-тесты для windows10, нужно использовать логическое И:
# pytest -s -v -m "smoke and win10" test_fixture3.py
# Чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip:
# Опционально к маркировке skip можно добавить параметр reason, который указывает на причину, почему тест запускать не нужно, указанный в reason текст также будет выведен в тестовый отчет в консоль. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rsx. Добавлять поясняющие комментарии — это хорошая практика, потому что реальную причину можно быстро забыть или потерять в большом тестовом фреймворке. Добавляется параметр так:
# @pytest.mark.skip(reason="no way of currently testing this")
# Пока разработчики исправляют баг, мы хотим, чтобы результат прогона всех наших тестов был успешен, но падающий тест помечался соответствующим образом, чтобы про него не забыть. Добавим маркировку @pytest.mark.xfail для падающего теста и запустим наш тест-сьют.


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(settings.BROWSER_DRIVER)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
