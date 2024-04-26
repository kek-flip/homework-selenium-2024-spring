from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, "a[href='/hq?ref=main_landing']")
    MAIL_RU_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id=oAuthService_mail_ru]')
    USERNAME_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=username]')
    NEXT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id=next-button]')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=password]')
    SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id=submit-button]')