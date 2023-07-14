
import time
from selenium.webdriver.common.by import By

from Teme.Workshop_5_tema.web_elements import WebElements
from Teme.Workshop_5_tema.base import Base

class OpenPage(WebElements, Base):

    def open_page(self):
        super().open(super().url)
        time.sleep(5)
        cookies_accept_button_locator = (By.ID, super().cookies_accept_bttn_id)
        super().accept_cookies(cookies_accept_button_locator)
        time.sleep(3)

