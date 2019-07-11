from pages.login_page import LoginPage


def test_guest_into_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.should_be_login_form()
    page.should_be_register_form()
