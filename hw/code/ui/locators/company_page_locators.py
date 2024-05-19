from selenium.webdriver.common.by import By
from .left_menu_locators import LeftMenuLocators

class CompanyPageLocators:
    left_menu = LeftMenuLocators()

    CLOSE_HELP_MODAL_BTN_LOCATOR = (By.CSS_SELECTOR, '[role=button][aria-label=Закрыть]')

    CREATE_COMPANY_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid=create-button]')
    COMPANY_BUDGET_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid=targeting-not-set]')
    APPLY_COMPANY_TARGET_BTN_LOCATOR = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/div[2]/button')
    APPLY_COMPANY_GROUP_BTN_LOCATOR = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/div[2]/button[2]')

    SITE_COMPANY_TARGER_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-id=site_conversions]')
    SITE_URL_INPUT_LOCATOR = (By.CSS_SELECTOR, '[placeholder="Введите ссылку на сайт"]')

    NO_REGION_ERROR_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-1"]/fieldset/div/div/section')
    TARGET_LABEL_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[2]/section/div/div/div/div/div/div[1]/div[1]')
