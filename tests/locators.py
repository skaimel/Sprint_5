from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REGISTRATION_INPUT_NAME = (By.XPATH, ".//label[text()='Имя']/../input")  # Регистрация поле Имя
    REGISTRATION_INPUT_EMAIL = (By.XPATH, ".//label[text()='Email']/../input")  # Регистрация поле Email
    REGISTRATION_INPUT_PASSWORD = (By.XPATH, ".//input[@type='password']")  # Регистрация поле Пароль
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка Зарегистрироваться
    INCORRECT_PASSWORD_ERROR = \
        (By.XPATH, ".//p[contains(@class, 'input__error text') and text()='Некорректный пароль']")
    # Надпись некорректный пароль при регистрации
    LOGIN = (By.XPATH, ".//a[@href='/login']")  # Ссылка на Вход со страницы регистрации и восстановления пароля


class AutorizationPageLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text() = 'Вход']")  # Текст "Вход" на странице авторизации
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name = 'name']")  # Поле Email
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']")  # Поле Пароль
    LOGIN_SUBMIT = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти"
    REGISTER = (By.XPATH, ".//a[@href='/register']")  # Зарегистрироваться
    RESTORE_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")  # Восстановить пароль


class ConstructorLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет"
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    HEADING_IN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")  # Заголовок главной страницы "Соберите бургер"
    NAME_BUTTON_SECTION_BREAD = (By.XPATH, "//span[text() = 'Булки']")  # Кнопка "Булки" для перехода к булкам
    NAME_BUTTON_SECTION_SAUCES = (By.XPATH, "//span[text() = 'Соусы']")  # Кнопка "Соусы" для перехода к соусам
    NAME_BUTTON_SECTION_TOPPING = (By.XPATH, "//span[text() = 'Начинки']")  # Кнопка "Начинки" для перехода к начинкам
    SECTION_BREAD = (By.XPATH, "//h2[text() = 'Булки']")  # Текст раздела "Булки"
    SECTION_SAUCES = (By.XPATH, "//h2[text() = 'Соусы']")  # Текст раздела "Соусы"
    SECTION_TOPPING = (By.XPATH, "//h2[text() = 'Начинки']")  # Текст раздела "Начинки"
    ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']") # Кнопка Оформить заказ


class ForgotPasswordLocators:
    LINK_TO_LOGIN_PAGE = (By.XPATH, "//a[@href = '/login']")  # Ссылка "Войти" на страницу авторизации


class ProfilePageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в хедере
    LINK_PROFILE = (By.XPATH, "//a[@href='/account/profile']")  # Кнопка Профиль в личном кабинете
    LINK_CONSTRUCTOR = (By.XPATH, "//li/a[@href = '/']")  # Кнопка Конструктор
    LINK_LOGO = (By.XPATH, "//div/a[@href = '/']")  # Логотип сайта
    BUTTON_LOG_OUT = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка Выход
