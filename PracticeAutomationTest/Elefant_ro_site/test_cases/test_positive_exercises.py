import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Elefant_ro_site.main.Classes import OpenPage, SearchItem, PageTitle


class TestPositive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_positive_exercises(self):

        elefant_ro = OpenPage(self.driver)
        elefant_ro.open_page()

        iphone_14 = SearchItem(self.driver)
        iphone_14.find_item()
        iphone_14.smallest_price()

        pageTitle = PageTitle(self.driver)
        pageTitle.correct_page()

    def tearDown(self):
        self.driver.quit()
