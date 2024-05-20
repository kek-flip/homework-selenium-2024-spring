from base import UnauthorizedCase
from ui.pages.footer_page import FooterPage
from selenium.webdriver.support.wait import WebDriverWait


class TestFooterPage(UnauthorizedCase):

    def test_go_to_main(self, footer_page: FooterPage):
        footer_page.click_logotip()  
        assert self.is_url_open('https://ads.vk.com/')

    def test_go_to_news(self, footer_page: FooterPage):
        footer_page.click_news()
        assert self.is_url_open('https://ads.vk.com/news')

    def test_go_to_monetization(self, footer_page: FooterPage):
        footer_page.click_monetization()
        footer_page.switch_to_new_tab()
        assert self.is_url_open('https://ads.vk.com/partner')
        
    def test_go_to_help(self, footer_page: FooterPage):
        footer_page.click_help()
        assert self.is_url_open('https://ads.vk.com/help')
    
    def test_go_to_cabinet(self, footer_page: FooterPage):
        footer_page.click_cabinet()
        assert self.is_redirect_occurred('https://ads.vk.com/')
    
    def test_go_to_cases(self, footer_page: FooterPage):
        footer_page.click_cases()
        assert self.is_url_open('https://ads.vk.com/cases')
    
    def test_go_to_insights(self, footer_page: FooterPage):
        footer_page.click_insights()
        assert self.is_url_open('https://ads.vk.com/insights')
    
    def test_go_to_events(self, footer_page: FooterPage):
        footer_page.click_events()
        assert self.is_url_open('https://ads.vk.com/events')
    
    def test_go_to_documents(self, footer_page: FooterPage):
        footer_page.click_documents()
        assert self.is_url_open('https://ads.vk.com/documents')
        
    def test_go_to_buisness(self, footer_page: FooterPage):
        footer_page.click_buisness()
        footer_page.switch_to_new_tab()
        assert self.is_redirect_occurred('https://ads.vk.com/')

    def test_go_to_vkbuisness(self, footer_page: FooterPage):
        footer_page.click_buisness()
        footer_page.switch_to_new_tab()
        assert self.is_redirect_occurred('https://vk.company/ru/company/business/')    
    
    def test_go_to_vk(self, footer_page: FooterPage):
        footer_page.click_cookie()
        footer_page.click_vk()
        footer_page.switch_to_new_tab()
        assert self.is_redirect_occurred('https://vk.com/vk_ads')    
        
    def test_go_to_ok(self, footer_page: FooterPage):
        footer_page.click_cookie()
        footer_page.click_ok()
        footer_page.switch_to_new_tab()
        assert self.is_url_open('https://ok.ru/group/64279825940712')    
    
    def test_go_to_telegram(self, footer_page: FooterPage):
        footer_page.click_cookie()
        footer_page.click_telegram()
        footer_page.switch_to_new_tab()
        assert self.is_url_open('https://t.me/vk_ads')
    
    def test_show_languages(self, footer_page: FooterPage):
        footer_page.click_cookie()
        footer_page.click_language()
        assert footer_page.is_lang_visible()
    
    def test_en(self, footer_page: FooterPage):
        footer_page.click_cookie()
        footer_page.click_language()
        footer_page.click_en()
        assert self.is_url_open('https://ads.vk.com/en')

    def test_ru(self, footer_page: FooterPage):
        footer_page.click_cookie()
        footer_page.click_language()
        footer_page.click_ru()
        assert self.is_url_open('https://ads.vk.com')
    
    def test_about(self, footer_page: FooterPage):
        footer_page.click_cookie()
        footer_page.click_about()
        footer_page.switch_to_new_tab()
        assert self.is_url_open('https://vk.company/ru/')