from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationPageLocators, AutorizationPageLocators, ProfilePageLocators, ConstructorLocators
from User_data import UserData


class TestAutorization:
    def test_login_from_button_in_main_page(self, get_driver):
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ConstructorLocators.BUTTON_LOG_IN_ACCOUNT))
        get_driver.find_element(*ConstructorLocators.BUTTON_LOG_IN_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.LOGIN_SUBMIT))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys((UserData.current_user.get(
            'email')))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys((UserData.current_user.get(
            'password')))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))
        assert get_driver.find_element(*ConstructorLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_from_personal_account(self, get_driver):
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys(UserData.current_user.get(
            'email'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(UserData.current_user.get(
            'password'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))
        assert get_driver.find_element(*ConstructorLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_from_registration_page(self, get_driver):
        WebDriverWait(get_driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.REGISTER))
        get_driver.find_element(*AutorizationPageLocators.REGISTER).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.LOGIN))
        get_driver.find_element(*RegistrationPageLocators.LOGIN).click()
        get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys(UserData.current_user.get(
            'email'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(UserData.current_user.get(
            'password'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))
        assert get_driver.find_element(*ConstructorLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_login_from_restore_password_page(self, get_driver):
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        (WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.RESTORE_PASSWORD)))
        get_driver.find_element(*AutorizationPageLocators.RESTORE_PASSWORD).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.LOGIN))
        get_driver.find_element(*RegistrationPageLocators.LOGIN).click()
        get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys(UserData.current_user.get(
            'email'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(UserData.current_user.get(
            'password'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))
        assert get_driver.find_element(*ConstructorLocators.ORDER_BUTTON).text == 'Оформить заказ'
