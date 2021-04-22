import pytest 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep



def test_app():
    chrome_driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    chrome_driver.get('http://127.0.0.1:5000/')
    chrome_driver.maximize_window()
 
    chrome_driver.find_element_by_name("title").send_keys("first test")
    chrome_driver.find_element_by_xpath("//form[@class='ui form']/button[1]").click()
    chrome_driver.find_element_by_name("title").send_keys("second test")
    chrome_driver.find_element_by_xpath("//form[@class='ui form']/button[1]").click()

    num_elements = 2
    sleep(3)
    # arr = chrome_driver.find_elements_by_class_name("ui segment")
    arr = chrome_driver.find_elements_by_xpath("//div[@class='ui segment']")
    assert len(arr) == num_elements
    chrome_driver.close()
