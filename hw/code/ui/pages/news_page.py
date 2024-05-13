from .base_page import BasePage
from  ui.locators.news_locators import NewsLocators


class NewsPage(BasePage):
    url = 'https://ads.vk.com/news'
    locators = NewsLocators()

    def click_detailed(self):
        self.click(self.locators.DETAILED_BTN_LOCATOR)

    def click_news_image(self):
        self.click(self.locators.NEWS_IMAGE_LOCATOR)

    def click_to_cabinet(self):
        self.scroll_click(self.locators.TO_CABINET_BTN_LOCATOR)

    def click_back_to_news(self):
        self.click(self.locators.TO_NEWS_LOCATOR)
