from selenium.webdriver.common.by import By


class NewsLocators:
    DETAILED_BTN_LOCATOR = (By.XPATH, f'//span[text()="Подробнее"]')
    NEWS_IMAGE_LOCATOR = (By.CLASS_NAME, "News_imageWrapper__5K0O4")
    TO_CABINET_BTN_LOCATOR = (By.XPATH, f'//span[text()="В кабинет"]')
    TO_NEWS_LOCATOR = (By.CLASS_NAME, "Summary_leftArrow__gcUOO")
