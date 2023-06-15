#!/usr/bin/env python3
import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://www.example.com/'


def chrome_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('-headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })
    logging.info('Prepared chrome options..')

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    logging.info('Initialized chrome browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


def firefox_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    firefox_options = firefox.options.Options()
    firefox_options.add_argument('-headless')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.binary_location = '/usr/bin/firefox'
    firefox_options.set_preference('browser.download.folderList', 2)
    firefox_options.set_preference(
        'browser.download.manager.showWhenStarting', False
    )
    firefox_options.set_preference('browser.download.dir', os.getcwd())
    firefox_options.set_preference(
        'browser.helperApps.neverAsk.saveToDisk', 'text/csv'
    )

    logging.info('Prepared firefox profile..')

    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    logging.info('Initialized firefox browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


if __name__ == '__main__':
    chrome_example()
    # firefox_example()  # runs normally in a docker container but Github Actions is having some trouble with it
