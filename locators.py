from selenium.webdriver.common.by import By


class TestLocators:
    AUTHORIZATION_FORM_NAME = By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default[name='name']"
    AUTHORIZATION_FORM_EMAIL = By.XPATH, "//form//fieldset[2]//input"
    AUTHORIZATION_FORM_PASSWORD = By.CSS_SELECTOR, \
        'input.text.input__textfield.text_type_main-default[type="password"][name="Пароль"]'
    AUTHORIZATION_FORM_REGISTER_BUTTON = By.XPATH, '//form//button'
    REGISTRATION_LINK = By.CSS_SELECTOR, "a.Auth_link__1fOlj"
    AUTHORIZATION_FORM_REGISTER_PASSWORD_ERROR = By.CSS_SELECTOR, "p.input__error.text_type_main-default"
    ENTER_ACCOUNT_BUTTON = By.CSS_SELECTOR, \
                        "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg"
    LOG_IN_FORM_EMAIL = By.XPATH, "//form/fieldset[1]/div/div/input"
    LOG_IN_FORM_PASSWORD = By.CSS_SELECTOR, "input[name='Пароль']"
    LOG_IN_FORM_ENTER_BUTTON = By.CSS_SELECTOR, \
                        "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa"
    GO_TO_CHECKOUT_BUTTON = By.CSS_SELECTOR, \
                                 ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg"
    MY_ACCOUNT_BUTTON = By.XPATH, "//header/nav/a/p"
    AUTHORIZATION_FORM_ALREADY_REGISTERED_LINK = By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/login']"
    RESTORE_PASSWORD_ENTER_LINK = By.XPATH, '//a[@class="Auth_link__1fOlj"]'
    PROFILE_LINK = By.LINK_TEXT, "Личный Кабинет"
    CONSTRUCTOR_BUTTON = By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2"
    DESIGN_BURGER_TEXT = By.CSS_SELECTOR, "h1.text.text_type_main-large.mb-5.mt-10"
    STELLAR_BURGERS_LOGO = By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2"
    EXIT_BUTTON_IN_MY_PROFILE = By.XPATH, '//button[text()="Выход"]'
    CONSTRUCTOR_SAUCE_TAB = By.CSS_SELECTOR, ".tab_tab__1SPyG.pt-4.pr-10.pb-4.pl-10.noselect:nth-child(2)"
    CONSTRUCTOR_FILLINGS_TAB = By.CSS_SELECTOR, ".tab_tab__1SPyG.pt-4.pr-10.pb-4.pl-10.noselect:nth-child(3)"
    CONSTRUCTOR_BUN_TAB = By.CSS_SELECTOR, ".tab_tab__1SPyG.pt-4.pr-10.pb-4.pl-10.noselect:nth-child(1)"







