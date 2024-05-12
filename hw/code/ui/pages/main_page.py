from .base_page import BasePage
from .overview_page import OverviewPage
from  ui.locators.main_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException


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

    def try_to_register(self):
        self.click(self.locators.NOT_ACTIVE_BULLET_LOCATOR)
        self.click(self.locators.REGISTER_BTN_LOCATOR)

    def show_all_cases(self):
        self.click(self.locators.SHOW_ALL_LINK_LOCATOR)

    def click_case_image(self):
        self.click(self.locators.CASE_IMAGE_LOCATOR)

    def click_detailed_button(self):
        self.scroll_click(self.locators.DETAILED_BTN_LOCATOR)

    def find_detailed_button(self):
        self.find(self.locators.DETAILED_BTN_LOCATOR)

    def click_events_banner(self):
        self.scroll_click(self.locators.WEBINAR_BANNER_LOCATOR)

    def click_news_banner(self):
        self.scroll_click(self.locators.NEWS_BANNER_LOCATOR)




# class MainPageUnauthorized(BasePage):
#     url = 'https://ads.vk.com/'
#     locators = MainPageLocators()
#     authorize = False
#
#     def try_to_register(self):
#         self.click(self.locators.REGISTER_BTN_LOCATOR)
#
#         return OverviewPage(self.driver)

