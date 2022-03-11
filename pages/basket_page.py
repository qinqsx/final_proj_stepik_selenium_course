from .base_page import BasePage
from .locators import BasketPageLocators

"""Методы для тестов basket_page с assert для упрощения отслеживания ошибок"""

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.QUANTITY_BASKET_LINK), "Basket is not empty"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE_LINK), "No text about empty basket"