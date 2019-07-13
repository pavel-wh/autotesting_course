from pages.basket_page import BasketPage
from pages.goods_page import GoodsPage
import pytest
import time
from pages.login_page import LoginPage


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = GoodsPage(browser, link)
    page.open()  # открываем страницу
    # нажимаем на кнопку добавления товара в корзину
    page.should_not_be_success_message()


def test_guest_cant_see_success_message_after_adding_goods_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = GoodsPage(browser, link)
    page.open()  # открываем страницу
    # нажимаем на кнопку добавления товара в корзину
    page.click_to_add_basket_button()
    page.should_not_be_success_message()


@pytest.mark.parametrize('offer', [i for i in range(0, 9)])
def test_guest_can_add_goods_to_basket(self, browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = GoodsPage(browser, link)
    page.open()  # открываем страницу
    # нажимаем на кнопку добавления товара в корзину
    page.click_to_add_basket_button()
    # выполняем метод подсчёта результата математического выражения
    page.solve_quiz_and_get_code()
    # pytest -s -v --tb=line --language=en
    page.should_be_message_about_goods_name()
    page.should_be_message_about_goods_price()
    print(link)


def test_message_disappeared_after_adding_goods_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = GoodsPage(browser, link)
    page.open()  # открываем страницу
    # нажимаем на кнопку добавления товара в корзину
    page.click_to_add_basket_button()
    time.sleep(2)  # Иначе не успевает появиться и тест падает сразу
    page.should_be_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = GoodsPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_goods_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = GoodsPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = GoodsPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_goods_in_basket()


# @pytest.fixture(scope="class")
# def browser():
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.register_new_user(email=str(
#         time.time()) + "@fakemail.org", password=str(time.time()) + "@fakemail.org")
#     print(email=str(time.time()) + "@fakemail.org",
#           password=str(time.time()) + "@fakemail.org")


@pytest.mark.need_review
class TestUserAddToCartFromProductPage(GoodsPage):
    def test_user_cant_see_success_message_after_adding_goods_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = GoodsPage(browser, link)
        page.open()  # открываем страницу
        # нажимаем на кнопку добавления товара в корзину
        page.click_to_add_basket_button()
        page.should_not_be_success_message()

    def test_user_can_add_goods_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = GoodsPage(browser, link)
        page.open()  # открываем страницу
        # нажимаем на кнопку добавления товара в корзину
        page.click_to_add_basket_button()
        # выполняем метод подсчёта результата математического выражения
        page.solve_quiz_and_get_code()
        # pytest -s -v --tb=line --language=en
        page.should_be_message_about_goods_name()
        page.should_be_message_about_goods_price()
        print(link)
