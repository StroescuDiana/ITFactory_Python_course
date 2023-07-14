
import time
from selenium.webdriver.common.by import By

from Teme.Workshop_5_tema.web_elements import WebElements
from Teme.Workshop_5_tema.base import Base

class OpenPage(WebElements, Base):

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):

        super().open(super().url)
        time.sleep(5)
        cookies_accept_button_locator = (By.ID, super().cookies_accept_bttn_id)
        super().accept_cookies(cookies_accept_button_locator)
        time.sleep(3)


class SearchItem(WebElements, Base):

    def __init__(self, driver):
        super().__init__(driver)

    def find_item(self):

        search_box_locator = (By.XPATH, super().search_box_xpath)
        super().search_item(search_box_locator, super().item)

        search_button_locator = (By.XPATH, super().search_button)
        super().click(search_button_locator)

        product_title_locator = (By.XPATH, super().product_title_xpath)
        products_number = self.find_elements(product_title_locator)
        if len(products_number) >= 10:
            print(f"{super().GREEN}Exista cel putin 10 produse pe pagina elefant.ro{super().RESET}")
        else:
            print(f"{super().RED}Exista mai putin de 10 produse pe pagina elefant.ro{super().RESET}")

    def smallest_price(self):

        product_price_locator = (By.XPATH, super().product_price_xpath)
        web_elements = super().find_elements(product_price_locator)

        prices = []
        for element in web_elements:
            price_without_currency = element.text.replace(" lei", "")
            accepted_price_format = price_without_currency.replace(",", ".")
            price = float(accepted_price_format)
            prices.append(price)

        min_price = min(prices)
        print(f"Cel mai mic pret este de {min_price} lei.")

class PageTitle(WebElements, Base):

    def __init__(self, driver):
        super().__init__(driver)

    def correct_page(self):
        current_url = self.page_title()
        try:
            assert current_url == super().expected_title, f"Titlul paginii curente este diferit de cel asteptat: {super().expected_title}"
            print(f"{super().GREEN}Titlul curent corespunde cu titlul asteptat{super().RESET}.")
        except AssertionError as error:
            print(super().RED, error, super().RESET)
