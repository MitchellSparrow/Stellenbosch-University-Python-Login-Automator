import webbrowser
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains


class InternetAutomator:

    def openInternet(self):
        webbrowser.open('https://inetkey.sun.ac.za/', new=1)

    def openSunlearn(self):
        webbrowser.open(
            'https://sso-prod.sun.ac.za/cas/login?service=http%3A%2F%2Flearn.sun.ac.za%2Flogin%2Findex.php', new=1)

    def openInternetWebdriver(self):
        username = "username"  # Enter your username here
        password = "password"  # Enter your password here

        browser.get('https://inetkey.sun.ac.za/')
        browser.find_elements_by_xpath(
            "/html/body/div/center/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/input")[0].send_keys(username)
        browser.find_elements_by_xpath(
            "//input[@name='password']")[0].send_keys(password)
        browser.find_elements_by_xpath(
            "/html/body/div/center/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/input")[0].click()

    def openSunlearnWebdriver(self):
        username = "username"  # Enter your username here
        password = "password"  # Enter your password here

        browser.get(
            'https://sso-prod.sun.ac.za/cas/login?service=http%3A%2F%2Flearn.sun.ac.za%2Flogin%2Findex.php')
        browser.find_elements_by_xpath(
            "//*[@id='username']")[0].send_keys(username)
        browser.find_elements_by_xpath(
            "//input[@name='password']")[0].send_keys(password)
        browser.find_elements_by_xpath(
            "//*[@id='submit-container']/div/input[4]")[0].click()


if __name__ == "__main__":

    internet = InternetAutomator()
    command1 = str(sys.argv[1])

    if command1 == "ilearn":
        internet.openInternet()
        internet.openSunlearn()
    if command1 == "learn":
        internet.openSunlearn()
    if command1 == "il":
        browser = webdriver.Chrome()
        browser.maximize_window()
        internet.openInternetWebdriver()
        internet.openSunlearnWebdriver()
    if command1 == "l":
        browser = webdriver.Chrome()
        browser.maximize_window()
        internet.openSunlearnWebdriver()
    if command1 == "i":
        browser = webdriver.Chrome()
        internet.openInternetWebdriver()
        browser.minimize_window()
