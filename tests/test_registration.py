import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import settings
from data import BurgerTestData
from locators import StellarBurgersLocators


class TestStellarBurgerRegistration:

    def test_registration(self, driver):
        name = 'Sergey'
        email = ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@yandex.ru'
        password = '111111'

        driver.get(settings.URL + "register")
        name_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT)
        name_input.send_keys(name)

        email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(password)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.BUTTON_FORGOT_PAS))

        email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = (driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT))
        password_input.send_keys(password)

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_SUBMIT).click()
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))

        profile_name = driver.find_element(*StellarBurgersLocators.LOGIN_EXPECTED_TEXT)

        assert profile_name.is_displayed() and profile_name.text == BurgerTestData.ORDER, 'Registration Failed'

    def test_registration_wrong_password(self, driver):
        name = 'Sergey'
        email = ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@yandex.ru'
        password = '11111'

        driver.get(settings.URL + "register")
        name_input = driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT)
        name_input.send_keys(name)

        email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(password)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located(StellarBurgersLocators.ERROR_VALIDATION_PASSWORD))

        current_url = driver.current_url

        assert 'login' not in current_url, 'Failed password'


