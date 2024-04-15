from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import StellarBurgersLocators


class TestPartsTransfer:

    def test_fillings_transfer(self, open_profile):
        open_profile.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCT).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))
        open_profile.find_element(*StellarBurgersLocators.FILLINGS_BUTTON).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.FILLINGS_TITLE))
        fillings_title = open_profile.find_element(*StellarBurgersLocators.FILLINGS_TITLE).text
        assert 'Начинки' in fillings_title, 'Wrong transfer in Fillings'

    def test_souses_transfer(self, open_profile):
        open_profile.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCT).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))
        open_profile.find_element(*StellarBurgersLocators.SOUSES_BUTTON).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.SOUSES_TITLE))
        souses_title = open_profile.find_element(*StellarBurgersLocators.SOUSES_TITLE).text
        assert 'Соусы' in souses_title, 'Wrong transfer in Fillings'

    def test_buns_transfer(self, open_profile):
        open_profile.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCT).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))
        open_profile.find_element(*StellarBurgersLocators.FILLINGS_BUTTON).click()
        open_profile.find_element(*StellarBurgersLocators.BUNS_BUTTON).click()
        WebDriverWait(open_profile, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.BUNS_TITLE))
        buns_title = open_profile.find_element(*StellarBurgersLocators.BUNS_TITLE).text
        assert 'Булки' in buns_title, 'Wrong transfer in Fillings'
