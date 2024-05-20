from .base_page import BasePage
from  ui.locators.footer_locators import FooterLocators

class FooterPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = FooterLocators()

    def click_logotip(self):
        self.scroll_click(self.locators.LOGOTIP_LOCATOR)

    def click_news(self):
        self.scroll_click(self.locators.NEWS_LOCATOR)
    
    def click_cookie(self):
        self.click(self.locators.COOKIE_LOCATOR)
    
    def click_documents(self):
        self.scroll_click(self.locators.DOCUMENTS_LOCATOR)
    
    def click_buisness(self):
        self.scroll_click(self.locators.BUISNESS_LOCATOR)
            
    def click_vkbuisness(self):
        self.scroll_click(self.locators.VKBUISNESS_LOCATOR)
            
    def click_vk(self):
        self.scroll_click(self.locators.VK_LOCATOR)
    
    def click_ok(self):
        self.scroll_click(self.locators.OK_LOCATOR)
    
    def click_telegram(self):
        self.scroll_click(self.locators.TELEGRAM_LOCATOR)
    # def click_forum(self):
    #     self.click(self.locators.FORUM_LOCATOR)
    
    def click_monetization(self):
        self.scroll_click(self.locators.MONETIZATION_LOCATOR)

    def click_help(self):
        self.scroll_click(self.locators.HELP_LOCATOR)

    def click_cabinet(self):
        self.scroll_click(self.locators.CABINET_LOCATOR)
    
    def click_cases(self):
        self.scroll_click(self.locators.CASES_LOCATOR)

    def click_insights(self):
        self.scroll_click(self.locators.INSIGHTS_LOCATOR)
        
    def click_events(self):
        self.scroll_click(self.locators.EVENTS_LOCATOR)

    def click_language(self):
        self.scroll_click(self.locators.LANGUAGE_LOCATOR)

    def is_lang_visible(self):
        return self.is_visible(self.locators.LANGUAGE_POPUP_LOCATOR)

    def click_en(self):
        self.scroll_click(self.locators.EN_LOCATOR)
    
    def click_ru(self):
        self.scroll_click(self.locators.RU_LOCATOR)
    
    def click_about(self):
        self.scroll_click(self.locators.ABOUT_LOCATOR)
    # def click_courses(self):
    #     self.click(self.locators.COURSES_LOCATOR)
        
    # def click_certification(self):
    #     self.click(self.locators.CERTIFICATION_LOCATOR)