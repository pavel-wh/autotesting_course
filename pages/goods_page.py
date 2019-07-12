import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import GoodsPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class GoodsPage(BasePage):
    def solve_quiz_and_get_code(self):
        """метод для подсчёта результата математического выражения и вывода ответа.
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def click_to_add_basket_button(self):
        basket_button = self.browser.find_element(
            *GoodsPageLocators.ADD_BASKET_BUTTON)
        basket_button.click()

    def should_be_message_about_goods_name(self):
        name_goods = self.browser.find_element(
            *GoodsPageLocators.NAME_GOODS)
        message_name_goods = self.browser.find_element(
            *GoodsPageLocators.MESSAGE_NAME_GOODS)
        assert name_goods.text == message_name_goods.text, "Goods name not match"

    def should_be_message_about_goods_price(self):
        price_goods = self.browser.find_element(
            *GoodsPageLocators.PRICE_GOODS)
        message_price_goods = self.browser.find_element(
            *GoodsPageLocators.MESSAGE_PRICE_GOODS)
        assert price_goods.text == message_price_goods.text, "Goods price not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*GoodsPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappear(self):
        assert self.is_not_element_present(*GoodsPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
