import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_browser_language_basket_btn(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector(
        "button.btn-add-to-basket[type='submit']")
