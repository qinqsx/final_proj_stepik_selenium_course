from .pages.login_page import LoginPage

def test_guest_can_find_login_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()