from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REGISTRATION_SUBMIT = (By.XPATH, ".//h2[text() = 'Вход']")
    REGISTRATION_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']//following-sibling::input")

    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    LOGIN_BUTTON_PROFILE = (By.XPATH, ".//a[@href='/account']")
    LOGIN_BUTTON_REG_FORM = (By.XPATH, ".//a[@href='/login']")

    LOGIN_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']//following-sibling::input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    LOGIN_BUTTON_SUBMIT = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_EXPECTED_TEXT = (By.XPATH, ".//button[text()='Оформить заказ']")

    BUTTON_FORGOT_PAS = (By.XPATH, ".//a[@href='/forgot-password']")
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
    BUTTON_CONSTRUCT = (By.XPATH, ".//p[text()='Конструктор']")
    BUTTON_LOGO = (By.XPATH, ".//nav/div/a")

    ERROR_VALIDATION_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")

    FILLINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")
    FILLINGS_TITLE = (By.XPATH, ".//h2[text()='Начинки']")
    SOUSES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")
    SOUSES_TITLE = (By.XPATH, ".//h2[text()='Соусы']")
    BUNS_BUTTON = (By.XPATH, ".//span[text()='Булки']")
    BUNS_TITLE = (By.XPATH, ".//h2[text()='Булки']")
