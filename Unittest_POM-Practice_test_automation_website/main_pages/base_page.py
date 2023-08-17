from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)  # locator = (By.XPATH, valoare)

    def wait_for_visible_element(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.presence_of_element_located(locator), "Element not visible")

    def type(self, locator: tuple, message: str, time: int = 10):
        self.wait_for_visible_element(locator, time)
        self.find(locator).send_keys(message)

    # get text from a label
    def get_text(self, locator, time: int = 10):
        self.wait_for_visible_element(locator, time)
        return self.find(locator).text

    # click on a button
    def click(self, locator, time: int = 10):
        self.wait_for_visible_element(locator, time)
        self.find(locator).click()

    # is object displayed
    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    # get current url
    def get_current_url(self):
        return self.driver.current_url

