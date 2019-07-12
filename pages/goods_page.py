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
