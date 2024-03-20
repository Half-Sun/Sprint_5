Project Description:
This project contains test scripts that verify the functionality of the registration and tab navigation on the Stellar Burgers website.

Files:
conftest.py Helper functions for generating test data, filling out the registration form, checking successful registration, and checking errors. Fixtures for setting up the driver.
Locators.py : This file contains a class named TestLocators that defines all the locators used for interacting with various elements on the Stellar Burgers website during testing. 

tests: Folder contains all collections of test.
test_clickthrough_pages.py: This file contains a collection of test cases that verify the user's ability to navigate through various sections of the Stellar Burgers website after successful registration and login.
test_login.py: This file houses test cases that verify the successful login functionality from various entry points on the Stellar Burgers website.
test_registration.py: This file encompasses test cases that specifically validate the registration process on the Stellar Burgers website.

Additional Information:
This project is written in Python using the pytest framework.
The tests use Selenium WebDriver to interact with the website.