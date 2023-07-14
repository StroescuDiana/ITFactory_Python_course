
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = WebDriver.Chrome()
# driver.maximize_window()


class Base:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def wait(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.presence_of_element_located(locator))

    def accept_cookies(self, locator: tuple):
        self.find(locator).click()

    def search_item(self, locator: tuple, message: str):
        return self.find(locator).send_keys(message)

    def click(self, locator):
        self.find(locator).click()


    def page_title(self):
        page_title = self.driver.title
        return page_title

