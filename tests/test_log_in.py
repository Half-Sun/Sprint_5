from locators import TestLocators
from helpers import perform_login, setup_and_register
from conftest import driver


class TestLoginFromDifferentPages:
    def test_successful_log_in_from_main_page(self, driver):
        driver, _, email, password = setup_and_register(driver)
        perform_login(driver, email, password)

    def test_successful_log_in_from_my_account(self, driver):
        driver, _, email, password = setup_and_register(driver)
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        perform_login(driver, email, password)

    def test_successful_log_in_via_button_in_registration_form(self, driver):
        driver, _, email, password = setup_and_register(driver)
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_ALREADY_REGISTERED_LINK).click()
        perform_login(driver, email, password)

    def test_successful_log_in_via_button_in_restore_password(self, driver):
        driver, _, email, password = setup_and_register(driver)
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.RESTORE_PASSWORD_ENTER_LINK).click()
        perform_login(driver, email, password)
