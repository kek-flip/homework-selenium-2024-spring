from selenium.webdriver.common.by import By

class LeftMenuLocators:
    LEFT_MENU_ITEMS_LOCATOR = (By.CSS_SELECTOR, '[data-testid=left-menu]')
    COMMERCE_CENTER_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-entityid=catalogs]')
    AUDIENCE_BTN = (By.CSS_SELECTOR, '[data-entityid=audience]')
    COMPANIES_BTN = (By.CSS_SELECTOR, '[data-entity=dashboardV2]')
