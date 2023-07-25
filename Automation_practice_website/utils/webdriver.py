from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait


class WebDriver:

    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    def quit(self):
        self.driver.quit()