import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.main_page import MainPage

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.main_page = MainPage(driver)
        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            self.overview_page = self.main_page.login(credentials)

