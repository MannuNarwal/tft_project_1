from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from xfile import * 


def getUrlDriver(url):
    options = webdriver.ChromeOptions()
    # options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    # options.add_experimental_option("detach", True)
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
        
def getElementData(driver, by, xpath):
    el = driver.find_element(by, xpath)
    return el.text


def get_table_data(driver):
    table_data = []
    try:
        table = driver.find_element(By.ID, 'tblArchive')
            # Extracting table headers
        headers = []
        for th in table.find_elements(By.XPATH, './/thead/tr/th'):
                headers.append(th.text.strip())
                
                
    except Exception as e:
        print(f"An error occurred while retrieving table data: {e}")
    
    return table_data   

def assert_verfication(actual_value, expected_value,msg):
    assert actual_value==expected_value, msg
    