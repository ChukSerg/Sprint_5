import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import settings
from data import BurgerTestData
from locators import StellarBurgersLocators


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def open_profile(driver):
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_PROFILE).click()

    email_input = driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT)
    email_input.send_keys(BurgerTestData.AUTH_EMAIL)
    password_input = (driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT))
    password_input.send_keys(BurgerTestData.AUTH_PASSWORD)
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_SUBMIT).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(StellarBurgersLocators.LOGIN_EXPECTED_TEXT))
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_PROFILE).click()
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located(StellarBurgersLocators.BUTTON_EXIT))
    return driver
