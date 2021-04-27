import pytest
from ui.locators import basic_locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseCase:
    driver = None
    config = None

    BASE_TIMEOUT = 5

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = self.BASE_TIMEOUT
        return WebDriverWait(self.driver, timeout)

    def click(self, locator, timeout=None):
        click = self.find(locator, timeout)
        click = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        click.click()

    def input_key(self, locator, key, enter=False):
        input_key = self.find(locator)
        input_key.clear()
        input_key.send_keys(key)
        if enter:
            input_key.send_keys(Keys.ENTER)

    @pytest.fixture(scope='function')
    def logined_browser(self):
        self.click(basic_locators.SIGN_BUTTON)
        self.input_key(basic_locators.SIGN_EMAIL, 'mishuuuutka@gmail.com')
        self.input_key(basic_locators.SIGN_PASSWORD, 'qwerty1!', True)

    def logout(self):
        self.click(basic_locators.SESSION_TITLE, 15)
        time.sleep(1)
        self.click(basic_locators.LOGOUT_BUTTON, 15)






