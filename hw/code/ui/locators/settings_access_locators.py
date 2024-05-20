from selenium.webdriver.common.by import By


class SettingsAccessLocators:
    ADD_CABINET_BTN_LOCATOR = (By.XPATH, f'//span[text()="Добавить кабинет"]')
    ID_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid="userid-input"]')
    SAVE_BTN_LOCATOR = (By.XPATH, f'//span[text()="Сохранить"]')
    WRONG_ID_ALERT_LOCATOR = (By.XPATH, f'//span[text()="Кабинета с таким ID не существует"]')
    ERROR = (By.CSS_SELECTOR, '[role="alert"]')
