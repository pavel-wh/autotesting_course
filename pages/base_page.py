from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        """Конструктор класса.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """метод открывает нужную страницу,
        используя метод get()
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """метод в котором будем перехватываем исключение. 
        В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор). 
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
