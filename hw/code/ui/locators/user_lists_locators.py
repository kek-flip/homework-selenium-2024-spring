from selenium.webdriver.common.by import By


class UserListsLocators:
    ADD_LIST_BTN_LOCATOR = (By.XPATH, f'//span[text()="Загрузить список"]')
    ADD_LIST_MODAL_LOCATOR = (By.CLASS_NAME, "ModalSidebarPage_container__Zopae")
    LOAD_LIST_LOCATOR = (By.CSS_SELECTOR, '[data-testid="other-buttons"]')
    ACTIVATE_LIST_LOCATOR = (By.XPATH, f".//*[text()='Активировать внешний список пользователей']")
    KEY_INPUT_LOCATOR = (By.CSS_SELECTOR, '[placeholder="Введите ключ"]')
    ACTIVATE_BTN_LOCATOR = (By.XPATH, f".//*[text()='Активировать']")
    WRONG_KEY_ALERT_LOCATOR = (By.XPATH, f'//span[text()="Ключ не найден"]')
    SEARCH_LOCATOR = (By.CSS_SELECTOR, '[placeholder="Поиск"]')
    NOTHING_LOCATOR = (By.XPATH, f".//*[text()='Ничего не нашлось']")
