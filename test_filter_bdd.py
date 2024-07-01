from xfile import *
from helper_func import *
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load all scenarios from the feature file
scenarios("url_filter.feature")

@pytest.fixture()
def all_variable_needed():
  return {
    "driver" : "",
    "opened_url" : ""
  }


# Scenario: Testing if correct URL is opened

@given("URL of website is opened by driver")
def open_website(all_variable_needed):
  driver = getUrlDriver(main_url)
  all_variable_needed["driver"] = driver
  
@when("URL is initiated by driver") 
def getting_url_from_driver(all_variable_needed):
  opened_url = all_variable_needed["driver"].current_url
  all_variable_needed["opened_url"]=opened_url 
  
@then("correct URL should be opened")  
def url_verified(all_variable_needed):
  assert all_variable_needed["opened_url"] == main_url, "FAILED - URL opened is NOT correct URL.!!"



#Scenario: Testing if only archive is clicked
    
@when("Archive button is clicked")
def archive_clicked(all_variable_needed):
  click_button(all_variable_needed["driver"], By.CLASS_NAME, archive_button)
  
@when("show button is clicked")
def show_clicked(all_variable_needed):
  click_button(all_variable_needed["driver"],By.XPATH,show_button)
    
@then("ERROR is occured Please select a commodity")
def commodity_error(all_variable_needed):
  data = getElementData(all_variable_needed["driver"], By.CLASS_NAME, err_class)
  assert_verfication(data,NO_SELECTED,"FAILED - Wrong error message")
  
  
  
#Scenario: Testing if only FROM calender is selected
  
@when("Gold from commodity is selected")
def gold_clicked(all_variable_needed):
 dropdown_button(all_variable_needed["driver"], By.XPATH, gold_dropdown_xpath1,select_gold_xpath2)
 
@when("Year, Month, date is selected from only calender") 
def set_calender(all_variable_needed):
  select_date(all_variable_needed["driver"],By.XPATH,FROM_x1,FROM_year_x2,FROM_month_x3,FROM_date_x4)
     
@then("ERROR is occured Please select From Date")
def to_error(all_variable_needed):
  data = getElementData(all_variable_needed["driver"], By.CLASS_NAME, err_class)
  assert_verfication(data,ONLY_DATE_SELECTED,"FAILED - Wrong error message")



# Scenario: Testing for date TO less than FROM

@when("Year, Month, date is set FROM calender")
def set_from_calender(all_variable_needed):
  select_date(all_variable_needed["driver"],By.XPATH,FROM_x1,TO_year_x2,TO_month_x3,TO_date_x4)

@when("Year, Month, date is set TO calender")
def set_to_calender(all_variable_needed):
  select_date(all_variable_needed["driver"],By.XPATH,TO_x1,FROM_year_x2,FROM_month_x3,FROM_date_x4)
   
@then("ERROR is occured From Date should not be greater than To Date")      
def date_error(all_variable_needed):
  data = getElementData(all_variable_needed["driver"], By.CLASS_NAME, err_class)
  assert_verfication(data,DIFFERENT_DATE,"FAILED - Wrong error message")
  
# Scenario: Testing for all filled filter parameter
  
@when("Year, Month, date TO calender")
def to_calender(all_variable_needed):
  select_date(all_variable_needed["driver"],By.XPATH,TO_x1,TO_year_x2,TO_month_x3,TO_date_x4)
  
@then("Tabulated data should show")
def show_data(all_variable_needed):
  data = getElementData(all_variable_needed["driver"], By.CLASS_NAME,err_class )
  assert_verfication(data,'',f"FAILED - Error message is coming - '{data}' , not able to show table.")
  