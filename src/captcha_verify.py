from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def _get_login_cookies(useragent):
    cookies = ""
    context = {
        "nation": "Celinova",
        "password": "XBsgjXz3",
        "autologin": "yes",
        "submit": "Login",
    }
    headers = {"User-Agent": "Hellfire development test by Celinova, Used by Celinova"}
    driver = Firefox()
    response = webdriver.request(
        "POST", "https://www.nationstates.net/page=login", data=context, headers=headers
    )

    return cookies
