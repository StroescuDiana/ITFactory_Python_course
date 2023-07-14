import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_button.click()

time.sleep(2)

alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")

confirm_button.click()
time.sleep(2)
confirm_alert = driver.switch_to.alert
time.sleep(2)
confirm_alert.dismiss()

prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")

prompt_button.click()
time.sleep(2)
prompt_alert = driver.switch_to.alert
time.sleep(2)
prompt_alert.send_keys("Some text")
driver.implicitly_wait(1)
time.sleep(2)
prompt_alert.accept()
time.sleep(2)
