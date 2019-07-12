from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class GoodsPageLocators(object):
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_GOODS = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_GOODS = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_NAME_GOODS = (
        By.CSS_SELECTOR, "#messages .alertinner>strong")
    MESSAGE_PRICE_GOODS = (
        By.CSS_SELECTOR, "#messages .alertinner p>strong")