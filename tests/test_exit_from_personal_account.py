from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorizationPageLocators, ProfilePageLocators
from user_data import UserData
from urls import Url
from conftest import get_driver


class TestExit:
    def test_exit(self, get_driver):
        WebDriverWait(get_driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.LOGIN_SUBMIT))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys(UserData.current_user.get(
            'email'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(UserData.current_user.get(
            'password'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.BUTTON_LOG_OUT))
        get_driver.find_element(*ProfilePageLocators.BUTTON_LOG_OUT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(AutorizationPageLocators.LOGIN_SUBMIT))
        assert Url.login_page == get_driver.current_url
