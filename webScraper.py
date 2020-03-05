# The first step of the code is to open the web browser.
# So to do that we will import selenium and the webdriver module

import sys
from selenium import webdriver
import time

#User info question
while True:
    try:
        userNum = int(input("How many users would you like to add?"))
        break
    except ValueError:
        print("Please input a number instead.")

print("Adding " + str(userNum) + " user accounts.")

# Create dictionary for user input
account = []

accountValue = []

user = {}

#Logic to check for if there are more than one user account being added.
numUser = False

if userNum >= 2:
    numUser = True

#Collects user information and stores that into a list.
while len(accountValue) < userNum:
    userAcc = str(input("Username:"))
    account.append(userAcc)
    userPass = str(input("Password:"))
    accountValue.append(userPass)
    print(numUser)
    print(account)
    print(accountValue)

# Calls on webdriver module to open chrome.
driver = webdriver.Chrome('C:\webDrivers/chromedriver.exe')

driver.get("https://www.nike.com/launch")

time.sleep(3);
button = driver.find_element_by_css_selector('#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > ul > li.member-nav-item.d-sm-ib.va-sm-m > button')
clickButton = button.click();