from selenium.webdriver.common.by import By

# ТЕСТ ЛОГИНА
SIGN_BUTTON = (By.XPATH, "//div[text()='Войти']")
SIGN_EMAIL = (By.NAME, 'email')
SIGN_PASSWORD = (By.NAME, 'password')

# ТЕСТ ЛОГАУТА
LOGIN_TEST = (By.XPATH, "//div[contains(@class, 'instruction-module-title') and contains(text(), 'С чего начать?')]")
LOGOUT_TEST = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'rightMenu-module-rightMenuLink') and text()='Выйти']")

# ТЕСТ НА РЕДАКТИРОВАНИЕ ПРОФИЛЯ
PROFILE_TEST = (By.XPATH, "//a[@data-gtm-id='pageview_profile']")
PROFILE_FIO = (By.XPATH, "//div[@data-name='fio']/div/input")
PROFILE_PHONE = (By.XPATH, "//div[@data-name='phone']/div/input")
PROFILE_EMAIL = (By.XPATH, "//div[contains(@class, 'js-additional-email profile__list__row__input')]/div/div/input")
PROFILE_BUTTON = (By.XPATH, "//button[@data-class-name='Submit']")
PROFILE_SAVE = (By.XPATH, "//div[@title='Иванов Иван Иванович']")

# ТЕСТ МЕНЮ
MENU_BALANCE = (By.XPATH, "//a[@data-gtm-id='pageview_billing']")
MENU_BALANCE_TEST = (By.CLASS_NAME, "deposit__payment-form__title")
MENU_AUDIT = (By.XPATH, "//a[text()='Аудитории']")
MENU_AUDIT_TEST = (By.XPATH, "//span[text()='Аудиторные сегменты']")