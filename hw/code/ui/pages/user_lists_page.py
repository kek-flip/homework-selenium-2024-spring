from .base_page import BasePage
from  ui.locators.user_lists_locators import UserListsLocators
from selenium.common.exceptions import TimeoutException


class UserListsPage(BasePage):
    url = 'https://ads.vk.com/hq/audience/user_lists'
    locators = UserListsLocators()

    def click_add_lists(self):
        self.click(self.locators.ADD_LIST_BTN_LOCATOR)

    def is_add_list_modal_visible(self):
        return self.is_visible(self.locators.ADD_LIST_MODAL_LOCATOR)

    def click_load_list(self):
        self.click(self.locators.LOAD_LIST_LOCATOR)

    def click_activate_list(self):
        self.click(self.locators.ACTIVATE_LIST_LOCATOR)

    def fill_key(self, key):
        self.fill(self.locators.KEY_INPUT_LOCATOR, key)

    def click_activate(self):
        self.click(self.locators.ACTIVATE_BTN_LOCATOR)

    def is_alert_visible(self):
        return self.is_visible(self.locators.WRONG_KEY_ALERT_LOCATOR)

    def click_search(self):
        self.click(self.locators.SEARCH_LOCATOR)

    def fill_search(self, text):
        self.fill(self.locators.SEARCH_LOCATOR, text)

    def is_nothing_found_visible(self):
        return self.is_visible(self.locators.NOTHING_LOCATOR)
