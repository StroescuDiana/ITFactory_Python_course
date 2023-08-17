from selenium.webdriver.common.by import By

from main_pages.base_page import BasePage
from page_objects.LoginPageObjects import LoginPageObjects
from page_objects.SuccessfullyLoggedIn_objects import SuccessfullyLoggedIn_objects


class LoggedInSuccessfully(BasePage, SuccessfullyLoggedIn_objects):

    def __init__(self, driver):
        super().__init__(driver)

    def get_expected_url(self):
        return super().successfully_logged_in_url

    def get_header_message(self):
        return super().get_text(super().header_locator)

    def is_logout_button_displayed(self):
        return super().is_displayed(super().logout_button_locator)