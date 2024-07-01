Feature: Testing website filter 
    Tests related to filter functionality

    Scenario: Testing if correct URL is opened
        Given URL of website is opened by driver
        When URL is initiated by driver
        Then correct URL should be opened


    Scenario: Testing if only archive is clicked 
        Given URL of website is opened by driver 
        When Archive button is clicked 
        When show button is clicked 
        Then ERROR is occured Please select a commodity


    Scenario: Testing if only FROM calender is selected
        Given URL of website is opened by driver
        When  Archive button is clicked
        When  Gold from commodity is selected
        When Year, Month, date is selected from only calender
        When show button is clicked
        Then ERROR is occured Please select From Date


    Scenario: Testing for date TO less than FROM
        Given URL of website is opened by driver
        When  Archive button is clicked
        When  Gold from commodity is selected
        When Year, Month, date is set FROM calender
        When Year, Month, date is set TO calender
        When show button is clicked
        Then ERROR is occured From Date should not be greater than To Date


    Scenario: Testing for all filled filter parameter
        Given URL of website is opened by driver
        When  Archive button is clicked
        When  Gold from commodity is selected
        When Year, Month, date is selected from only calender
        When Year, Month, date TO calender
        When show button is clicked
        Then Tabulated data should show
    
    




