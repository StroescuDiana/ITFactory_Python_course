import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Elefant_ro_site.main.Classes import OpenPage, Negative_log_in


class TestNegative(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_negative_exercises(self):

        elefant_ro = OpenPage(self.driver)
        elefant_ro.open_page()

        log_in = Negative_log_in(self.driver)
        log_in.negative()
        log_in.invalid_email_login()

    def tearDown(self):
        self.driver.quit()