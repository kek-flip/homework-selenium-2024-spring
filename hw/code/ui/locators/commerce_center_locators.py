from selenium.webdriver.common.by import By
from .left_menu_locators import LeftMenuLocators
from enum import Enum

class FeedSources(Enum):
    URL = 'url'
    FILE = 'file'

class CommerceCenterPageLocators:
    left_menu = LeftMenuLocators()
    CREATE_CATALOG_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid=create-catalog]')

    CATALOG_MENU_BTNS_LOCATOR = (By.XPATH, '//*[@id="catalogs"]/div/div/section/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div')
    MENU_ITEM_BTNS_LOCATOR = (By.CSS_SELECTOR, '[data-testid=dropdown-item]')
    CATALOG_NAME_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid=catalogName-input]')
    SUBMIT_CATALOG_SETTINGS_LOCATOR = (By.CSS_SELECTOR, '[data-testid=submit]')

    CATALOG_SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, '[type=search][data-testid=search]')
    LENS_LOCATOR = (By.CSS_SELECTOR, 'svg.vkuiIcon[width="56"]')

    REMOVE_CATALOG_MODAL_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid=button-remove]')
    CLOSE_HELP_MODAL_BTN_LOCATOR = (By.CSS_SELECTOR, '[role=button][aria-label=Закрыть]')

    SUCCESS_CATALOG_REMOVE_NOTIFY_LOCATOR = (By.CSS_SELECTOR, '.vkuiSnackbar')

    FEED_FROM_URL_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-entityid=url]')
    FEED_FROM_FILE_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-entityid=file]')

    FEED_URL_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid=catalogUrl-input]')

    SUBMIT_CATALOG_BTN_LOCATOR = (By.CSS_SELECTOR, '[type=submit][title="Создать каталог"]')

    HISTORY_ROW_LOCATOR = (By.CSS_SELECTOR, '.BaseTable__row[role=row]')

    GOODS_TAB_LOCATOR = (By.CSS_SELECTOR, '[data-testid=catalog-tabs-goods]')

    GOODS_TITLES_LOCATOR = (By.CSS_SELECTOR, '.NameCell_itemNameBlock__m3cNF > h5')
    GOODS_ID_LOCATOR = (By.CSS_SELECTOR, '.NameCell_itemNameBlock__m3cNF > span')

    def get_locator_by_source(self, source):
        if source == FeedSources.URL:
            return self.FEED_FROM_URL_BTN_LOCATOR
        elif source == FeedSources.FILE:
            return self.FEED_FROM_FILE_BTN_LOCATOR
        else:
            raise TypeError('unknown source')
