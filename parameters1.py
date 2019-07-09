import settings
import pytest
from selenium import webdriver
import time
import math


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(settings.BROWSER_DRIVER)
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('urlId', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestPageAnswer(object):
    def test_page(self, browser, urlId):
        link = f"https://stepik.org/lesson/{urlId}/step/1/"
        browser.get(link)
        textareaAnswer = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        textareaAnswer.send_keys(f"{answer}")
        sendBtn = browser.find_element_by_css_selector(
            "button.submit-submission")
        sendBtn.click()
        feedback = browser.find_element_by_css_selector(".smart-hints__hint")
        feedbackTxt = feedback.text
        assert "Correct!" == feedbackTxt, f"Не корректно: {feedbackTxt}"
