
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Testing(unittest.TestCase, Base, WebElements):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_positive_exercises(self):


        search_box_locator = (By.XPATH, super().search_box_xpath)
        super().search_item(search_box_locator, "iphone 14")
        search_button_locator = (By.XPATH, super().search_button)
        super().click(search_button_locator)

    def tearDown(self):
        self.driver.quit()