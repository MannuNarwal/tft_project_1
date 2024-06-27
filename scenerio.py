
import pytest
from helper_func import *
from selenium.webdriver.common.by import By
from xfile import *


def test_open_website():
  driver = getUrlDriver(main_url)
  opened_url = driver.current_url
  assert opened_url == main_url, "FAILED - URL opened is NOT correct URL.!!"

def test_no_filter_selected():
  driver = getUrlDriver(main_url)
  click_button(driver, By.CLASS_NAME, archive_button)
  click_button(driver, By.XPATH,show_button)
  data = getElementData(driver, By.CLASS_NAME, err_class)
  assert_verfication(data,NO_SELECTED,"FAILED - Wrong error message")
  
  
def test_only_commodity():
  driver = getUrlDriver(main_url)
  click_button(driver, By.CLASS_NAME, archive_button)
  dropdown_button(driver, By.XPATH, gold_dropdown_xpath1,select_gold_xpath2)
  click_button(driver, By.XPATH,show_button)
  data = getElementData(driver, By.CLASS_NAME, err_class)
  assert_verfication(data,ONLY_COMMODITY_SELECTED,"FAILED - Wrong error message")
    
def test_from_date():
  driver = getUrlDriver(main_url)
  click_button(driver, By.CLASS_NAME, archive_button)
  dropdown_button(driver, By.XPATH, gold_dropdown_xpath1,select_gold_xpath2)
  select_date(driver,By.XPATH,FROM_x1,FROM_year_x2,FROM_month_x3,FROM_date_x4)
  click_button(driver, By.XPATH,show_button)
  data = getElementData(driver, By.CLASS_NAME, err_class)
  assert_verfication(data,ONLY_DATE_SELECTED,"FAILED - Wrong error message")
  
  

  
def test_different_date():
  driver = getUrlDriver(main_url)
  click_button(driver, By.CLASS_NAME, archive_button)
  dropdown_button(driver, By.XPATH, gold_dropdown_xpath1,select_gold_xpath2)
  select_date(driver,By.XPATH,FROM_x1,TO_year_x2,TO_month_x3,TO_date_x4)
  select_date(driver,By.XPATH,TO_x1,FROM_year_x2,FROM_month_x3,FROM_date_x4)
  click_button(driver, By.XPATH,show_button)
  data = getElementData(driver, By.CLASS_NAME, err_class)
  assert_verfication(data,DIFFERENT_DATE,"FAILED - Wrong error message")
 


def test_filter():
  driver = getUrlDriver(main_url)
  click_button(driver, By.CLASS_NAME, archive_button)
  dropdown_button(driver, By.XPATH, gold_dropdown_xpath1,select_gold_xpath2)
  select_date(driver,By.XPATH,FROM_x1,FROM_year_x2,FROM_month_x3,FROM_date_x4)
  select_date(driver,By.XPATH,TO_x1,TO_year_x2,TO_month_x3,TO_date_x4)
  click_button(driver, By.XPATH,show_button)
  data = getElementData(driver, By.CLASS_NAME,err_class )
  assert_verfication(data,'',f"FAILED - Error message is coming - '{data}' , not able to show table.")
  
  
