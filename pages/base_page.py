from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


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

    def is_not_element_present(self, how, what, timeout=4):
        """абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени. 
        Упадет, как только увидит искомый элемент. 
        Не появился: успех, тест зеленый. 
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """метод позволяет проверить, что какой-то элемент исчезает, следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем.
        Будет ждать до тех пор, пока элемент не исчезнет. 
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
