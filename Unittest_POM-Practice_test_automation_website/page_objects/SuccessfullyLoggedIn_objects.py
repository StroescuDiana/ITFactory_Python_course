from selenium.webdriver.common.by import By


class SuccessfullyLoggedIn_objects:
    successfully_logged_in_url = "https://practicetestautomation.com/logged-in-successfully/"
    successfully_logged_in_text = "Logged In Successfully"
    header_locator = (By.XPATH, "//h1[@class='post-title']")
    logout_button_locator = (By.LINK_TEXT, "Log out")