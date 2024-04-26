from base import BaseCase
from ui.pages.commerce_center_page import CommerceCenterPage

from ui.locators.commerce_center_locators import FeedSources
import csv

class TestCommerceCenter(BaseCase):
    def test_create_catalog_from_link(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()

        with open(self.config['feed_path'], newline='') as csvfile:
           goods = sorted(commerce_center_page.get_catalog_goods(), key=lambda good: good['id'])
           reader = csv.DictReader(csvfile)
           for row, good in zip(reader, goods):
               assert row['id'] == good['id']
               assert row['title'] == good['title']
        
        commerce_center_page.open_commerce_center()
        commerce_center_page.clear_catalogs()
