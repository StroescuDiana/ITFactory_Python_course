import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from Practice_test_automation_site.page_objects.LoginPageObjects import LoginPageObjects

class TestNegativeLogin(unittest.TestCase, LoginPageObjects):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10)
        self.driver.get(super().log_in_page_url)

        self.wait = WebDriverWait(self.driver, 10)

    def test_invalid_username(self):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.username_field_xpath))
        )
        username_field.send_keys(self.invalid_username)
        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, self.password_field_xpath)
        password_field.send_keys(self.valid_password)
        time.sleep(2)
        submit_button = self.driver.find_element(By.XPATH, super().submit_login_button_xpath)
        submit_button.click()
        time.sleep(1)

        error_masage = self.driver.find_element(By.ID, "error")
        assert error_masage.is_displayed(), f"{self._RED}Error mesage is not display{self._RESET}"
        print(f"{self._GREEN}Error mesage is display{self._RESET}")

        assert  error_masage.text == self.username_invalid_expected_message, f"{self._RED}Error mesage is not as expected{self._RESET}"
        print(f"{self._GREEN}Error mesage is as expected{self._RESET}")

        print(f"{self._GREEN}Test passed successfully{self._RESET}!")
        print("-" * 40)

    def test_invalid_password(self):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.username_field_xpath))
        )
        username_field.send_keys(self.valid_username)
        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, self.password_field_xpath)
        password_field.send_keys(self.invalid_password)
        time.sleep(2)
        submit_button = self.driver.find_element(By.XPATH, super().submit_login_button_xpath)
        submit_button.click()
        time.sleep(1)

        error_masage = self.driver.find_element(By.ID, "error")
        assert error_masage.is_displayed(), f"{self._RED}Error mesage is not display{self._RESET}"
        print(f"{self._GREEN}Error mesage is display{self._RESET}")

        assert error_masage.text == self.password_invalid_expected_message, f"{self._RED}Error mesage is not as expected{self._RESET}"
        print(f"{self._GREEN}Error mesage is as expected{self._RESET}")

        print(f"{self._GREEN}Test passed successfully{self._RESET}!")
        print("-" * 40)

    def tearDown(self):
        self.driver.quit()
