from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq?ref=main_landing"]')
    MAIL_RU_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id=oAuthService_mail_ru]')
    USERNAME_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=username]')
    NEXT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id=next-button]')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=password]')
    SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id=submit-button]')
    NOT_ACTIVE_BULLET_LOCATOR = (By.XPATH, "//div[contains(@class, 'Bullets_box') and not(contains(@class, 'Active'))]")
    REGISTER_BTN_LOCATOR = (By.LINK_TEXT, "Зарегистрироваться")
    SHOW_ALL_LINK_LOCATOR = (By.LINK_TEXT, "Смотреть все")
    CASE_IMAGE_LOCATOR = (By.XPATH, "//*[contains(@class, 'Case_imageWrapper__')]")
    DETAILED_BTN_LOCATOR = (By.LINK_TEXT, "Подробнее")
    WEBINAR_BANNER_LOCATOR = (By.CLASS_NAME, "GetStarted_wrapper__cTNLj")
    NEWS_BANNER_LOCATOR = (By.CLASS_NAME, "News_cols__L6uYy")

