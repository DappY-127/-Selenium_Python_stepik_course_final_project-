from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')   
    CONFIRMATION_FIELD = (By.CSS_SELECTOR, '#messages > div.alert-success:nth-child(1)')  # uses in should_be_confirmation_add_to_cart_message  
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRICE_IN_CONFIRMATION_FIELD = (By.CSS_SELECTOR, '.alertinner p strong')
    NAME_IN_CONFIRMATION_FIELD = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert-success:nth-child(1) div.alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
 