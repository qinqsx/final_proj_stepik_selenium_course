from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not  present in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Register form is not present"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.send_text(*LoginPageLocators.INPUT_EMAIL_LINK, email)
        self.send_text(*LoginPageLocators.INPUT_PASSWORD_LINK1, password)
        self.send_text(*LoginPageLocators.INPUT_PASSWORD_LINK2, password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_LINK).click()
