
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Elefant_ro_site.main.web_elements import WebElements
from Elefant_ro_site.main.base import Base

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

        search_button_locator = (By.XPATH, super().search_button_xpath)
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
        actual_title = self.page_title()

        try:
            assert actual_title == super().expected_title, f"Titlul paginii curente: {actual_title} este diferit de cel asteptat: {super().expected_title}"
            print(f"{super().GREEN}Titlul curent corespunde cu titlul asteptat{super().RESET}.")

        except AssertionError as error:
            print(super().RED, error, super().RESET)

class Negative_log_in(WebElements, Base):

    def __init__(self, driver):
        super().__init__(driver)

    def negative(self):
        cont_icon_locator = (By.XPATH, super().cont_icon_xpath)
        self.find(cont_icon_locator).click()

        conectare_bttn_locator = (By.XPATH, super().conectare_bttn_homepage_xpath)
        self.find(conectare_bttn_locator).click()

        try:
            current_url = self.page_url()
            assert current_url == super().log_in_url, f"Nu te afli pe pagina de conectare."

        except AssertionError as error:
            print(super().RED, error, super().RESET)
        else:
            email_field_locator = (By.XPATH, super().email_field_xpath)
            self.find(email_field_locator).send_keys(super().wrong_email_address)
            password_field_locator = (By.XPATH, super().password_box_xpath)
            self.find(password_field_locator).send_keys(super().wrong_password)
            conectare_locator = (By.XPATH, super().conectare_button_login_xpath)
            self.find(conectare_locator).click()

            error_alert_locator = (By.XPATH, super().error_alert_text_xpath)
            actual_error = self.find(error_alert_locator).text
            if actual_error == super().expected_error:
                print(actual_error)
            else:
                print(f"{super().RED}Error message is incorrect{super().RESET}.")

            actual_url = self.page_url()
            expected_url = super().log_in_successful_url
            if not actual_url == expected_url:
                print("Nu s-a putut realiza conectarea in cont.")


    def invalid_email_login(self):

        email_field_locator = (By.XPATH, super().email_field_xpath)
        self.find(email_field_locator).send_keys(Keys.CONTROL + "a")
        self.find(email_field_locator).send_keys(Keys.BACKSPACE)
        self.find(email_field_locator).send_keys(super().invalid_email_address)
        conectare_locator = (By.XPATH, super().conectare_button_login_xpath)
        conectare_button_status = self.find(conectare_locator).is_displayed()
        print(f"Este butonul de conectare dezactivat? {conectare_button_status}")