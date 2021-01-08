from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_book_name(self):
        book_name_header = self.browser.find_element(*ProductPageLocators.BOOK_NAME_HEADER)
        return book_name_header.text

    def should_be_message_about_adding_to_basket(self):
        book_name = self.get_book_name()
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS_MESSAGES), "Alert-success messages is not presented"
        messages = self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS_MESSAGES)
        is_present = False
        for message in messages:
            if book_name == message.text:
                is_present = True
        assert is_present, "Message about adding to basket is not presented"

    def should_be_change_sum_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_LABLE), "Price lable is not presented"
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO_MESSAGE), "Alert-info messages is not presented"
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_LABLE).text
        message_price = self.browser.find_element(*ProductPageLocators.ALERT_INFO_MESSAGE).text
        assert book_price == message_price, "Message with price is not presented"

