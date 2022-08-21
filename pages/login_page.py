from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        #self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_PAGE)
        except NoSuchElementException:
            return False
        return True

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        except NoSuchElementException:
            return False
        return True