from .base_page import BasePage
from .overview_page import OverviewPage
from  ui.locators.main_locators import MainPageLocators
class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = MainPageLocators()

    def login(self, credentials):
        self.click(self.locators.LOGIN_BTN_LOCATOR)
        self.click(self.locators.MAIL_RU_BTN_LOCATOR)

        login, password = credentials
        self.fill(self.locators.USERNAME_INPUT_LOCATOR, login)
        self.click(self.locators.NEXT_BTN_LOCATOR)
        self.fill(self.locators.PASSWORD_INPUT_LOCATOR, password)
        self.click(self.locators.SUBMIT_BTN_LOCATOR)

        return OverviewPage(self.driver)
