from .base_page import BasePage
from  ui.locators.education_locators import EducationLocators
from selenium.common.exceptions import TimeoutException


class EducationPage(BasePage):
    
    url = 'https://ads.vk.com/hq/overview'
    locators = EducationLocators()
    
    def click_education(self):
        self.click(self.locators.EDUCATION_LOCATOR)
    
    def click_cross(self):
        self.click(self.locators.CROSS_LOCATOR)
    
    def is_window_not_visible(self):
        return self.is_not_visible(self.locators.WINDOW_LOCATOR)