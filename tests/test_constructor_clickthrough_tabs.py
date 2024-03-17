from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import perform_registration_and_login
from conftest import driver


class TestBurgerConstructorNavigation:
    def test_successful_clickthrough_constructor_from_bun_to_sauce(self, driver):
        driver, _, _, _ = perform_registration_and_login(driver)

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        sauces_tab = driver.find_element(*TestLocators.CONSTRUCTOR_SAUCE_TAB)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_SAUCE_TAB)).click()

        driver.implicitly_wait(20)
        assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class")

    def test_successful_clickthrough_constructor_from_sauce_to_fillings(self, driver):
        driver, _, _, _ = perform_registration_and_login(driver)

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        fillings_tab = driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS_TAB)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_FILLINGS_TAB)).click()

        driver.implicitly_wait(20)
        assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class")

    def test_successful_clickthrough_constructor_from_fillings_to_bun(self, driver):
        driver, _, _, _ = perform_registration_and_login(driver)

        driver.find_element(*TestLocators.PROFILE_LINK).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_FILLINGS_TAB)).click()

        bun_tab = driver.find_element(*TestLocators.CONSTRUCTOR_BUN_TAB)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUN_TAB)).click()

        driver.implicitly_wait(20)
        assert "tab_tab_type_current__2BEPc" in bun_tab.get_attribute("class")
