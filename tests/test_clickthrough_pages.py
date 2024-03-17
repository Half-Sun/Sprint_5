from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import (
    assert_element_text, perform_registration_and_login,
    setup_and_register)
from conftest import driver

class TestMyAccountNavigation(object):

    def test_successful_clickthrough_from_registration_to_profile(self, driver):
        driver, _, _, _ = perform_registration_and_login(driver)  # Register and login

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK)).click()
        driver.find_element(*TestLocators.PROFILE_LINK).click()
        driver.find_element(*TestLocators.PROFILE_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EXIT_BUTTON_IN_MY_PROFILE))

        assert_element_text(driver, TestLocators.EXIT_BUTTON_IN_MY_PROFILE, "Выход")

    def test_successful_clickthrough_from_profile_to_constructor(self, driver):
        driver, _, _, _ = setup_and_register(driver)  # Register and login

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(TestLocators.PROFILE_LINK)).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        assert_element_text(driver, TestLocators.DESIGN_BURGER_TEXT, "Соберите бургер")

    def test_successful_clickthrough_from_profile_to_stellar_burger_logo(self, driver):
        driver, _, _, _ = setup_and_register(driver)  # Register and login

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()

        assert_element_text(driver, TestLocators.DESIGN_BURGER_TEXT, "Соберите бургер")

    def test_successful_clickthrough_from_profile_to_logout(self, driver):
        driver, _, _, _ = perform_registration_and_login(driver)  # Register and login

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(TestLocators.PROFILE_LINK)).click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(TestLocators.EXIT_BUTTON_IN_MY_PROFILE)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.RESTORE_PASSWORD_ENTER_LINK))

        assert_element_text(driver, TestLocators.RESTORE_PASSWORD_ENTER_LINK, "Зарегистрироваться")
