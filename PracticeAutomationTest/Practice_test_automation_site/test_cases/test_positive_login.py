import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Practice_test_automation_site.page_objects.LoginPageObjects import LoginPageObjects


class TestPositiveLogin(unittest.TestCase, LoginPageObjects):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10)
        self.driver.get(super().log_in_page_url)

        self.wait = WebDriverWait(self.driver, 10)

    def test_positive_login(self):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, super().username_field_xpath))

        )
        username_field.send_keys(super().valid_username)
        time.sleep(2)

        password_field = self.driver.find_element(By.XPATH, super().password_field_xpath)
        password_field.send_keys(super().valid_password)
        time.sleep(1)

        submit_button = self.driver.find_element(By.XPATH, super().submit_login_button_xpath)
        submit_button.click()
        time.sleep(2)

        assert super().successfully_logged_in_url == self.driver.current_url, f"{self._RED}URL verification failed{self._RESET}."
        print(f"{self._GREEN}URL verification passed successfully{self._RESET}.")

        header = self.driver.find_element(By.XPATH,super().logged_in_successfully_xpath)
        assert super().successfully_logged_in_text == header.text, f"{self._RED} Expected text not found in page{self._RESET}."
        print(f"{self._GREEN}Expected text found on the page{self._RESET}")

        logout_button = self.driver.find_element(By.LINK_TEXT, super().log_out_button_link)
        assert logout_button.is_displayed(), f"{self._RED}'Log out' button not displayed {self._RESET}."
        print(f"{self._GREEN} 'Log out' button is successfuly displayed{self._RESET}.")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()