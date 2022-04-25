import pytest
import time
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators


"""Тесты для product_page с маркерами, о них подробнее в pytest.ini"""

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)    #фикстура устанавливается на каждую последующую функцию в данном классе
    def setup(self, browser):                          #создаем аккаунт
        email = str(time.time()) + "@fakemail.org"
        password = "Qq391609404"
        link = ProductPageLocators.LINK3
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.LINK3
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.LINK3
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_in_basket()
        product_page.should_be_product_basket_page()


@pytest.mark.parametrize("urls", [*[num for num in range(10) if num != 7],
                                  pytest.param(7, marks=pytest.mark.xfail)])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, urls):
    # при помощи параметризации узнаем какой тест падает и затем помечаем его как заведомо падающий xfail
    link = f"{ProductPageLocators.LINK_PROMO}{urls}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_basket_page()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.LINK3
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message_present()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.LINK3
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_not_be_success_message_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.LINK3
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_not_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.LINK4
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.LINK4
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.LINK4
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
    basket_page.should_be_text_about_empty_basket()


