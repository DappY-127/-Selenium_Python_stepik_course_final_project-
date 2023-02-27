from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    # REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    # REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    # REGISTRATION_PASSWORD_CONFIRMATION_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    # LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    # LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
       