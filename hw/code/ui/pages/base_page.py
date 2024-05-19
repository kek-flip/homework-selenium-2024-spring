import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.keys import Keys

class PageNotOpenedExeption(Exception):
    pass


class element_in_viewport(object):
    def __init__(self, locator: tuple[str, str]):
        self.locator = locator

    def __call__(self, driver: RemoteWebDriver):
        script = """
                    var elem = arguments[0],
                    box = elem.getBoundingClientRect(),
                    cx = box.left + box.width / 2,
                    cy = box.top + box.height / 2,
                    e = document.elementFromPoint(cx, cy);
                    for (; e; e = e.parentElement) {
                    if (e === elem)
                      return true;
                    }
                    return false;
                """

        elem = driver.find_element(*self.locator)
        return driver.execute_script(script, elem)


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)
    
    def unfocus(self):
        self.driver.execute_script('document.activeElement.blur()')

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))
    
    def find_all(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    def find_from(self, parent, locator, timeout: float | None = None) -> WebElement:
        def wait_cond(_):
            elem = parent.find_element(*locator)
            if elem.is_displayed():
                return elem
            return False

        return self.wait(timeout).until(wait_cond)
    
    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def fill(self, locator, keys):
        self.find(locator).send_keys(keys)

    def scroll_click(self, locator, timeout=5) -> WebElement:
        elem = self.find(locator, timeout=timeout)

        self.wait(timeout).until(EC.visibility_of_element_located(locator))
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))

        elem.location_once_scrolled_into_view

        self.wait(timeout).until(element_in_viewport(locator))

        elem.click()

        return elem

    def is_visible(self, locator, timeout: float | None = None):
        try:
            elem = self.find(locator, timeout)
            elem.location_once_scrolled_into_view
            return True
        except:
            return False

    def is_not_visible(self, locator, timeout: float | None = None):
        try:
            self.wait(timeout).until(EC.invisibility_of_element(locator))
            return True
        except:
            return False

    def switch_to_new_tab(self):
        assert len(self.driver.window_handles) > 1
        self.driver.switch_to.window(self.driver.window_handles[1])

    def clear(self, locator, timeout: float | None = None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()

        if elem.get_attribute('value') != '':
            size = len(elem.get_attribute('value'))
            elem.send_keys(size * Keys.BACKSPACE)

        return elem

    def fill_in(self, locator, query: str, timeout: float | None = None) -> WebElement:
        elem = self.clear(locator, timeout)
        elem.send_keys(query)
        return elem

    def form_error(self, locator, error) -> WebElement:
        try:
            error_container = self.find(self.locators.ERROR)
            self.find_from(error_container, locator)
            error = self.find_from(
                error_container, self.locators.BY_TEXT(error))
            return error
        except TimeoutException:
            return None

    def wait_for_count_of_elements(self, locator, count, timeout: float | None = None):
        self.wait(timeout).until(lambda _: len(
            self.find_all(locator)) == count)
