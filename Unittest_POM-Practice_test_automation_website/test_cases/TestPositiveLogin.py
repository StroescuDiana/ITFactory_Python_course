"""
Test case 1: Positive LogIn test
Open page https://practicetestautomation.com/practice-test-login/
Type username student into Username field
Type password Password123 into Password field
Push Submit button
Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Verify new page contains expected text ('Congratulations' or 'successfully logged in')
Verify button Log out is displayed on the new page
"""


import unittest

from selenium import webdriver

from main_pages.logged_in_successfully import LoggedInSuccessfully
from main_pages.login_page import Login
from page_objects.LoginPageObjects import LoginPageObjects
from page_objects.SuccessfullyLoggedIn_objects import SuccessfullyLoggedIn_objects


class TestPositiveLogin(unittest.TestCase, LoginPageObjects, SuccessfullyLoggedIn_objects):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_positive_login(self):

        login = Login(self.driver)
        login.open()  #Open page https://practicetestautomation.com/practice-test-login/

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login.execute_valid_login()

        logged_in = LoggedInSuccessfully(self.driver)
        assert logged_in.get_expected_url() == logged_in.get_current_url(), "Actual URL is not the same as expected"  #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert logged_in.get_header_message() == super().successfully_logged_in_text, "Header message not as expected"  #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in.is_logout_button_displayed(), "Logout button should be visible"  #Verify button Log out is displayed on the new page

    def tearDown(self):
        self.driver.quit()