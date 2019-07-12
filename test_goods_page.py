from pages.goods_page import GoodsPage
import pytest
import time


# @pytest.mark.parametrize('offer', [i for i in range(0, 9)])
# def test_guest_can_add_goods_to_basket(browser, offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page = GoodsPage(browser, link)
#     page.open()  # открываем страницу
#     # нажимаем на кнопку добавления товара в корзину
#     page.click_to_add_basket_button()
#     # выполняем метод подсчёта результата математического выражения
#     page.solve_quiz_and_get_code()
#     # pytest -s -v --tb=line --language=en
#     page.should_be_message_about_goods_name()
#     page.should_be_message_about_goods_price()
#     print(link)


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = GoodsPage(browser, link)
    page.open()  # открываем страницу
    # нажимаем на кнопку добавления товара в корзину
    page.click_to_add_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = GoodsPage(browser, link)
    page.open()  # открываем страницу
    # нажимаем на кнопку добавления товара в корзину
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = GoodsPage(browser, link)
    page.open()  # открываем страницу
    # нажимаем на кнопку добавления товара в корзину
    page.click_to_add_basket_button()
    time.sleep(2)  # Иначе не успевает появиться и тест падает сразу
    page.should_be_success_message_disappear()
