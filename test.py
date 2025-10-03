from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
nation_name = "Celinova"
password = "XBsgjXz3"

# go to login page
driver.get(
    "https://www.nationstates.net/page=login/?generated_by=Hellfire_dev_script__by_Celinova__usedBy_Celinova"
)

try:
    # check if it exists first, wait until user resolves captcha
    random = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button icon primary"))
    )

    input()

    # locate field elements and fill them in
    username_element = driver.find_element(By.NAME, "nation")
    username_element.send_keys(f"{nation_name}")

    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys(f"{password}")

    driver.find_element(By.NAME, "autologin").click()


    # submit form after 6 seconds
    time.sleep("7")
    driver.find_element(By.CLASS_NAME, "button icon primary").click()
    input()
finally:
    input()
