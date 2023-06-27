import time

from selenium import webdriver
from selene import browser
from conftest import TMP_PATH
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
def test_get_file_with_browser(file_manager):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    filename = 'pytest-main.zip'
    assert os.path.exists(TMP_PATH)

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)
    assert os.path.exists(os.path.join(TMP_PATH, filename))
