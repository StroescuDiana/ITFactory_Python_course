from selenium.webdriver.common.by import By

from main_pages.BasePage import BasePage
from main_pages.LoginPageObjects import LoginPageObjects


class Login(BasePage, LoginPageObjects):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        return super().open_url(super().log_in_page_url)

    def execute_valid_login(self):
        username_locator = (By.XPATH, super().username_field_xpath)
        password_locator = (By.XPATH, super().password_field_xpath)
        submit_locator = (By.XPATH, super().submit_login_button_xpath)

        super().type(username_locator, super().valid_username)
        super().type(password_locator, super().valid_password, 9)
        super().click(submit_locator)