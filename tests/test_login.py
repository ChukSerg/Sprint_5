from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators import StellarBurgersLocators
from data import BurgerTestData
import settings


class TestBurgersLogin:

    def test_login_main_page(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()

        email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(BurgerTestData.AUTH_EMAIL)
        password_input = (driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT))
        password_input.send_keys(BurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_SUBMIT).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))

        profile_name = driver.find_element(*StellarBurgersLocators.LOGIN_EXPECTED_TEXT)

        assert profile_name.is_displayed() and profile_name.text == BurgerTestData.ORDER, 'Login Failed'

    def test_login_page_profile(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_PROFILE).click()

        email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(BurgerTestData.AUTH_EMAIL)
        password_input = (driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT))
        password_input.send_keys(BurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_SUBMIT).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))

        profile_name = driver.find_element(*StellarBurgersLocators.LOGIN_EXPECTED_TEXT)

        assert profile_name.is_displayed() and profile_name.text == BurgerTestData.ORDER, 'Login Failed'

    def test_login_registration_form(self, driver):
        driver.get(settings.URL + "register")
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REG_FORM).click()

        email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(BurgerTestData.AUTH_EMAIL)
        password_input = (driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT))
        password_input.send_keys(BurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_SUBMIT).click()
        WebDriverWait(driver, 15).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))

        profile_name = driver.find_element(*StellarBurgersLocators.LOGIN_EXPECTED_TEXT)

        assert profile_name.is_displayed() and profile_name.text == BurgerTestData.ORDER, 'Login Failed'

    def test_login_recovery_form(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_FORGOT_PAS).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REG_FORM).click()

        email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(BurgerTestData.AUTH_EMAIL)
        password_input = (driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT))
        password_input.send_keys(BurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_SUBMIT).click()
        WebDriverWait(driver, 15).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))

        profile_name = driver.find_element(*StellarBurgersLocators.LOGIN_EXPECTED_TEXT)

        assert profile_name.is_displayed() and profile_name.text == BurgerTestData.ORDER, 'Login Failed'

