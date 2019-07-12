from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_goods_in_basket(self):
        # проверка, что нет товаров в корзине
        assert self.is_disappeared(
            *BasketPageLocators.GOODS_FORM), "Goods is not presented in basket"
