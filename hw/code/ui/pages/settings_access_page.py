from .base_page import BasePage
from  ui.locators.settings_access_locators import SettingsAccessLocators
from selenium.common.exceptions import TimeoutException


class SettingsAccessPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/access'
    locators = SettingsAccessLocators()

    def click_add_cabinet(self):
        self.click(self.locators.ADD_CABINET_BTN_LOCATOR)

    def fill_id(self, text):
        self.fill(self.locators.ID_INPUT_LOCATOR, text)

    def click_save(self):
        self.click(self.locators.SAVE_BTN_LOCATOR)

    def id_error(self, error):
        return self.form_error(self.locators.ID_INPUT_LOCATOR, error=error)

    def is_alert_visible(self):
        return self.is_visible(self.locators.WRONG_ID_ALERT_LOCATOR)
