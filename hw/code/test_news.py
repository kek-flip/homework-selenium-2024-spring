from base import UnauthorizedCase
from ui.pages.news_page import NewsPage


class TestMainPage(UnauthorizedCase):

    def test_go_to_detailed(self,  news_page: NewsPage):
        news_page.click_detailed()
        assert self.is_url_open('https://ads.vk.com/news/')

    def test_go_to_news(self,  news_page: NewsPage):
        news_page.click_news_image()
        assert self.is_url_open('https://ads.vk.com/news/')

    def test_go_to_cabinet(self,  news_page: NewsPage):
        news_page.click_news_image()
        news_page.click_to_cabinet()
        news_page.switch_to_new_tab()
        assert self.is_url_open('https://id.vk.com/auth?')

    def test_go_to_news(self,  news_page: NewsPage):
        news_page.click_news_image()
        news_page.click_back_to_news()
        assert self.is_url_open('https://ads.vk.com/news')


