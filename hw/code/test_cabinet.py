from base import BaseCase
from ui.pages.cabinet import CabinetPage
from selenium.webdriver.support.wait import WebDriverWait


class TestMainPage(BaseCase):

    def test_go_to_cabinet(self):
        assert self.is_url_open('https://ads.vk.com/hq/overview')

    def test_go_to_campaign(self, cabinet_page: CabinetPage):
        cabinet_page.click_campaign()
        assert self.is_url_open('https://ads.vk.com/hq/dashboard/')

    def test_go_to_audience(self, cabinet_page: CabinetPage):
        cabinet_page.click_audience()
        assert self.is_url_open('https://ads.vk.com/hq/audience')

    def test_go_to_budget(self, cabinet_page: CabinetPage):
        cabinet_page.click_budget()
        assert self.is_url_open('https://ads.vk.com/hq/budget/transactions')

    def test_go_to_education(self, cabinet_page: CabinetPage):
        cabinet_page.click_education()
        assert cabinet_page.is_education_modal_shown()

    def test_close_education(self, cabinet_page: CabinetPage):
        cabinet_page.click_education()
        cabinet_page.click_cross_education_modal()
        assert cabinet_page.is_education_modal_closed()

    def test_go_to_commerce_center(self, cabinet_page: CabinetPage):
        cabinet_page.click_commerce_centre()
        assert self.is_url_open('https://ads.vk.com/hq/ecomm/catalogs')

    def test_go_to_sites(self, cabinet_page: CabinetPage):
        cabinet_page.click_sites()
        assert self.is_url_open('https://ads.vk.com/hq/pixels')

    def test_go_to_apps(self, cabinet_page: CabinetPage):
        cabinet_page.click_apps()
        assert self.is_url_open('https://ads.vk.com/hq/apps')

    def test_go_to_lead_forms(self, cabinet_page: CabinetPage):
        cabinet_page.click_lead_forms()
        assert self.is_url_open('https://ads.vk.com/hq/leadads/leadforms')

    def test_go_to_settings(self, cabinet_page: CabinetPage):
        cabinet_page.click_settings()
        assert self.is_url_open('https://ads.vk.com/hq/settings')

    def test_open_help(self, cabinet_page: CabinetPage):
        cabinet_page.click_help()
        assert cabinet_page.is_help_modal_shown()

    def test_close_help(self, cabinet_page: CabinetPage):
        cabinet_page.click_help()
        cabinet_page.click_lead_forms()
        assert cabinet_page.is_help_modal_closed()

    def test_go_to_cases(self, cabinet_page: CabinetPage):
        cabinet_page.click_help()
        cabinet_page.click_cases()
        cabinet_page.switch_to_new_tab()
        assert self.is_url_open('https://ads.vk.com/cases')

    def test_go_to_spravka(self, cabinet_page: CabinetPage):
        cabinet_page.click_help()
        cabinet_page.click_spravka()
        cabinet_page.switch_to_new_tab()
        assert self.is_url_open('https://ads.vk.com/help')

    def test_go_to_forum(self, cabinet_page: CabinetPage):
        cabinet_page.click_help()
        cabinet_page.click_forum()
        cabinet_page.switch_to_new_tab()
        assert self.is_url_open('https://ads.vk.com/upvote')

    def test_go_to_overview(self, cabinet_page: CabinetPage):
        cabinet_page.click_sites()
        cabinet_page.click_logo()
        assert self.is_url_open('https://ads.vk.com/hq/overview')

    def test_open_account(self, cabinet_page: CabinetPage):
        cabinet_page.click_account()
        assert cabinet_page.is_account_modal_visible()

    def test_go_to_access(self, cabinet_page: CabinetPage):
        cabinet_page.click_account()
        cabinet_page.click_all_cabinets()
        assert self.is_url_open('https://ads.vk.com/hq/settings/access')

    def test_open_balance(self, cabinet_page: CabinetPage):
        cabinet_page.click_balance()
        assert cabinet_page.is_balance_modal_visible()

    def test_open_notifications(self, cabinet_page: CabinetPage):
        cabinet_page.click_notifications()
        assert cabinet_page.is_notification_visible()

    def test_open_profile_modal(self, cabinet_page: CabinetPage):
        cabinet_page.click_profile()
        assert cabinet_page.is_profile_modal_visible()

    def test_logout(self, cabinet_page: CabinetPage):
        cabinet_page.click_profile()
        cabinet_page.click_logout()
        assert self.is_url_open('https://ads.vk.com/')

