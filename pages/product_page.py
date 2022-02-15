from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math



class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product_in_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON_LINK)
        add_button.click()
        self.solve_quiz_and_get_code()

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

