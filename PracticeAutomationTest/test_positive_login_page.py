import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

PATH = r"C:\Program Files (x86):\chromedriver"
RED = '\033[91m'
RED1 = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_successful_login(self):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))  #explicit wait
        )
        username_field.send_keys("student")

        password_field = self.driver.find_element(By.ID, "password")
        # varianta alternativa
        # password_field = driver.find_element(By.CSS_SELECTOR, "#password")

        password_field.send_keys("Password123")

        submit_button = self.driver.find_element(By.XPATH, "//*[@id='submit']")
        submit_button.click()

        time.sleep(2)

        expected_result = "https://practicetestautomation.com/logged-in-successfully/"
        actual_result = self.driver.current_url
        assert expected_result == actual_result, f"{RED}URL verification failed{RESET}."
        print(f"{GREEN}URL verification passed successfully{RESET}.")

        expected_text = ["Congratulations", "successfully logged in"]
        text_present = any(text in self.driver.page_source for text in expected_text)
        assert text_present, f"{RED}Expected text not found in the page{RESET}"
        print(f"{GREEN}Expected text found in the page{RESET}")

        logout_button = self.driver.find_element(By.CLASS_NAME, "wp-block-button__link")
        assert logout_button.is_displayed(), f"{RED}'Log out' button not displayed{RESET}."
        print(f"{GREEN}'Log out' button is successfully displayed{RESET}.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
