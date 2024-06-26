from selenium.webdriver.common.by import By
from .left_menu_locators import LeftMenuLocators
from enum import Enum

class FeedSources(Enum):
    URL = 'url'
    FILE = 'file'

class CommerceCenterPageLocators:
    left_menu = LeftMenuLocators()

    RIGHT_MENU_LOCATOR = (By.CSS_SELECTOR, '.ModalRoot_componentWrapper__uzHTL')

    CREATE_CATALOG_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid=create-catalog]')

    CATALOG_MENU_BTNS_LOCATOR = (By.XPATH, '//*[@id="catalogs"]/div/div/section/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div')
    CATALOG_SETTINGS_LOCATOR = (By.CLASS_NAME, "Nav_buttonSettingsIcon__Q6eJ2")
    CATALOG_DELETE_LOCATOR = (By.XPATH, f'//span[text()="Удалить каталог"]')
    FINAL_DELETE_LOCATOR = (By.XPATH, f'//span[text()="Удалить"]')

    FILE_INPUT_LOCATOR = (By.CLASS_NAME, "LocalFileSelector_container__W4cfb")

    ERROR_LOCATOR = (By.XPATH, f'//span[text()="2 ошибки"]')

    MUST_HAVE_FIELD = (By.XPATH, f'//div[text()="Обязательное поле"]')

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

    ROW_LOCATOR = (By.CSS_SELECTOR, '.BaseTable__row[role=row]')
    HEADER_ROW_ITEMS_LOCATOR = (By.CSS_SELECTOR, '.BaseTable__header-row[role=row] > div')

    GOODS_TAB_LOCATOR = (By.CSS_SELECTOR, '[data-testid=catalog-tabs-goods]')
    GROUP_TAB_LOCATOR = (By.CSS_SELECTOR, '[data-testid=catalog-tabs-groups]')

    GOODS_TAB_SETTINGS_LOCATOR = (By.CSS_SELECTOR, '.TableSettings_settingsButton__uz8xK')
    GOODS_TAB_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, '[type=submit]')

    GOODS_TITLES_LOCATOR = (By.CSS_SELECTOR, '.NameCell_itemNameBlock__m3cNF > h5')
    GOODS_ID_LOCATOR = (By.CSS_SELECTOR, '.NameCell_itemNameBlock__m3cNF > span')
    GOODS_MODEL_LOCATOR = (By.CSS_SELECTOR, '.BaseTable__row[role=row] > div:nth-child(6) > span')

    GOOD_NAME_HEADER_LOCATOR = (By.CSS_SELECTOR, '[role=gridcell][data-key=name]')
    GOOD_COLUMN_REMOVE_BTN_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Удалить Наличие"]')
    GOOD_COLUMN_NAMES_BTN_LOCATOR = (By.CSS_SELECTOR, '[role=presentation] > span')

    GROUP_CREATION_BTN_LOCATOR = (By.CSS_SELECTOR, '.CatalogGroups_controls__MC4-s > button')
    GROUP_DROPDOWN_ITEMS_LOCATOR = (By.CSS_SELECTOR, '.CatalogGroups_createGroupDropdown__aPPLw')
    GROUPS_LOCATOR = (By.CSS_SELECTOR, 'data-testid=catalog-groups-nav-item')

    GROUP_GOOD_CHECK_LOCATOR = (By.XPATH, '//*[@id="0"]/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div')
    GROUP_GOOD_TITLE_LOCATOR = (By.CSS_SELECTOR, '.ModalRoot_componentWrapper__uzHTL .NameCell_itemNameBlock__m3cNF > h5')
    GROUP_NAME_LOCATOR = (By.NAME, "groupName")

    def get_locator_by_source(self, source):
        if source == FeedSources.URL:
            return self.FEED_FROM_URL_BTN_LOCATOR
        elif source == FeedSources.FILE:
            return self.FEED_FROM_FILE_BTN_LOCATOR
        else:
            raise TypeError('unknown source')
