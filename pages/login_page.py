from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.LoginPageLocators.LOGIN_URL_PART in self.browser.current_url, "Not login in the URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # регистрирует пользователя
        input_email = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL)
        input_pass1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS1)
        input_pass2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS2)
        button_submit = self.browser.find_element(
            *LoginPageLocators.REGISTER_SUBMIT)
        input_email.send_keys(email)
        input_pass1.send_keys(password)
        input_pass2.send_keys(password)
        button_submit.click()
