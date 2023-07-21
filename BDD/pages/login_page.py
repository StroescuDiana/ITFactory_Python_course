import time

from selenium.webdriver.common.by import By

from utils.webdriver import WebDriver


class LoginPage(WebDriver):

    def load(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

    def set_username(self, username):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='password'][@name='password']").send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn'][@id='submit']").click()
        self.driver.implicitly_wait(3)

    def get_title(self):
        print(str(self.driver.title).lower())
        return self.driver.title