from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import settings
from locators import StellarBurgersLocators


class TestPageTransfer:

    def test_profile_transfer(self, open_profile):
        current_profile_url = open_profile.current_url
        assert '/account/profile' in current_profile_url

    def test_constructor_transfer(self, open_profile):
        open_profile.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCT).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))
        current_profile_url = open_profile.current_url
        assert current_profile_url == settings.URL

    def test_logo_transfer(self, open_profile):
        open_profile.find_element(*StellarBurgersLocators.BUTTON_LOGO).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))
        current_profile_url = open_profile.current_url
        assert current_profile_url == settings.URL

    def test_account_exit(self, open_profile):
        open_profile.find_element(*StellarBurgersLocators.BUTTON_EXIT).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.BUTTON_FORGOT_PAS))
        current_profile_url = open_profile.current_url
        assert current_profile_url == settings.URL + 'login'
