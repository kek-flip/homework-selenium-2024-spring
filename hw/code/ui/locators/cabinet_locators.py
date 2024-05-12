from selenium.webdriver.common.by import By


class CabinetLocators:
    CAMPAIGN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/dashboard"]')
    AUDIENCE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/audience"]')
    BUDGET_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/budget"]')
    EDUCATION_LOCATOR = (By.CSS_SELECTOR, '[data-testid="onboarding-button"]')
    EDUCATION_MODAL_LOCATOR = (By.CLASS_NAME, 'vkuiModalPage__in')
    EDUCATION_MODAL_CROSS_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Закрыть"]')
    COMMERCE_CENTRE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/ecomm/catalogs"]')
    SITES_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/pixels"]')
    APPS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/apps"]')
    LEAD_FORM_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/leadads"]')
    SETTINGS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/settings"]')
    HELP_LOCATOR = (By.XPATH,  "//*[contains(@class, 'Hint_hintTrigger__ixYRu sidebar_portalMenuTrigger__vwcrf')]")
    HELP_MODAL_LOCATOR = (By.CLASS_NAME, 'Tooltip_tooltipContainer__P1b-O')
    CASES_LOCATOR = (By.LINK_TEXT, "Кейсы компаний")
    SPRAVKA_LOCATOR = (By.LINK_TEXT, "Справка")
    FORUM_LOCATOR = (By.LINK_TEXT, "Форум идей")
    QUESTION_LOCATOR = (By.XPATH, f'//span[text()="Задать вопрос"]')
    MESSENGER_LOCATOR = (By.CLASS_NAME, 'SAKWindow SAKWindow--opened')
    LOGO_LOCATOR = (By.CLASS_NAME, 'header_left__cv9bp')
    ACCOUNT_LOCATOR = (By.CLASS_NAME, 'AccountSwitch_changeAccountButton__o5T9V')
    ACCOUNT_MODAL_LOCATOR = (By.CLASS_NAME, 'AccountSwitch_accountsDropdown__4uPNG')
    ALL_CABINETS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/settings/access"]')
    BALANCE_LOCATOR = (By.CLASS_NAME, 'balance_balanceText__oDLjF')
    BALANCE_MODAL_LOCATOR = (By.CLASS_NAME, 'ModalManagerPage_modalContent__ybbav')
    NOTIFICATION_LOCATOR = (By.CLASS_NAME, 'BellNotificationsButton_icon__ER9KV')
    NOTIFICATION_MODAL_LOCATOR = (By.CLASS_NAME, 'BellNotificationsContent_cardContent__Hkz1H')
    PROFILE_LOCATOR = (By.CLASS_NAME, 'userMenu_avatar__oCUFq')
    PROFILE_MODAL_LOCATOR = (By.CLASS_NAME, 'userMenu_menu__RBqWO')
    LOGOUT_LOCATOR = (By.CLASS_NAME, 'userMenu_logoutButton__6MkNF')



