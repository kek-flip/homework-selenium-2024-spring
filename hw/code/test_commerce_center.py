from base import BaseCase
from ui.pages.commerce_center_page import CommerceCenterPage

from ui.locators.commerce_center_locators import FeedSources
import csv

class TestCommerceCenter(BaseCase):
    def test_open_side_menu(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_commerce_center()
        commerce_center_page.open_catalog_settings()
        commerce_center_page.wait_for_right_menu()
        

    def test_create_catalog_from_link(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()

        with open(self.config['feed_path'], newline='', encoding='utf-8') as csvfile:
           goods = sorted(commerce_center_page.get_catalog_goods(), key=lambda good: good['id'])
           reader = csv.DictReader(csvfile)
           for row, good in zip(reader, goods):
               assert row['id'] == good['id']
               assert row['title'] == good['title']
        
        commerce_center_page.open_commerce_center()
        commerce_center_page.clear_catalogs()
    
    def test_rename_catalog(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_commerce_center()
        commerce_center_page.open_catalog_settings()
        commerce_center_page.rename_catalog("new_catalog")
        
        assert "new_catalog" in commerce_center_page.driver.page_source
        commerce_center_page.clear_catalogs()
    
    def test_search_catalog_positive(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_commerce_center()
        commerce_center_page.open_catalog_settings()
        commerce_center_page.rename_catalog("new_catalog")
        commerce_center_page.search_catalog("new_catalog")

        assert "new_catalog" in commerce_center_page.driver.page_source
        commerce_center_page.clear_catalogs()

    def test_search_catalog_negative(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_commerce_center()
        commerce_center_page.open_catalog_settings()
        commerce_center_page.rename_catalog("new_catalog")
        commerce_center_page.search_catalog("not_existing_catalog")
        commerce_center_page.wait_for_lens()

        assert "Ничего не найдено" in commerce_center_page.driver.page_source

        commerce_center_page.search_catalog("")
        commerce_center_page.clear_catalogs()

    def test_good_info_right_menu(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()
        commerce_center_page.open_good_info()
        commerce_center_page.wait_for_right_menu()
