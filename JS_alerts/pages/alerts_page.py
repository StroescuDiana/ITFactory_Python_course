from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class Alerts(Base_page):
    BUTTONALERT = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    MESSAGELOCATOR = (By.ID, 'result')
    JSCONFIRM = (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    JSPROMPT = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")

    def click_JS_alert_button(self):
        self.driver.find_element(*self.BUTTONALERT).click()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def message_alert(self):
        assert self.driver.find_element(*self.MESSAGELOCATOR).text, 'You successfully clicked an alert'

    def click_JS_Confirm_button(self):
        self.driver.find_element(*self.JSCONFIRM).click()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def message_confirm(self):
        assert self.driver.find_element(*self.MESSAGELOCATOR).text, 'You clicked: Cancel'

    def click_JS_Prompt_button(self):
        self.driver.find_element(*self.JSPROMPT).click()
    def send_text(self):
        self.driver.switch_to.alert.send_keys('This is text')

    def accept_Js_Prompt(self):
        self.driver.switch_to.alert.accept()
    def message_prompt(self):
        assert self.driver.find_element(*self.MESSAGELOCATOR).text, 'You entered: This is text'
