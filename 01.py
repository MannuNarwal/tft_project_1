from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from csv import reader
from xfile import *


def getUrlDriver(url):
    options = webdriver.ChromeOptions()
    # options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver
  

# Clicking archives and show button
def click_button(driver, by, xpath):
    try:
        button = driver.find_element(by, xpath)
        button.click()
        sleep(1)
    except Exception as e:
        print(f"An error occurred while clicking one click button: {e}")

# Selecting gold, all and session2 button
def dropdown_button(driver,by, xpath1, xpath2):
    try:
        button = driver.find_element(by, xpath1)
        button.click()
        sleep(1)
        button = driver.find_element(by, xpath2)
        button.click()
        sleep(1)
    except Exception as e:
        print(f"An error occurred while clicking dropdown button: {e}")

# Selecting date button
def select_date(driver,by,x1, x2, x3, x4):
    try:
        button = driver.find_element(by, x1)
        button.click()
        sleep(1)
        button = driver.find_element(by, x2)
        button.click()
        sleep(1)
        button = driver.find_element(by,x3)
        button.click()
        sleep(1)
        button = driver.find_element(by,x4)
        button.click()
        sleep(1)
    except Exception as e:
        print(f"An error occurred while clicking date button: {e}")
        
driver = getUrlDriver(main_url)
click_button(driver, By.CLASS_NAME, archive_button) #clicking recent button

dropdown_button(driver, By.XPATH, gold_dropdown_xpath1,select_gold_xpath2)#clicking gold button

dropdown_button(driver, By.XPATH, all_dropdown_xpath1,select_all_xpath2)#clicking all button

dropdown_button(driver, By.XPATH, session_dropdown_xpath1,selecting_session2_xpath2)#clicking session 2 button

select_date(driver,By.XPATH, FROM_x1, FROM_year_x2, FROM_month_x3, FROM_date_x4)#clicking date FROM

select_date(driver,By.XPATH,TO_x1,TO_year_x2,TO_year_x2,TO_date_x4 )#clicking date TO

click_button(driver, By.XPATH,show_button)#clicking show button