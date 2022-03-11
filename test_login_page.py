from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators

"""Тесты сраницы логина"""

def test_guest_can_find_login_register_form(browser):
    link = LoginPageLocators.LINK
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()