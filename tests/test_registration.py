from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from helpers import generate_password, generate_email, generate_name
from conftest import driver


class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        name = generate_name()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.AUTHORIZATION_FORM_NAME).send_keys(name)
        password = generate_password(8)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.REGISTRATION_LINK))
        link_register = driver.find_element(*TestLocators.REGISTRATION_LINK)

        assert link_register.is_displayed()
        print("Successful registration. Registration link is found")

    def test_registration_failed_password_is_less_then_6_symbols(self, driver):
        email = generate_email()
        name = generate_name()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.AUTHORIZATION_FORM_NAME).send_keys(name)
        password = generate_password(3)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.AUTHORIZATION_FORM_REGISTER_PASSWORD_ERROR))
        error_message = driver.find_element(*TestLocators.AUTHORIZATION_FORM_REGISTER_PASSWORD_ERROR).text

        assert error_message == "Некорректный пароль"
        print("Text 'Некорректный пароль' is found")
