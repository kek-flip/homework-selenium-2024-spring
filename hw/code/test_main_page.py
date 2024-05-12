from base import UnauthorizedCase
from ui.pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait


class TestMainPage(UnauthorizedCase):

    def test_try_to_register(self, main_page: MainPage):
        main_page.try_to_register()
        assert self.is_url_open('https://id.vk.com/auth?')

    def test_show_all_cases(self, main_page: MainPage):
        main_page.show_all_cases()
        assert self.is_url_open('https://ads.vk.com/cases')

    def test_show_case(self, main_page: MainPage):
        main_page.click_case_image()
        assert self.is_url_open('https://ads.vk.com/cases/')

    def test_show_events(self, main_page: MainPage):
        main_page.click_events_banner()
        assert self.is_url_open('https://ads.vk.com/events')

    def test_show_news(self, main_page: MainPage):
        main_page.click_news_banner()
        assert self.is_url_open('https://ads.vk.com/news/')
