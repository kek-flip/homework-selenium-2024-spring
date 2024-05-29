from selenium.webdriver.common.by import By
from .left_menu_locators import LeftMenuLocators

class CompanyPageLocators:
    left_menu = LeftMenuLocators()

    LOGO = (By.CSS_SELECTOR, '[data-route=root]')

    CLOSE_HELP_MODAL_BTN_LOCATOR = (By.CSS_SELECTOR, '[role=button][aria-label=Закрыть]')

    COMPANIES_DRAFTS = (By.CSS_SELECTOR, '[data-testid=drafts-button]')
    COMPANY_DRAFT_NAME = (By.CSS_SELECTOR, '.nameCellContent_content__TyfEC > button')

    CREATE_COMPANY_BTN = (By.CSS_SELECTOR, '[data-testid=create-button]')
    COMPANY_BUDGET_INPUT = (By.CSS_SELECTOR, '[data-testid=targeting-not-set]')
    APPLY_COMPANY_TARGET_BTN = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/div[2]/button')
    APPLY_COMPANY_GROUP_BTN = (By.XPATH, "//*[contains(@class, 'CreateFooter_footerContentGroup__Hm+Yd')]/div[2]/button[2]")
    SAVE_COMPANY_BTN = (By.XPATH, "//*[contains(@class, 'CreateFooter_footerContentGroup__Hm+Yd')]/div[2]/button[1]")

    SITE_COMPANY_TARGET = (By.CSS_SELECTOR, '[data-id=site_conversions]')
    SITE_URL_INPUT = (By.CSS_SELECTOR, '[placeholder="Введите ссылку на сайт"]')

    NO_REGION_ERROR_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-1"]/fieldset/div/div/section')
    REGION_RUSSIA_BTN_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-33"]/fieldset/div/div/div[1]/div[2]/button[1]')
    TARGET_LABEL_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[2]/section/div/div/div/div/div/div[1]/div[1]')

    INTERESTS_SECTION_LOCATOR = (By.CSS_SELECTOR, '[data-testid=section-interests]')
    INTERESTS_SUBSECTION_LOCATOR = (By.CSS_SELECTOR, '#react-collapsed-toggle-69')
    INTERESTS_DROPDOWN_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-name=interests] > div')
    INTERESTS_DROPDOWN_CONTENT_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[1]/div[5]/div')

    AD_HEADER_INPUT = (By.CSS_SELECTOR, '[name="заголовок, макс. 40 символов"]')
    AD_SHORT_DECS_TEXTAREA = (By.CSS_SELECTOR, '[name="заголовок, макс. 90 символов"]')
