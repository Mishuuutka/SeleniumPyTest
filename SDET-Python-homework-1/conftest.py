import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


@pytest.fixture(scope='session')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(
        executable_path='')
    browser.get(url)
    browser.set_window_size(1280, 720)
    yield browser
    browser.close()
