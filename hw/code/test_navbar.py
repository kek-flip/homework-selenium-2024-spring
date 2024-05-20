from base import UnauthorizedCase
from ui.pages.navbar_page import NavbarPage
from selenium.webdriver.support.wait import WebDriverWait


class TestNavbarPage(UnauthorizedCase):

    def test_go_to_main(self, navbar_page: NavbarPage):
        navbar_page.click_logotip()  
        assert self.is_url_open('https://ads.vk.com/')

    def test_go_to_news(self, navbar_page: NavbarPage):
        navbar_page.click_news()
        assert self.is_url_open('https://ads.vk.com/news')
    
    def test_go_to_forum(self, navbar_page: NavbarPage):
        navbar_page.click_forum()
        assert self.is_url_open('https://ads.vk.com/upvote')

    def test_go_to_monetization(self, navbar_page: NavbarPage):
        navbar_page.click_monetization()
        navbar_page.switch_to_new_tab()
        assert self.is_url_open('https://ads.vk.com/partner')
        
    def test_go_to_help(self, navbar_page: NavbarPage):
        navbar_page.click_help()
        assert self.is_url_open('https://ads.vk.com/help')
    
    def test_go_to_cabinet(self, navbar_page: NavbarPage):
        navbar_page.click_cabinet()
        assert self.is_redirect_occurred('https://ads.vk.com/')
    
    def test_go_to_cases(self, navbar_page: NavbarPage):
        navbar_page.click_cases()
        assert self.is_url_open('https://ads.vk.com/cases')
    
    def test_go_to_insights(self, navbar_page: NavbarPage):
        navbar_page.move_to_onboarding()
        navbar_page.click_insights()
        assert self.is_url_open('https://ads.vk.com/insights')
    
    def test_go_to_events(self, navbar_page: NavbarPage):
        navbar_page.move_to_onboarding()
        navbar_page.click_events()
        assert self.is_url_open('https://ads.vk.com/events')
    
    def test_go_to_courses(self, navbar_page: NavbarPage):
        navbar_page.move_to_onboarding()
        navbar_page.click_courses()
        navbar_page.switch_to_new_tab()
        assert self.is_url_open('https://expert.vk.com/catalog/courses/')
    
    def test_go_to_certification(self, navbar_page: NavbarPage):
        navbar_page.move_to_onboarding()
        navbar_page.click_certification()
        navbar_page.switch_to_new_tab()
        assert self.is_url_open('https://expert.vk.com/certification/')