from .base_page import BasePage
from ui.locators.commerce_center_locators import CommerceCenterPageLocators

class CommerceCenterPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CommerceCenterPageLocators()

    def open_catalog_creation(self):
        self.click(self.locators.CREATE_CATALOG_BTN_LOCATOR)

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
        goods_names = map(lambda good_name_element: good_name_element.text, self.find_all(self.locators.GOODS_NAMES_LOCATOR))
        goods_IDs = map(lambda good_id_element: good_id_element.text[3:], self.find_all(self.locators.GOODS_ID_LOCATOR))

        goods = []
        for id, name in zip(goods_IDs, goods_names):
            goods.append({'id': id, 'name': name})
        
        return goods

    def open_commerce_center(self):
        self.click(self.locators.left_menu.COMMERCE_CENTER_BTN_LOCATOR)

    def clear_catalogs(self):
        pass
