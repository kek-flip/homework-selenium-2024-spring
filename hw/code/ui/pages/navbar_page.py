from .base_page import BasePage
from  ui.locators.navbar_locators import NavbarLocators

class NavbarPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = NavbarLocators()

    def click_logotip(self):
        self.click(self.locators.LOGOTIP_LOCATOR)

    def click_news(self):
        self.click(self.locators.NEWS_LOCATOR)
    
    def click_forum(self):
        self.click(self.locators.FORUM_LOCATOR)
    
    def click_monetization(self):
        self.click(self.locators.MONETIZATION_LOCATOR)

    def click_help(self):
        self.click(self.locators.HELP_LOCATOR)

    def click_cabinet(self):
        self.click(self.locators.CABINET_LOCATOR)
    
    def click_cases(self):
        self.click(self.locators.CASES_LOCATOR)

    def click_insights(self):
        self.click(self.locators.INSIGHTS_LOCATOR)
    
    def move_to_onboarding(self):
        self.hover(self.locators.ONBOARDING_LOCATOR)
        
    def click_events(self):
        self.click(self.locators.EVENTS_LOCATOR)

    def click_courses(self):
        self.click(self.locators.COURSES_LOCATOR)
        
    def click_certification(self):
        self.click(self.locators.CERTIFICATION_LOCATOR)