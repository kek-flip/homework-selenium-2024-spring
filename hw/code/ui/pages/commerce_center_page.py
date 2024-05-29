from .base_page import BasePage
from ui.locators.commerce_center_locators import CommerceCenterPageLocators
from selenium.webdriver.support import expected_conditions as EC

class CommerceCenterPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CommerceCenterPageLocators()

    def open_catalog_creation(self):
        self.click(self.locators.CREATE_CATALOG_BTN_LOCATOR)

    def open_catalog_settings(self):
        self.find(self.locators.CATALOG_NAME_INPUT_LOCATOR, 100)

    def is_error_visible(self):
        return self.is_visible(self.locators.ERROR_LOCATOR)

    def is_catalog_invisible(self):
        return self.is_not_visible()

    def is_must_have_field_visible(self):
        return self.is_visible(self.locators.MUST_HAVE_FIELD)
        
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

    def fill_file(self, file):
        self.fill(self.locators.FILE_INPUT_LOCATOR, file)

    def submit_catalog_creation(self):
        self.click(self.locators.SUBMIT_CATALOG_BTN_LOCATOR)

    def wait_for_feed_load(self):
        self.find(self.locators.ROW_LOCATOR, 200)
    
    def open_goods_tab(self):
        self.click(self.locators.GOODS_TAB_LOCATOR)

    def open_group_tab(self):
        self.click(self.locators.GROUP_TAB_LOCATOR)

    def get_catalog_goods(self):
        goods_titles = map(lambda good_title_element: good_title_element.text, self.find_all(self.locators.GOODS_TITLES_LOCATOR))
        goods_IDs = map(lambda good_id_element: good_id_element.text[3:], self.find_all(self.locators.GOODS_ID_LOCATOR))
        goods_models = map(lambda good_model_element: good_model_element.text, self.find_all(self.locators.GOODS_MODEL_LOCATOR))

        goods = []
        for id, title, model in zip(goods_IDs, goods_titles, goods_models):
            goods.append({'id': id, 'title': title, 'model': model})
        
        return goods

    def open_commerce_center(self):
        self.click(self.locators.left_menu.COMMERCE_CENTER_BTN_LOCATOR)

    def clear_catalogs(self):
        self.click(self.locators.CATALOG_SETTINGS_LOCATOR)
        self.click(self.locators.CATALOG_DELETE_LOCATOR)
        self.click(self.locators.FINAL_DELETE_LOCATOR)

    def search_catalog(self, catalog_name):
        self.find(self.locators.CATALOG_SEARCH_INPUT_LOCATOR).clear()
        self.fill(self.locators.CATALOG_SEARCH_INPUT_LOCATOR, catalog_name)

    def wait_for_lens(self):
        self.find(self.locators.LENS_LOCATOR)

    def wait_for_right_menu(self):
        self.fill(self.locators.RIGHT_MENU_LOCATOR)

    def open_good_info(self):
        self.click(self.locators.ROW_LOCATOR)

    def sort_by_name(self):
        self.click(self.locators.GOOD_NAME_HEADER_LOCATOR)

    def sort_by_model(self):
        self.find_all(self.locators.HEADER_ROW_ITEMS_LOCATOR)[5].click()

    def open_goods_tab_settings(self):
        self.click(self.locators.GOODS_TAB_SETTINGS_LOCATOR)

    def get_first_column_name(self):
        self.find_all(self.locators.GOOD_COLUMN_NAMES_BTN_LOCATOR)[1].text

    def remove_first_column(self):
        self.click(self.locators.GOOD_COLUMN_REMOVE_BTN_LOCATOR)

    def submit_goods_settings(self):
        self.click(self.locators.GOODS_TAB_SUBMIT_BTN_LOCATOR)

    def create_good_group(self):
        self.click(self.locators.GROUP_CREATION_BTN_LOCATOR)

    def open_create_group_from_scratch(self):
        self.find_all(self.locators.GROUP_DROPDOWN_ITEMS_LOCATOR)[1].click()

    def open_create_group_with_filters(self):
        self.find_all(self.locators.GROUP_DROPDOWN_ITEMS_LOCATOR)[0].click()

    def check_first_good_in_group(self):
        self.click(self.locators.GROUP_GOOD_CHECK_LOCATOR)

    def get_first_good_name(self):
        self.find_all(self.locators.GROUP_GOOD_TITLE_LOCATOR)[0].text

    def get_group_name(self):
        self.find(self.locators.GROUP_NAME_LOCATOR).text

    def open_first_group(self):
        self.find_all(self.locators.GROUPS_LOCATOR)[1].click()

    def is_group_visible(self):
        self.is_visible(self.locators.GROUP_NAME_LOCATOR)

    def clear_groups(self):
        # TODO not to do
        self.find(self.locators.SUCCESS_CATALOG_REMOVE_NOTIFY_LOCATOR, 100)
