from selenium.webdriver.common.by import By

from main_pages.base_page import BasePage
from page_objects.LoginPageObjects import LoginPageObjects


class Login(BasePage, LoginPageObjects):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        return super().open_url(super().log_in_page_url)

    def execute_valid_login(self):
        super().type(super().username_locator, super().valid_username)
        super().type(super().password_locator, super().valid_password, 9)
        super().click(super().submit_login_button_locator)

    def execute_negative_username_login(self):
        super().type(super().username_locator, super().invalid_username)
        super().type(super().username_locator, super().valid_password)
        super().click(super().submit_login_button_locator)

    def execute_negative_password_login(self):
        super().type(super().username_locator, super().valid_username)
        super().type(super().username_locator, super().invalid_password)
        super().click(super().submit_login_button_locator)

    def visibility_of_error_message(self):
        super().wait_for_visible_element(super().error_message)
        return super().is_displayed(super().error_message)

    def get_error_message(self):
        return super().get_text(super().error_message)
