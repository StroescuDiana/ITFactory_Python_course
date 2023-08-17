from selenium.webdriver.common.by import By


class LoginPageObjects:
    username_locator = (By.XPATH, "//input[@id='username']")
    password_locator = (By.XPATH, "//input[@id='password'][@name='password']")
    submit_login_button_locator = (By.XPATH, "//button[@class='btn'][@id='submit']")

    log_in_page_url = "https://practicetestautomation.com/practice-test-login/"
    error_message = (By.ID, "error")

    username_invalid_expected_message = "Your username is invalid!"
    password_invalid_expected_message = "Your password is invalid!"

    valid_username = "student"
    valid_password = "Password123"
    invalid_username = "studenta"
    invalid_password = "password123"