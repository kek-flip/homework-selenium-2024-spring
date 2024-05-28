from .base_page import BasePage
from ui.locators.audience_locators import AudiencePageLocators
from enum import Enum
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class AudienceSource(Enum):
    EXISTING = 'existing'
    USERS_LIST = 'users list'
    KEYWORDS = 'keywords'

class UsersListType(Enum):
    EMAIL = 'Email'

class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    # -------Audience--------

    def submit_audience_source(self):
        self.find_all(self.locators.SUBMIT_BTN)[1].click()

    def submit_audience_creation(self):
        self.find_all(self.locators.SUBMIT_BTN)[0].click()

    def open_audiences_list(self):
        self.click(self.locators.left_menu.AUDIENCE_BTN)

    def open_users_list_list(self):
        self.click(self.locators.left_menu.AUDIENCE_BTN)
        self.click(self.locators.USERS_LIST_TAB_BTN)

    def open_audience_creation(self):
        self.click(self.locators.CREATE_AUDIENCE_BTN)

    def set_audience_name(self, name: str):
        self.fill_in(self.locators.AUDIENCE_NAME_INPUT, name)

    def open_sources_list(self):
        self.click(self.locators.ADD_AUDIENCE_SRC_BTN)

    def select_audience_source(self, source: AudienceSource):
        if source == AudienceSource.EXISTING:
            self.find_all(self.locators.AUDIENCE_SRC)[0].click()
        elif source == AudienceSource.USERS_LIST:
            self.find_all(self.locators.AUDIENCE_SRC)[1].click()

    def add_existing_audience(self, audience_name: str):
        self.click(self.locators.EXISTING_AUDIENCE_SELECT)
        self.click(self.locators.EXISTING_AUDIENCE_SELECT_ITEM(audience_name))

    def add_existing_users_list(self, users_list_name: str):
        self.click(self.locators.EXISTING_USERS_LIST_SELECT)
        self.click(self.locators.EXISTING_USERS_LIST_SELECT_ITEM(users_list_name))

    def load_new_users_list(self, users_list_name: str, type: str, file_name: str):
        try:
            self.click(self.locators.NEW_USERS_LIST_TAB)
        except:
            pass
        self.fill_in(self.locators.NEW_USERS_LIST_NAME_INPUT, users_list_name)
        self.click(self.locators.NEW_USERS_LIST_TYPE_SELECT)
        self.click(self.locators.NEW_USERS_LIST_TYPE_SELECT_ITEM(type))
        self.find_invisible(self.locators.NEW_USERS_LIST_FILE_INPUT).send_keys(file_name)

    def add_key_words(self, name: str, keywords: list[str], breakwords: list[str]):
        self.fill_in(self.locators.KEYWORDS_NAME_INPUT, name)

        [keywords_textarea, breakwords_textarea] = self.find_all(self.locators.KEYWORDS_TEXTAREA)
        for keyword in keywords:
            keywords_textarea.send_keys(keyword)
            keywords_textarea.send_keys(Keys.ENTER) 
        for breakword in breakwords:
            breakwords_textarea.send_keys(breakword)
            breakwords_textarea.send_keys(Keys.ENTER)

    def get_audiences(self) -> list[str]:
        return map(lambda audience_name_element: audience_name_element.text, self.find_all(self.locators.AUDIENCE_NAME_LOCATOR))

    def sort_audiences_by(self, column: str):
        pass

    def open_audience(self, name: str):
        self.hover(self.locators.AUDIENCE_MENU_LOCATOR)
        self.click(self.locators.AUDIENCE_MENU_LOCATOR)

    def clear_audiences(self):
        for menu_btn in self.find_all(self.locators.AUDIENCE_MENU_LOCATOR):
            hover = ActionChains(self.driver).move_to_element(menu_btn)
            hover.perform()
            self.find_all(self.locators.AUDIENCE_MENU_ITEM_BTN)[2].click()

    def wait_for_success_notify(self):
        self.find(self.locators.SUCCESS_NOTIFY, 600)

    # -------Users list--------

    def open_users_list_creation(self):
        self.click(self.locators.CREATE_USERS_LIST_BTN)

    def clear_users_lists(self):
        for menu_btn in self.find_all(self.locators.USERS_LIST_MENU_LOCATOR):
            hover = ActionChains(self.driver).move_to_element(menu_btn)
            hover.perform()
            self.find_all(self.locators.USERS_LIST_MENU_ITEM_BTN)[1].click()

    def submit_users_list_creation(self):
        self.click(self.locators.SUBMIT_BTN)

    def get_users_lists(self) -> list[str]:
        return map(lambda users_list_name_element: users_list_name_element.text, self.find_all(self.locators.USERS_LIST_NAME))
    
    def create_audience_from_list(self):
        self.click(self.locators.CREATE_AUDIENCE_FROM_LIST_CHECK)
