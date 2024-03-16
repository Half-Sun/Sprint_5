import random
import string
from string import ascii_letters, digits
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators import TestLocators
def generate_password(length=8):
    chars = ascii_letters + digits
    password = "".join(random.choice(chars) for _ in range(length))
    return password


def generate_email(domain="gmail.com"):
    # Список допустимых символов для имени пользователя
    username_chars = string.ascii_lowercase + string.digits + "_"
    username_length = random.randint(5, 10)
    username = "".join(random.choice(username_chars) for _ in range(username_length))
    email = f"{username}@{domain}"
    return email


def generate_name(length=8):
    chars = ascii_letters
    name = "".join(random.choice(chars) for _ in range(length))
    return name

@pytest.fixture(scope="function")
def driver():
  options = Options()
  options.add_argument('--window-size=1920,1080')
  driver = webdriver.Chrome(options=options)
  yield driver
  driver.quit()


# Helper functions for registration and loginа
def perform_registration_and_login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    email = generate_email()
    name = generate_name()
    password = generate_password(8)

    fill_registration_form(driver, name, email, password)
    click_my_account(driver)
    login_using_my_account(driver, email, password)

    return driver, name, email, password


def fill_registration_form(driver, name, email, password):
    driver.find_element(*TestLocators.AUTHORIZATION_FORM_NAME).send_keys(name)
    driver.find_element(*TestLocators.AUTHORIZATION_FORM_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.AUTHORIZATION_FORM_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.AUTHORIZATION_FORM_REGISTER_BUTTON).click()


def click_my_account(driver):
    driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()


def login_using_my_account(driver, email, password):
    driver.find_element(*TestLocators.LOG_IN_FORM_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.LOG_IN_FORM_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.LOG_IN_FORM_ENTER_BUTTON).click()


def assert_element_text(driver, locator, expected_text):
    element = driver.find_element(*locator)
    assert element.text == expected_text

def perform_login(driver, email, password):
    """
    Logs in the user and verifies successful login.
    """
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*TestLocators.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.LOG_IN_FORM_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.LOG_IN_FORM_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.LOG_IN_FORM_ENTER_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.GO_TO_CHECKOUT_BUTTON))
    button = driver.find_element(*TestLocators.GO_TO_CHECKOUT_BUTTON)

    try:
        assert button.text == "Оформить заказ", "Error: unexpected text"
        print("Successful log in. Button text as expected")
    except AssertionError as e:
        print(e)

def setup_and_register(driver):
        """
        Sets up Chrome browser, navigates to registration page, registers user.
        """
        driver.get("https://stellarburgers.nomoreparties.site/register")

        name = generate_name()
        email = generate_email()
        password = generate_password(8)

        driver.find_element(*TestLocators.AUTHORIZATION_FORM_NAME).send_keys(name)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.AUTHORIZATION_FORM_REGISTER_BUTTON).click()

        return driver, name, email, password