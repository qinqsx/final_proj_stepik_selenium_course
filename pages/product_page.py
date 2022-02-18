from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math



class ProductPage(BasePage):

    def add_product_in_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON_LINK)
        add_button.click()


    def should_be_product_basket_page(self):
        self.should_be_product_url()
        self.should_be_button_add()
        self.should_be_eq_added_massage_and_product_name()
        self.should_be_eq_price_basket_and_product()



    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "'catalogue' is not  present in current url"
    def should_be_button_add(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_BUTTON_LINK), "Add button is not present"
    def should_be_eq_added_massage_and_product_name(self):
        assert self.element_text(*ProductPageLocators.PRODUCT_NAME_LINK) == self.element_text(*ProductPageLocators.PRODUCT_NAME_ADDED_IN_BASKET_LINK), "Product and basket product names does not equil"
    def should_be_eq_price_basket_and_product(self):
        assert self.element_text(*ProductPageLocators.PRODUCT_PRICE_LINK) == self.element_text(*ProductPageLocators.TOTAL_BASKET_PRICE_LINK), "Product price and basket total price does not equil"
    def should_not_be_success_message_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MASSAGE_LINK), "Success message is avalible"
    def should_not_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MASSAGE_LINK), "Success message is not disappeared"

