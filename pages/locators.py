from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini  a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_LINK1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_LINK2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_LINK = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    PRODUCT_ADD_BUTTON_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_LINK = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, ".product_main h1")
    TOTAL_BASKET_PRICE_LINK = (By.CSS_SELECTOR, "#messages>:nth-child(3) strong")
    PRODUCT_NAME_ADDED_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    SUCCESS_MASSAGE_LINK = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, "#content_inner>p")
    QUANTITY_BASKET_LINK = (By.CSS_SELECTOR, "[name='form-0-quantity']")




