from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_button.click()

    def should_be_confirmation_add_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.CONFIRMATION_FIELD), "'{product} has been added to your basket.' is not visible "   

    def should_be_success_message_with_product_name(self, product_name):
        success_message = self.browser.find_element(*ProductPageLocators.NAME_IN_CONFIRMATION_FIELD).text
        assert product_name == success_message, f"Success message does not contain product name '{product_name}'"

    def should_be_cart_total_with_product_price(self, product_price):
        cart_total_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_CONFIRMATION_FIELD).text
        assert product_price == cart_total_message, f"Cart total does not match product price '{product_price}'"

    def get_product_name(self):
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_element.text
    
    def get_product_price(self):
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_element.text
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is still presented, but should have disappeared"
