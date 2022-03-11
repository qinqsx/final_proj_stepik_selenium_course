from selenium.webdriver.common.by import By

"""Классы с локаторами для страниц и ссылки на них, для улучшения читаемости кода, так же в случае изменения селектора или ссылки на тот или иной объект упрощает корректировку"""

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini  a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_LINK1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_LINK2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_LINK = (By.CSS_SELECTOR, "[name='registration_submit']")
    LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

class ProductPageLocators():
    LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    LINK2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    LINK3 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    LINK4 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    LINK_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    PRODUCT_ADD_BUTTON_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_LINK = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, ".product_main h1")
    TOTAL_BASKET_PRICE_LINK = (By.CSS_SELECTOR, "#messages>:nth-child(3) strong")
    PRODUCT_NAME_ADDED_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    SUCCESS_MASSAGE_LINK = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, "#content_inner>p")
    QUANTITY_BASKET_LINK = (By.CSS_SELECTOR, "[name='form-0-quantity']")




