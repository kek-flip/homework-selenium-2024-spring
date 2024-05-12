from .base_page import BasePage
from  ui.locators.cabinet_locators import CabinetLocators
from selenium.common.exceptions import TimeoutException


class CabinetPage(BasePage):
    url = 'https://ads.vk.com//hq/overview'
    locators = CabinetLocators()

    def click_campaign(self):
        self.click(self.locators.CAMPAIGN_LOCATOR)

    def click_audience(self):
        self.click(self.locators.AUDIENCE_LOCATOR)

    def click_budget(self):
        self.click(self.locators.BUDGET_LOCATOR)

    def click_education(self):
        self.click(self.locators.EDUCATION_LOCATOR)

    def is_education_modal_shown(self):
        return self.is_visible(self.locators.EDUCATION_MODAL_LOCATOR)

    def click_cross_education_modal(self):
        self.click(self.locators.EDUCATION_MODAL_CROSS_LOCATOR)

    def is_education_modal_closed(self):
        return self.is_not_visible(self.locators.EDUCATION_MODAL_LOCATOR)

    def click_commerce_centre(self):
        self.click(self.locators.COMMERCE_CENTRE_LOCATOR)

    def click_sites(self):
        self.click(self.locators.SITES_LOCATOR)

    def click_apps(self):
        self.click(self.locators.APPS_LOCATOR)

    def click_lead_forms(self):
        self.click(self.locators.LEAD_FORM_LOCATOR)

    def click_settings(self):
        self.click(self.locators.SETTINGS_LOCATOR)

    def click_help(self):
        self.scroll_click(self.locators.HELP_LOCATOR)

    def is_help_modal_shown(self):
        return self.is_visible(self.locators.HELP_MODAL_LOCATOR)

    def is_help_modal_closed(self):
        return self.is_not_visible(self.locators.HELP_MODAL_LOCATOR)

    def click_cases(self):
        self.click(self.locators.CASES_LOCATOR)

    def click_spravka(self):
        self.click(self.locators.SPRAVKA_LOCATOR)

    def click_forum(self):
        self.click(self.locators.FORUM_LOCATOR)

    def click_question(self):
        self.click(self.locators.QUESTION_LOCATOR)

    def is_messenger_visible(self):
        return self.is_visible(self.locators.MESSENGER_LOCATOR)

    def click_logo(self):
        self.click(self.locators.LOGO_LOCATOR)

    def click_account(self):
        self.click(self.locators.ACCOUNT_LOCATOR)

    def is_account_modal_visible(self):
        return self.is_visible(self.locators.ACCOUNT_MODAL_LOCATOR)

    def click_all_cabinets(self):
        self.click(self.locators.ALL_CABINETS_LOCATOR)

    def click_balance(self):
        self.click(self.locators.BALANCE_LOCATOR)

    def is_balance_modal_visible(self):
        return self.is_visible(self.locators.BALANCE_MODAL_LOCATOR)

    def click_notifications(self):
        self.click(self.locators.NOTIFICATION_LOCATOR)

    def is_notification_visible(self):
        return self.is_visible(self.locators.NOTIFICATION_MODAL_LOCATOR)

    def click_profile(self):
        self.click(self.locators.PROFILE_LOCATOR)

    def is_profile_modal_visible(self):
        return self.is_visible(self.locators.PROFILE_MODAL_LOCATOR)

    def click_logout(self):
        self.click(self.locators.LOGOUT_LOCATOR)


