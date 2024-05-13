from .base_page import BasePage
from  ui.locators.registration_locators import RegistrationLocators
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = RegistrationLocators()

    def click_create(self):
        self.click(self.locators.CREATE_CABINET_BTN_LOCATOR)

    def select_country(self, country_name):
        self.click(self.locators.COUNTRY_LOCATOR)
        self.click(self.locators.VK_UI_SELECT_ELEM(country_name))

    def available_currencies_after_country_change(self, main_currency):
        self.wait(timeout=5)

        self.click(self.locators.CURRENCY_LOCATOR)
        elems = self.find_all(self.locators.VK_UI_SELECT_ELEMS)
        return tuple(elem.get_attribute("title") for elem in elems)

    def click_create_account(self):
        self.click(self.locators.CREATE_CABINET_BTN_LOCATOR)
        self.click(self.locators.CREATE_ACCOUNT_BTN_LOCATOR)

    def email_error(self, error):
        return self.form_error(self.locators.EMAIL_INPUT_LOCATOR, error=error)

    def fill_in_form(self, email, terms_accepted=True):
        self.fill_in(self.locators.EMAIL_INPUT_LOCATOR, email)
        if not terms_accepted:
            self.click(self.locators.TERMS_LOCATOR)
        self.click(self.locators.CREATE_ACCOUNT_BTN_LOCATOR)

    def click_create_account(self):
        self.click(self.locators.CREATE_ACCOUNT_BTN_LOCATOR)

    def choose_physical(self):
        self.click(self.locators.PHYSICAL)

    def fill_inn(self, inn):
        self.fill(self.locators.INN_LOCATOR, inn)

    def inn_error(self, error):
        return self.form_error(self.locators.INN_LOCATOR, error=error)

    def terms_not_accepted_error(self, error):
        return self.form_error(self.locators.TERMS_LOCATOR, error=error)

    def delete_account(self):
        self.click(self.locators.SETTINGS_LOCATOR)
        self.scroll_click(self.locators.DELETE_ACCOUNT_BTN_LOCATOR)
        self.click(self.locators.DELETE_LOCATOR)



