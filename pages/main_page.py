from .base_page import BasePage

"""Заглушка т.к. в тесте main_page используются методы из base_page"""

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)