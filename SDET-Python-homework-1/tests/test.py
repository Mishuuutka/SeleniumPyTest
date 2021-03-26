import pytest
from ui.locators import basic_locators
from base import BaseCase
import time


class TestMyTarget(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        self.find(basic_locators.LOGIN_TEST)

    @pytest.mark.UI
    def test_logout(self):
        self.logout()
        self.find(basic_locators.SIGN_BUTTON)

    @pytest.mark.UI
    def test_profile(self):
        self.login()
        self.click(basic_locators.PROFILE_TEST)
        self.input_key(basic_locators.PROFILE_FIO, 'Иванов Иван Иванович')
        self.input_key(basic_locators.PROFILE_PHONE, '8912345678901')
        self.input_key(basic_locators.PROFILE_EMAIL, 'ivanov123456@mail.ru')
        self.click(basic_locators.PROFILE_BUTTON)
        self.driver.refresh()
        self.find(basic_locators.PROFILE_SAVE)
        self.logout()

    @pytest.mark.parametrize("locators, check",
                             [(basic_locators.MENU_BALANCE, basic_locators.MENU_BALANCE_TEST),
                              (basic_locators.MENU_AUDIT, basic_locators.MENU_AUDIT_TEST)])
    @pytest.mark.UI
    def test_menu(self, locators, check):
        self.login()
        time.sleep(1)
        self.click(locators)
        self.find(check)
        self.logout()

