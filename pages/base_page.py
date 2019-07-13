from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
            " probably unauthorised user"


"""
Плюсы наследования: магия ООП
Если вы использовали ранее парадигму ООП при написании кода, то уже представляете, как хорошая архитектура может облегчить жизнь. В этом плане код автотестов ничем не отличается от кода приложений — мы можем использовать всё те же приёмы для организации методов.

Здесь мы рассмотрим лишь один из примеров: использование механизма наследования.

Мы уже немного использовали механизм наследования, когда сделали базовый класс для всех наших проверок BasePage, а от него наследовали все остальные Page Object: LoginPage, MainPage. Сейчас у нас в классе BasePage в основном технические детали — реализация поиска элементов, метод для открытия страницы и прохождения капчи. Но никто не мешает нам добавить туда элементы и методы, которые являются общими для всех страниц.
 
ВАЖНО! Не нужно запихивать в базовый класс все, что плохо лежит и может когда-нибудь пригодиться. Добавлять нужно только то, что ОБЯЗАТЕЛЬНО будет на каждой странице-наследнике, иначе есть риск, что увеличение строк кода в файле будет неконтролируемым, и поддерживать его будет сложно.

Вообще говоря, мы можем строить какую угодно иерархию наших классов для взаимодействия с веб-приложением, если это поможет избежать дублирования кода. Например, есть набор страниц с общими методами, мы можем организовать их в виде наследования с дополнительным "слоем".

Например, когда мы тестируем страницу урока в Stepik (это та страница, на которой вы сейчас находитесь), мы используем LessonPage как базовый класс, где содержатся общие элементы и методы для всех типов шагов (шапка, комментарии, боковое расписание) и класс-наследник для каждого типа заданий, а их на Stepik более 20, каждый со своими уникальными методами и элементами. Такой подход позволяет избежать дублирования кода, и необходимости поддерживать файл на >1000 строк кода. 

"""
