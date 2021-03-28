import pytest
from ui.locators import basic_locators
from base import BaseCase
import time


class TestMyTarget(BaseCase):

    @pytest.mark.UI
    def test_login(self, logined_browser):
        self.find(basic_locators.DASHBOARD_TITLE)

    @pytest.mark.UI
    def test_logout(self):
        self.logout()
        self.find(basic_locators.SIGN_BUTTON)

    @pytest.mark.UI
    def test_profile(self, logined_browser):
        self.click(basic_locators.PROFILE_LINK)
        fio = 'Иван Иван Иванович'
        phone = '8912345678901'
        email = 'ivanov123456@mail.ru'
        self.input_key(basic_locators.PROFILE_FIO, fio)
        self.input_key(basic_locators.PROFILE_PHONE, phone)
        self.input_key(basic_locators.PROFILE_EMAIL, email)
        self.click(basic_locators.PROFILE_BUTTON)
        self.driver.refresh()
        assert fio == self.find(basic_locators.PROFILE_FIO).get_attribute('value')\
               and phone == self.find(basic_locators.PROFILE_PHONE).get_attribute('value')\
               and email == self.find(basic_locators.PROFILE_EMAIL).get_attribute('value')
        self.logout()

    @pytest.mark.parametrize("locators, check",
                             [(basic_locators.MENU_BALANCE, basic_locators.BALANCE_LOCATOR),
                              (basic_locators.MENU_AUDIT, basic_locators.AUDIT_LOCATOR)])
    @pytest.mark.UI
    def test_menu(self, locators, check, logined_browser):
        time.sleep(1)
        self.click(locators)
        self.find(check)
        self.logout()


