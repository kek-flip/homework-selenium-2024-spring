from selenium.webdriver.common.by import By
from .left_menu_locators import LeftMenuLocators

class AudiencePageLocators:
    left_menu = LeftMenuLocators()

    USERS_LIST_TAB_BTN = (By.CSS_SELECTOR, '#tab_audience.users_list')

    AUDIENCE_NAME_LOCATOR = (By.CSS_SELECTOR, '.NameCell_wrapper__hxqrL > h5')
    AUDIENCE_MENU_LOCATOR = (By.CSS_SELECTOR, '[data-testid=audience-item-menu]')
    AUDIENCE_MENU_ITEM_BTN = (By.CSS_SELECTOR, '[data-testid=dropdown-item]')

    CREATE_AUDIENCE_BTN = (By.CSS_SELECTOR, '[data-testid=create-audience]')
    AUDIENCE_NAME_INPUT = (By.CSS_SELECTOR, 'span.vkuiFormField > input')
    ADD_AUDIENCE_SRC_BTN = (By.CSS_SELECTOR, '.vkuiInternalGroup > div > button')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[data-testid=submit]')
    SUCCESS_NOTIFY = (By.CSS_SELECTOR, '.vkuiSnackbar')

    AUDIENCE_SRC = (By.CSS_SELECTOR, 'div.ModalSidebarPage_content__2mBu8 > section > div[role=button]')

    EXISTING_AUDIENCE_SELECT = (By.CSS_SELECTOR, '.vkuiCustomSelect')

    @staticmethod
    def EXISTING_AUDIENCE_SELECT_ITEM(audience_name):
        return (By.XPATH, f"//*[contains(@class, 'Segment_option__79RaG')][text()='{audience_name}']")
    
    EXISTING_USERS_LIST_SELECT = (By.CSS_SELECTOR, '.vkuiCustomSelect')

    @staticmethod
    def EXISTING_USERS_LIST_SELECT_ITEM(users_list_name):
        return (By.XPATH, f"//*[contains(@class, 'UsersListSelect_option__gUna1')][text()='{users_list_name}']")
    
    NEW_USERS_LIST_TAB = (By.CSS_SELECTOR, '#tab-create-from-user-list-new')

    NEW_USERS_LIST_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="Введите название списка"]')

    NEW_USERS_LIST_TYPE_SELECT = (By.CSS_SELECTOR, '.vkuiCustomSelect')

    @staticmethod
    def NEW_USERS_LIST_TYPE_SELECT_ITEM(type):
        return (By.CSS_SELECTOR, f'[role=option][title={type}]')
    
    NEW_USERS_LIST_FILE_INPUT = (By.CSS_SELECTOR, 'input[type=file]')

    KEYWORDS_NAME_INPUT = (By.CSS_SELECTOR, '.SelectSourceModal_groupSourceWrapper__wAURc > div > span > input')

    KEYWORDS_TEXTAREA = (By.CSS_SELECTOR, '.KeyPhrases_textarea__wzycT > textarea')
