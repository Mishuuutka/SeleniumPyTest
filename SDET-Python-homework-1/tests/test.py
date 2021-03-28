import pytest
from ui.locators import basic_locators
from base import BaseCase
import time


class TestMyTarget(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        self.find(basic_locators.DASHBOARD_TITLE)

    @pytest.mark.UI
    def test_logout(self):
        self.logout()
        self.find(basic_locators.SIGN_BUTTON)

    @pytest.mark.UI
    def test_profile(self):
        self.login()
        self.click(basic_locators.PROFILE_LINK)
        fio = self.find(basic_locators.PROFILE_FIO)
        phone = self.find(basic_locators.PROFILE_PHONE)
        email = self.find(basic_locators.PROFILE_EMAIL)
        self.input_key(basic_locators.PROFILE_FIO, 'Иван Иван Иванович')
        self.input_key(basic_locators.PROFILE_PHONE, '8912345678901')
        self.input_key(basic_locators.PROFILE_EMAIL, 'ivanov123456@mail.ru')
        self.click(basic_locators.PROFILE_BUTTON)
        self.driver.refresh()
        assert fio != self.find(basic_locators.PROFILE_FIO)\
               and phone != self.find(basic_locators.PROFILE_PHONE)\
               and email != self.find(basic_locators.PROFILE_EMAIL)
        self.logout()

    @pytest.mark.parametrize("locators, check",
                             [(basic_locators.MENU_BALANCE, basic_locators.BALANCE_LOCATOR),
                              (basic_locators.MENU_AUDIT, basic_locators.AUDIT_LOCATOR)])
    @pytest.mark.UI
    def test_menu(self, locators, check):
        self.login()
        time.sleep(1)
        self.click(locators)
        self.find(check)
        self.logout()

