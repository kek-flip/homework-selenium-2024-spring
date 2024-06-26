import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.pages.base_page import PageNotOpenedException


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            driver.get(MainPage.url)
            MainPage(driver).login(credentials)

    def is_url_open(self, url):
        timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def is_redirect_occurred(self, url):
        timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until_not(EC.url_matches(url))
            return True
        except:
           raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, гдеcurrent url {self.driver.current_url}')

class UnauthorizedCase:
    authorize = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

    def is_url_open(self, url):
        timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, гдеcurrent url {self.driver.current_url}')

    def is_redirect_occurred(self, url):
        timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until_not(EC.url_matches(url))
            return True
        except:
           raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, гдеcurrent url {self.driver.current_url}')


class NoCabinetCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        if self.authorize:
            no_cabinet_credentials = request.getfixturevalue('no_cabinet_credentials')
            driver.get(MainPage.url)
            MainPage(driver).login_no_cabinet(no_cabinet_credentials)

    def is_url_open(self, url):
        timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

