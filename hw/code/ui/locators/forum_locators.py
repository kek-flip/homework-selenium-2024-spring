from selenium.webdriver.common.by import By


class ForumLocators:
    SEARCH_FIELD = (By.XPATH, "//input[contains(@class, 'vkuiSearch__input')]")
    IDEAS_COUNT = (By.XPATH, "//div[contains(@class, 'Idea_cardVote__')]")

    IDEA_THEME_SELECT = (
        By.XPATH, "(//div[contains(@class, 'vkuiSelect__container')])[1]")
    IDEA_STATUS_SELECT = (
        By.XPATH, "(//div[contains(@class, 'vkuiSelect__container')])[2]")

    IDEA_TITLE = (By.XPATH, "//*[contains(@class, 'Idea_title__')]")

    @staticmethod
    def IDEA_LINK(title: str):
        return (By.XPATH, f"//a[contains(@class, 'Idea_title__')][text()='{title}']")
    @staticmethod
    def VK_UI_SELECT_ELEM(text):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']")
