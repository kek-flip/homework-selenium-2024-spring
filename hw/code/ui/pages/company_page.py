from .base_page import BasePage
from ui.locators.company_page_locators import CompanyPageLocators
from selenium.webdriver.support import expected_conditions as EC

class CompanyPage(BasePage):
    locators = CompanyPageLocators()
    url = 'https://ads.vk.com/hq/dashboard'

    def create_company(self):
        self.click(self.locators.CREATE_COMPANY_BTN_LOCATOR)

    def clear_companies(self):
        pass

    def select_site_target(self):
        self.click(self.locators.SITE_COMPANY_TARGER_BTN_LOCATOR)
    
    def fill_site_url(self, url):
        self.fill(self.locators.SITE_URL_INPUT_LOCATOR, url)
        self.unfocus()

    def close_help_modal(self):
        try:
            self.click(self.locators.CLOSE_HELP_MODAL_BTN_LOCATOR)
        except:
            pass

    def apply_target(self):
        self.fill(self.locators.COMPANY_BUDGET_INPUT_LOCATOR, '1000')
        self.click(self.locators.APPLY_COMPANY_TARGET_BTN_LOCATOR)
        self.click(self.locators.APPLY_COMPANY_TARGET_BTN_LOCATOR)

    def apply_groups(self):
        self.find(self.locators.TARGET_LABEL_LOCATOR)
        self.click(self.locators.APPLY_COMPANY_GROUP_BTN_LOCATOR)

    def assert_no_region_message(self):
        self.find(self.locators.NO_REGION_ERROR_LOCATOR)

    def open_interests(self):
        self.click(self.locators.INTERESTS_SECTION_LOCATOR)
        self.click(self.locators.INTERESTS_SUBSECTION_LOCATOR)

    def open_interests_dropdown(self):
        self.click(self.locators.INTERESTS_DROPDOWN_BTN_LOCATOR)

    def assert_interests_dropdown(self):
        self.fill(self.locators.INTERESTS_DROPDOWN_CONTENT_LOCATOR)
