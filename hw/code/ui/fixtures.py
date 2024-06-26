import pytest

from os import environ

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.overview_page import OverviewPage
from ui.pages.commerce_center_page import CommerceCenterPage
from ui.pages.main_page import MainPage
from ui.pages.cabinet import CabinetPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.news_page import NewsPage
from ui.pages.navbar_page import NavbarPage
from ui.pages.footer_page import FooterPage
from ui.pages.education_page import EducationPage
from ui.pages.forum_page import ForumPage
from ui.pages.settings_page import SettingsPage
from ui.pages.company_page import CompanyPage
from ui.pages.audience_page import AudiencePage

@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def credentials():
    return (environ.get("LOGIN", "Test"), environ.get("PASSWORD", "Test"))

@pytest.fixture(scope='session')
def no_cabinet_credentials():
    return (environ.get("NO_CABINET_LOGIN", "Test"), environ.get("NO_CABINET_PASSWORD", "Test"))

# -------Pages--------

@pytest.fixture()
def main_page(driver):
    driver.get(MainPage.url)
    return MainPage(driver)

@pytest.fixture()
def overview_page(driver):
    driver.get(OverviewPage.url)
    return OverviewPage(driver)

@pytest.fixture()
def commerce_center_page(driver):
    driver.get(CommerceCenterPage.url)
    return CommerceCenterPage(driver)

@pytest.fixture()
def cabinet_page(driver):
    driver.get(CabinetPage.url)
    return CabinetPage(driver)

@pytest.fixture()
def registration_page(driver):
    driver.get(RegistrationPage.url)
    return RegistrationPage(driver)

@pytest.fixture()
def news_page(driver):
    driver.get(NewsPage.url)
    return NewsPage(driver)

@pytest.fixture()
def navbar_page(driver):
    driver.get(NavbarPage.url)
    return NavbarPage(driver)

@pytest.fixture()
def footer_page(driver):
    driver.get(FooterPage.url)
    return FooterPage(driver)

@pytest.fixture()
def education_page(driver):
    driver.get(EducationPage.url)
    return EducationPage(driver)
def forum_page(driver):
    driver.get(ForumPage.url)
    return ForumPage(driver)

@pytest.fixture()
def settings_page(driver):
    driver.get(SettingsPage.url)
    return SettingsPage(driver)

@pytest.fixture()
def company_page(driver):
    driver.get(CompanyPage.url)
    return CompanyPage(driver)

@pytest.fixture()
def audience_page(driver):
    driver.get(AudiencePage.url)
    return AudiencePage(driver)
