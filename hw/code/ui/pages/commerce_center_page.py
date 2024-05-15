from .base_page import BasePage
from ui.locators.commerce_center_locators import CommerceCenterPageLocators
from selenium.webdriver.support import expected_conditions as EC

class CommerceCenterPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CommerceCenterPageLocators()

    def open_catalog_creation(self):
        self.click(self.locators.CREATE_CATALOG_BTN_LOCATOR)

    def open_catalog_settings(self):
        # self.click(self.locators.CATALOG_MENU_BTNS_LOCATOR)
        # self.click(self.locators.MENU_ITEM_BTNS_LOCATOR)
        self.find(self.locators.CATALOG_NAME_INPUT_LOCATOR, 100)
        
    def rename_catalog(self, new_name):
        self.find(self.locators.CATALOG_NAME_INPUT_LOCATOR).clear()
        self.fill(self.locators.CATALOG_NAME_INPUT_LOCATOR, new_name)
        self.click(self.locators.SUBMIT_CATALOG_SETTINGS_LOCATOR)

    def close_help_modal(self):
        try:
            self.click(self.locators.CLOSE_HELP_MODAL_BTN_LOCATOR)
        except:
            pass
    
    def select_feed_source(self, source):
        self.click(self.locators.get_locator_by_source(source))
    
    def fill_feed_url(self, url):
        self.fill(self.locators.FEED_URL_INPUT_LOCATOR, url)

    def submit_catalog_creation(self):
        self.click(self.locators.SUBMIT_CATALOG_BTN_LOCATOR)

    def wait_for_feed_load(self):
        self.find(self.locators.HISTORY_ROW_LOCATOR, 600)
    
    def open_goods_tab(self):
        self.click(self.locators.GOODS_TAB_LOCATOR)

    def get_catalog_goods(self):
        goods_titles = map(lambda good_title_element: good_title_element.text, self.find_all(self.locators.GOODS_TITLES_LOCATOR))
        goods_IDs = map(lambda good_id_element: good_id_element.text[3:], self.find_all(self.locators.GOODS_ID_LOCATOR))

        goods = []
        for id, title in zip(goods_IDs, goods_titles):
            goods.append({'id': id, 'title': title})
        
        return goods

    def open_commerce_center(self):
        self.click(self.locators.left_menu.COMMERCE_CENTER_BTN_LOCATOR)

    def clear_catalogs(self):
        # self.click(self.locators.CATALOG_MENU_BTNS_LOCATOR)
        # delete_btn = self.find_all(self.locators.MENU_ITEM_BTNS_LOCATOR)[1]
        # delete_btn.click()
        # self.hover(self.locators.REMOVE_CATALOG_MODAL_BTN_LOCATOR)
        # self.click(self.locators.REMOVE_CATALOG_MODAL_BTN_LOCATOR)
        self.find(self.locators.SUCCESS_CATALOG_REMOVE_NOTIFY_LOCATOR, 100)

    def search_catalog(self, catalog_name):
        self.find(self.locators.CATALOG_SEARCH_INPUT_LOCATOR).clear()
        self.fill(self.locators.CATALOG_SEARCH_INPUT_LOCATOR, catalog_name)
