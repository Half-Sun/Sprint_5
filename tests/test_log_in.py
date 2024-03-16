from Locators import TestLocators
from conftest import driver, perform_login, setup_and_register


def test_successful_log_in_from_main_page(driver):
    """
    Registers a user, navigates to main page, logs in, and verifies success.
    """
    driver, _, email, password = setup_and_register(driver)
    perform_login(driver, email, password)


def test_successful_log_in_from_my_account(driver):
    """
    Registers a user, navigates to main page, clicks on 'Личный кабинет', logs in, and verifies success.
    """
    driver, _, email, password = setup_and_register(driver)
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
    perform_login(driver, email, password)


def test_successful_log_in_via_button_in_registration_form(driver):
    """
    Registers a user, clicks on 'Уже зарегистрированы?' link, logs in, and verifies success.
    """
    driver, _, email, password = setup_and_register(driver)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*TestLocators.AUTHORIZATION_FORM_ALREADY_REGISTERED_LINK).click()
    perform_login(driver, email, password)



def test_successful_log_in_via_button_in_restore_password(driver):
    driver, _, email, password = setup_and_register(driver)
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*TestLocators.RESTORE_PASSWORD_ENTER_LINK).click()
    perform_login(driver, email, password)


