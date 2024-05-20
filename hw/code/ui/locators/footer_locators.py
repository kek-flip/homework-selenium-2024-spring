from selenium.webdriver.common.by import By

class FooterLocators:
    
    LOGOTIP_LOCATOR = (By.XPATH, '//a[contains(@class, "Footer_logo__")]')
    NEWS_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "/news")]')
    COOKIE_LOCATOR = (
        By.XPATH, '//*[contains(@class, "CookieBanner_button__")]')
    DOCUMENTS_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "/documents")]')
    BUISNESS_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "https://expert.vk.com/?utm_source=vk_ads_blog&utm_medium=futer")]')
    VKBUISNESS_LOCATOR = (
        By.XPATH, '//div[contains(@class, "Footer_controls__")]//a[contains(@href, "https://vk.company/ru/company/business/")]')
    VK_LOCATOR = (
        By.XPATH, '//div[contains(@class, "Footer_controls__")]//a[contains(@href, "https://vk.com/vk_ads")]')
    OK_LOCATOR = (
        By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[1]/a[2]')
    EN_LOCATOR = (
        By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[2]/div[1]/div/div/div/h5/div/span[1]')
    RU_LOCATOR = (
        By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[2]/div[1]/div/div/div/h5/div/span[2]')
    ABOUT_LOCATOR = (
        By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[2]/a/span')
    MONETIZATION_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "/partner")]')
    HELP_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "/help")]')
    CABINET_LOCATOR = (
        By.XPATH, "//div[contains(@class, 'layout_content__')]//a[contains(@class, 'ButtonCabinet_primary__')]")
    CASES_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "/cases")]')
    INSIGHTS_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "/insights")]')
    EVENTS_LOCATOR = (
        By.XPATH, '//ul[contains(@class, "Footer_items__")]//a[contains(@href, "/events")]')
    TELEGRAM_LOCATOR = (
        By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[1]/a[3]')
    LANGUAGE_LOCATOR = (
        By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[2]/div[1]/div')
    LANGUAGE_POPUP_LOCATOR = (
        By.XPATH, '//*[@id="classic-layout"]/div[2]/footer/div[2]/div/div[2]/div[1]/div/div/div')
