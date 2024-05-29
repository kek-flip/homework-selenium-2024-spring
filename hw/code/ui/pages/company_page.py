from .base_page import BasePage
from ui.locators.company_page_locators import CompanyPageLocators
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum

class CompanyTarget(Enum):
    SITE = 'site'
class CompanyPage(BasePage):
    locators = CompanyPageLocators()
    url = 'https://ads.vk.com/hq/dashboard'

    def open_companies_list(self):
        self.click(self.locators.LOGO)
        self.click(self.locators.left_menu.COMPANIES_BTN)

    def open_companies_drafts(self):
        self.click(self.locators.COMPANIES_DRAFTS)

    def get_companies_drafts(self):
        return map(lambda company_draft_name_element: company_draft_name_element.text, self.find_all(self.locators.COMPANY_DRAFT_NAME))

    def open_company_creation(self):
        self.click(self.locators.CREATE_COMPANY_BTN)

    def clear_companies(self):
        pass

    def select_target(self, target: CompanyTarget):
        if target == CompanyTarget.SITE:
            self.click(self.locators.SITE_COMPANY_TARGET)
    
    def set_site_url(self, url: str):
        self.fill_in(self.locators.SITE_URL_INPUT, url)

    def close_help_modal(self):
        try:
            self.click(self.locators.CLOSE_HELP_MODAL_BTN_LOCATOR)
        except:
            pass

    def apply_target(self):
        self.fill(self.locators.COMPANY_BUDGET_INPUT, '1000')
        self.unfocus()
        self.click(self.locators.APPLY_COMPANY_TARGET_BTN)

    def apply_groups(self):
        self.find(self.locators.TARGET_LABEL_LOCATOR)
        self.click(self.locators.APPLY_COMPANY_GROUP_BTN)

    def set_region(self):
        self.find(self.locators.TARGET_LABEL_LOCATOR)
        self.click(self.locators.REGION_RUSSIA_BTN_LOCATOR)

    def is_no_region_message_visible(self):
        return self.is_visible(self.locators.NO_REGION_ERROR_LOCATOR)

    def open_interests(self):
        self.click(self.locators.INTERESTS_SECTION_LOCATOR)
        self.click(self.locators.INTERESTS_SUBSECTION_LOCATOR)

    def open_interests_dropdown(self):
        self.click(self.locators.INTERESTS_DROPDOWN_BTN_LOCATOR)

    def is_interests_dropdown_visible(self):
        return self.is_visible(self.locators.INTERESTS_DROPDOWN_CONTENT_LOCATOR)

    def set_ad_header(self, header: str):
        self.fill_in(self.locators.AD_HEADER_INPUT, header)

    def set_ad_short_desc(self, description: str):
        self.fill_in(self.locators.AD_SHORT_DECS_TEXTAREA, description)

    def save_company(self):
        self.click(self.locators.SAVE_COMPANY_BTN)
