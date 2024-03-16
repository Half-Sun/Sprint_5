from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators
from conftest import driver, perform_registration_and_login, assert_element_text



def test_successful_clickthrough_from_registration_page_to_my_account_profile(driver):
    driver, _, _, _ = perform_registration_and_login(driver)
    driver.find_element(*TestLocators.PROFILE_LINK).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK)).click()
    driver.find_element(*TestLocators.PROFILE_LINK).click()
    driver.find_element(*TestLocators.PROFILE_LINK).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.EXIT_BUTTON_IN_MY_PROFILE))

    driver.implicitly_wait(20)
    assert_element_text(driver, TestLocators.EXIT_BUTTON_IN_MY_PROFILE, "Выход")


def test_successful_clickthrough_from_my_account_profile_to_constructor(driver):
    driver, _, _, _ = perform_registration_and_login(driver)
    driver.find_element(*TestLocators.PROFILE_LINK).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(TestLocators.PROFILE_LINK)).click()
    driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

    driver.implicitly_wait(20)
    assert_element_text(driver, TestLocators.DESIGN_BURGER_TEXT, "Соберите бургер")


def test_successful_clickthrough_from_my_account_profile_to_stellar_burger_logo(driver):
    driver, _, _, _ = perform_registration_and_login(driver)
    driver.find_element(*TestLocators.PROFILE_LINK).click()
    driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()

    assert_element_text(driver, TestLocators.DESIGN_BURGER_TEXT, "Соберите бургер")

def test_successful_clickthrough_from_my_account_profile_to_log_out(driver):
    driver, _, _, _ = perform_registration_and_login(driver)
    driver.find_element(*TestLocators.PROFILE_LINK).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(TestLocators.PROFILE_LINK)).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(TestLocators.EXIT_BUTTON_IN_MY_PROFILE)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.RESTORE_PASSWORD_ENTER_LINK))

    driver.implicitly_wait(20)
    assert_element_text(driver, TestLocators.RESTORE_PASSWORD_ENTER_LINK, "Зарегистрироваться")


def test_successful_clickthrough_constructor_from_bun_to_sause(driver):
    driver, _, _, _ = perform_registration_and_login(driver)

    driver.find_element(*TestLocators.PROFILE_LINK).click()
    driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

    sauces_tab = driver.find_element(*TestLocators.CONSTRUCTOR_SAUSE_TAB)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_SAUSE_TAB)).click()

    driver.implicitly_wait(20)
    assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class")


def test_successful_clickthrough_constructor_from_sause_to_fillings(driver):
    driver, _, _, _ = perform_registration_and_login(driver)

    driver.find_element(*TestLocators.PROFILE_LINK).click()
    driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

    fillings_tab = driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS_TAB)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_FILLINGS_TAB)).click()

    driver.implicitly_wait(20)
    assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class")


def test_successful_clickthrough_constructor_from_fillings_to_bun(driver):
    driver, _, _, _ = perform_registration_and_login(driver)

    driver.find_element(*TestLocators.PROFILE_LINK).click()
    driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_FILLINGS_TAB)).click()

    bun_tab = driver.find_element(*TestLocators.CONSTRUCTOR_BUN_TAB)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUN_TAB)).click()

    driver.implicitly_wait(20)
    assert "tab_tab_type_current__2BEPc" in bun_tab.get_attribute("class")


