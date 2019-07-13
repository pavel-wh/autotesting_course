from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_URL_PART = (By.PARTIAL_LINK_TEXT, "login")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-default[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success .alertinner")


class GoodsPageLocators(object):
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_GOODS = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_GOODS = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_NAME_GOODS = (
        By.CSS_SELECTOR, "#messages .alertinner>strong")
    MESSAGE_PRICE_GOODS = (
        By.CSS_SELECTOR, "#messages .alertinner p>strong")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success .alertinner")


class BasketPageLocators(object):
    GOODS_FORM = (By.CSS_SELECTOR, "#basket_formset")
