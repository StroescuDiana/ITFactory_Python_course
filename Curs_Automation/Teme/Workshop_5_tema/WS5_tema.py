import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.elefant.ro/")

# # Delete all cookies
# driver.delete_all_cookies()
time.sleep(5)
wait = WebDriverWait(driver, 10)
cookies_bttn = wait.until(
    EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)

cookies_bttn.click()
time.sleep(3)