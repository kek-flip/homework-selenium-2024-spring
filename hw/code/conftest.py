from ui.fixtures import *
from dotenv import load_dotenv
from os import environ


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://ads.vk.com/')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    load_dotenv()
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    feed_url = environ.get("FEED_URL", "https://bring-give.hb.ru-msk.vkcs.cloud/homework-selenium/feed.csv")  
    feed_path = environ.get("FEED_PATH", "./test-data/feed.csv")
    users_list_path = environ.get("USERS_LIST_PATH", "./test-data/emails.txt")
    keywords_path = environ.get("KEYWORDS_PATH", "./test-data/keywords.txt")
    breakwords_path = environ.get("BREAKWORDS_PATH", "./test-data/breakwords.txt")

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
        'feed_url': feed_url,
        'feed_path': feed_path,
        'users_list_path': users_list_path,
        'keywords_path': keywords_path,
        'breakwords_path': breakwords_path,
    }
