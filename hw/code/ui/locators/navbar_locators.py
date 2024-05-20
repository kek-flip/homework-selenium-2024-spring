from selenium.webdriver.common.by import By

class NavbarLocators:
    LOGOTIP_LOCATOR = (By.XPATH, "//*[contains(@class, 'HeaderLeft_left__')]")
    NEWS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/news"]')
    FORUM_LOCATOR = (By.CSS_SELECTOR, 'a[href="/upvote"]')
    MONETIZATION_LOCATOR = (By.CSS_SELECTOR, 'a[href="/partner"]')
    HELP_LOCATOR = (By.CSS_SELECTOR, 'a[href="/help"]')
    CABINET_LOCATOR = (By.XPATH, "//*[contains(@class, 'ButtonCabinet_primary__')]")
    CASES_LOCATOR = (By.CSS_SELECTOR, 'a[href="/cases"]')
    INSIGHTS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/insights"]')
    ONBOARDING_LOCATOR = (By.XPATH, "//*[contains(@class, 'NavigationVKAdsItem_item__')]")
    EVENTS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/events"]')
    COURSES_LOCATOR = (By.CSS_SELECTOR, 'a[href="https://expert.vk.com/catalog/courses/"]')
    CERTIFICATION_LOCATOR = (By.CSS_SELECTOR, 'a[href="https://expert.vk.com/certification/"]')

