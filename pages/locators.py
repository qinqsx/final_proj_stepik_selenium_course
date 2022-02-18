from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_ADD_BUTTON_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_LINK = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, ".product_main h1")
    TOTAL_BASKET_PRICE_LINK = (By.CSS_SELECTOR, "#messages>:nth-child(3) strong")
    PRODUCT_NAME_ADDED_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages>:nth-child(1) strong")
    SUCCESS_MASSAGE_LINK = (By.CSS_SELECTOR, ".alert-success")

