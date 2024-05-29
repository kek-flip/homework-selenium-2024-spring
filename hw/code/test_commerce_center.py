from base import BaseCase
from ui.pages.commerce_center_page import CommerceCenterPage

from ui.locators.commerce_center_locators import FeedSources
import csv
import pytest

@pytest.fixture()
def delete_catalog(commerce_center_page: CommerceCenterPage, config):
    yield
    commerce_center_page.clear_catalogs()

@pytest.fixture()
def delete_group(commerce_center_page: CommerceCenterPage, config):
    yield
    commerce_center_page.clear_groups()

class TestCommerceCenter(BaseCase):

    def test_create_catalog_from_link(self, commerce_center_page: CommerceCenterPage, delete_catalog):
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

    def test_create_catalog_from_file(self, commerce_center_page: CommerceCenterPage, delete_catalog):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_file(self.config['feed_path'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()

        with open(self.config['feed_path'], newline='', encoding='utf-8') as csvfile:
           goods = sorted(commerce_center_page.get_catalog_goods(), key=lambda good: good['id'])
           reader = csv.DictReader(csvfile)
           for row, good in zip(reader, goods):
               assert row['id'] == good['id']
               assert row['title'] == good['title']

    def test_create_catalog_from_file_invalid_category(self, commerce_center_page: CommerceCenterPage, delete_catalog):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.fill_file(self.config['feed_path'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()

        assert commerce_center_page.is_error_visible()

    def test_create_catalog_from_file_invalid_input(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()

        assert commerce_center_page.is_must_have_field_visible()

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

    def test_delete_catalog(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()
        commerce_center_page.clear_catalogs()

        assert commerce_center_page.is_catalog_invisible()

    def test_create_group_with_filters(self, commerce_center_page: CommerceCenterPage, delete_group, delete_catalog):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_group_tab()
        commerce_center_page.create_good_group()
        commerce_center_page.open_create_group_with_filters()

        commerce_center_page.submit_goods_settings()

        assert commerce_center_page.is_group_visible()
        commerce_center_page.clear_groups()
        commerce_center_page.open_commerce_center()

    def test_create_group(self, commerce_center_page: CommerceCenterPage, delete_group,  delete_catalog):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_group_tab()
        commerce_center_page.create_good_group()
        commerce_center_page.open_create_group_from_scratch()

        good_name = commerce_center_page.get_first_good_name()
        commerce_center_page.check_first_good_in_group()
        commerce_center_page.submit_goods_settings()
        commerce_center_page.open_first_group()

        assert good_name in commerce_center_page.driver.page_source

    def test_search_catalog_positive(self, commerce_center_page: CommerceCenterPage, delete_catalog):
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

    def test_search_catalog_negative(self, commerce_center_page: CommerceCenterPage, delete_catalog):
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

    def test_sort_goods_by_name(self, commerce_center_page: CommerceCenterPage, delete_catalog):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()
        commerce_center_page.sort_by_name()

        goods = commerce_center_page.get_catalog_goods()
        sorted_goods = sorted(commerce_center_page.get_catalog_goods(), key=lambda good: good['title'])
        for g, sg in zip(goods, sorted_goods):
            assert g['id'] == sg['id']
            assert g['title'] == sg['title']

    def test_sort_goods_by_model(self, commerce_center_page: CommerceCenterPage, delete_catalog):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()
        commerce_center_page.sort_by_model()

        goods = commerce_center_page.get_catalog_goods()
        sorted_goods = sorted(commerce_center_page.get_catalog_goods(), key=lambda good: good['model'])
        for g, sg in zip(goods, sorted_goods):
            assert g['id'] == sg['id']
            assert g['title'] == sg['title']

    def test_remove_column(self, commerce_center_page: CommerceCenterPage, delete_catalog):
        commerce_center_page.close_help_modal()
        commerce_center_page.open_catalog_creation()
        commerce_center_page.select_feed_source(FeedSources.URL)
        commerce_center_page.fill_feed_url(self.config['feed_url'])
        commerce_center_page.submit_catalog_creation()
        commerce_center_page.wait_for_feed_load()
        commerce_center_page.open_goods_tab()
        commerce_center_page.open_goods_tab_settings()

        good_column = commerce_center_page.get_first_column_name()
        commerce_center_page.remove_first_column()
        commerce_center_page.submit_goods_settings()

        commerce_center_page.driver.navigate().refresh()
        assert good_column not in commerce_center_page.driver.page_source
