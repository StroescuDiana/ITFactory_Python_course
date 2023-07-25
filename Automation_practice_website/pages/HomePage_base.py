import time

from utils.webdriver import WebDriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC


class HomePage(WebDriver):

    def load_homepage(self):
        super().driver.get('http://automationexercise.com')
        time.sleep(2)

    def home_page_is_visible(self):
        is_home_page_visible = super().driver.execute_script("return document.readyState === 'complete';")
        assert is_home_page_visible, "The page is not visible or still loading."

    def scroll_to_footer(self):
        super().driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.END)
        time.sleep(2)

    def verify_text(self):
        expected_text = "SUBSCRIPTION"
        actual_text = super().driver.find_element(By.XPATH, "//div[@class='single-widget']//h2[contains(text(), 'Subscription')]").text
        assert expected_text == actual_text, f"Actual text {actual_text} is different from {expected_text}"

    def subscribe(self, email):
        super().driver.find_element(By.ID, "susbscribe_email").send_keys(email)
        time.sleep(1)
        super().driver.find_element(By.ID, "subscribe").click()

    def verify_success_message(self):
        success_message = super().wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'You have been successfully subscribed!')]"))
            )
        assert success_message.is_displayed(), "Success message is not visible"
        time.sleep(1)
