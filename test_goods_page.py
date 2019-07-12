from pages.goods_page import GoodsPage
import pytest


@pytest.mark.parametrize('offer', [i for i in range(0, 9)])
def test_guest_can_add_goods_to_basket(browser, offer):
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
