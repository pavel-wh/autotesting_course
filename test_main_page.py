from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest

"""мы можем логически сгруппировать тесты в один класс просто ради более стройного кода: удобно, когда тесты, связанные с одним компонентом лежат в одном классе, а с помощью pytest.mark можно помечать сразу весь класс. Основное правило такое: название класса должно начинаться с Test, чтобы PyTest смог его обнаружить и запустить.
"""


class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()                      # открываем страницу
        # выполняем метод страницы - переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


"""для разных тест-кейсов можно выделять общие функции, чтобы не повторять код. Эти функции называются setup — функция, которая выполнится перед запуском каждого теста из класса, обычно туда входит подготовка данных, и teardown — функция, которая выполняется ПОСЛЕ каждого теста из класса, обычно там происходит удаление тех данных, которые мы создали во время теста. Хороший автотест должен сработать даже на чистой базе данных и удалить за собой сгенерированные в тесте данные. Такие функции реализуются с помощью фикстур, которые мы изучили в предыдущем модуле. Чтобы функция запускалась автоматически перед каждым тест-кейсом, нужно пометить её как @pytest.fixture с параметрами scope="function", что значит запускать на каждую функцию, и autouse=True, что значит запускать автоматически без явного вызова фикстуры.
Мы уже немного говорили про независимость от контента в предыдущих шагах — идеальным решением было бы везде, где мы работаем со страницей продукта, создавать новый товар в нашем интернет-магазине перед тестом и удалять по завершении теста. К сожалению, наш интернет-магазин пока не имеет возможности создавать объекты по API, но в идеальном мире мы бы написали вот такой тест-класс в файле test_product_page.py:

@pytest.mark.login
class TestLoginFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

Работа с API выходит за рамки этого курса, но знание о том, что можно группировать тесты и выделять подготовительные шаги в единые для всех тестов функции — важно для каждого автоматизатора.

"""


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_goods_in_basket()
