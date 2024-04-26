from .base_page import BasePage
from locators.main_locators import MainPageLocators


class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = MainPageLocators()

    def login(self, credentials):
        self.click(self.locators.LOGIN_BTN_LOCATOR)
