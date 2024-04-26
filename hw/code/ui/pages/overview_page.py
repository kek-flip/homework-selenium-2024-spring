from .base_page import BasePage
from locators.overview_locators import OverviewPageLocators

class OverviewPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = OverviewPageLocators()