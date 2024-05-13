from selenium.webdriver.common.by import By


class RegistrationLocators:
    @staticmethod
    def VK_UI_SELECT_ELEM(text):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']")

    @staticmethod
    def BY_TEXT(text):
        return (By.XPATH, f".//*[text()='{text}']")

    CREATE_CABINET_BTN_LOCATOR = (By.ID, 'click-createNewButton')
    AGENCY_LOCATOR = (By.XPATH, f".//*[text()='Агентство']")
    REKLAM_MAN_LOCATOR = (By.XPATH, f".//*[text()='Рекламодатель']")
    COUNTRY_LOCATOR = (By.CSS_SELECTOR, '[data-testid="country"]')
    CURRENCY_LOCATOR = (By.CSS_SELECTOR, '[data-testid="currency"]')
    VK_UI_SELECT_ELEMS = (By.XPATH, "//*[contains(concat(' ', @class, ' '), ' vkuiCustomSelectOption ')]")
    CREATE_ACCOUNT_BTN_LOCATOR = (By.XPATH, f".//*[text()='Создать кабинет']")
    EMAIL_INPUT_LOCATOR = (By.NAME, "email")
    TERMS_LOCATOR = (By.CLASS_NAME, "registration_offerTitle__BqyqW")
    FORM_ERROR_LOCATOR = (By.CLASS_NAME, "vkuiFormStatus--mode-error")
    ERROR = (By.CLASS_NAME, "vkuiFormItem--status-error")
    PHYSICAL = BY_TEXT("Физическое лицо")
    INN_LOCATOR = (By.NAME, "inn")
    SETTINGS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/settings"]')
    DELETE_ACCOUNT_BTN_LOCATOR = (By.CLASS_NAME, "DeleteAccount_button__BEy7F")
    DELETE_LOCATOR = (By.XPATH, f".//*[text()='Да, удалить']")
