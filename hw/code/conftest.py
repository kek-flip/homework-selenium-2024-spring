from ui.fixtures import *
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://ads.vk.com/')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--feed-path', default='./hw/code/test-data/feed.csv')
    parser.addoption('--feed-url', default='https://bring-give.hb.ru-msk.vkcs.cloud/homework-selenium/feed.csv')


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

    feed_url = request.config.getoption('--feed-url')
    feed_path = request.config.getoption('--feed-path')

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
        'feed_url': feed_url,
        'feed_path': feed_path,
    }
