from base import BaseCase
from ui.pages.education_page import EducationPage
from selenium.webdriver.support.wait import WebDriverWait


class TestFooterPage(BaseCase):
    
    def test_close_window(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_cross()
        assert education_page.is_window_not_visible()