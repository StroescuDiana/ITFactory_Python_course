import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_something(self):
        submit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn"))).text
        print(submit)


if __name__ == '__main__':
    unittest.main()
