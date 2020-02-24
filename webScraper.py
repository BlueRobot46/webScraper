# The first step of the code is to open the web browser.
# So to do that we will import selenium and the webdriver module

import sys
from selenium import webdriver
import time

# Calls on webdriver module to open chrome.
driver = webdriver.Chrome('C:\webDrivers/chromedriver.exe')

driver.get("https://www.nike.com/launch")

time.sleep(3);
button = driver.find_element_by_css_selector('#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > ul > li.member-nav-item.d-sm-ib.va-sm-m > button')
clickButton = button.click();