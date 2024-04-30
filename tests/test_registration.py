from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import RegistrationPageLocators, AutorizationPageLocators, ProfilePageLocators
from User_data import UserData


class TestRegistration:
    def test_success_registration(self, get_driver):
        WebDriverWait(get_driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.REGISTER))
        get_driver.find_element(*AutorizationPageLocators.REGISTER).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BUTTON))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_INPUT_NAME).send_keys(UserData.new_user.get(
            'name'))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_INPUT_EMAIL).send_keys(UserData.new_user.get(
            'email'))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_INPUT_PASSWORD).send_keys(UserData.new_user.get(
            'password'))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.LOGIN_SUBMIT))
        assert get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).text == 'Войти'

    def test_registration_with_short_password(self, get_driver):
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.REGISTER))
        get_driver.find_element(*AutorizationPageLocators.REGISTER).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BUTTON))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_INPUT_NAME).send_keys(UserData.new_user.get(
            'name'))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_INPUT_EMAIL).send_keys(UserData.new_user.get(
            'email'))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_INPUT_PASSWORD).send_keys(
            UserData.new_user_short_password.get('password'))
        get_driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.INCORRECT_PASSWORD_ERROR))
        assert get_driver.find_element(*RegistrationPageLocators.INCORRECT_PASSWORD_ERROR).text == 'Некорректный пароль'
