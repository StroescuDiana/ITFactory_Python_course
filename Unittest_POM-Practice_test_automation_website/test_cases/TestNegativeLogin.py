"""
Test case 2: Negative username test
Open page https://practicetestautomation.com/practice-test-login/
Type username incorrectUser into Username field
Type password Password123 into Password field
Push Submit button
Verify error message is displayed
Verify error message text is Your username is invalid!

Test case 3: Negative password test
Open page https://practicetestautomation.com/practice-test-login/
Type username student into Username field
Type password incorrectPassword into Password field
Push Submit button
Verify error message is displayed
Verify error message text is Your password is invalid!
"""

import unittest

from selenium import webdriver

from main_pages.base_page import BasePage
from main_pages.login_page import Login
from page_objects.LoginPageObjects import LoginPageObjects


class TestNegativeLogin(unittest.TestCase, BasePage, LoginPageObjects):

    _GREEN = '\033[92m'
    _RESET = '\033[0m'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_negative_username_login(self):
        login_page = Login(self.driver)
        login_page.open()
        login_page.execute_negative_username_login()
        assert login_page.visibility_of_error_message(), "Error message is not displayed."
        print(f"{self._GREEN}Error message is displayed.{self._RESET}")
        assert login_page.get_error_message() == super().username_invalid_expected_message, f"Actual message{login_page.get_error_message()} is different than {super().username_invalid_expected_message}."
        print(f"{self._GREEN}Error message is 'Your username is invalid!'.{self._RESET}")

    def test_negative_password_login(self):
        login_page = Login(self.driver)
        login_page.open()
        login_page.execute_negative_password_login()
        assert login_page.visibility_of_error_message(), "Error message is not displayed."
        print(f"{self._GREEN}Error message is displayed.{self._RESET}")
        assert login_page.get_error_message() == super().username_invalid_expected_message, f"Actual message{login_page.get_error_message()} is different than {super().password_invalid_expected_message}."
        print(f"{self._GREEN}Error message is 'Your password is invalid!'.{self._RESET}")

    def tearDown(self):
        self.driver.quit()