from base import BaseCase
from ui.pages.settings_access_page import SettingsAccessPage
from selenium.webdriver.support.wait import WebDriverWait


class TestMainPage(BaseCase):

    def test_invalid_id(self, settings_access_page: SettingsAccessPage):
        settings_access_page.click_add_cabinet()
        settings_access_page.fill_id("8888888888")
        settings_access_page.click_save()
        assert settings_access_page.is_alert_visible()
