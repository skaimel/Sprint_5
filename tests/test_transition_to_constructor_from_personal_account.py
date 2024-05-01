from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorizationPageLocators, ProfilePageLocators, ConstructorLocators
from user_data import UserData
from conftest import get_driver


class TestTransitionConstructor:
    def test_transition_to_constructor_by_constructor(self, get_driver):
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys(UserData.current_user.get('email'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(
            UserData.current_user.get('password'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.LINK_CONSTRUCTOR))
        get_driver.find_element(*ProfilePageLocators.LINK_CONSTRUCTOR).click()
        assert get_driver.find_element(*ConstructorLocators.HEADING_IN_PAGE).text == 'Соберите бургер'

    def test_transition_to_constructor_by_logo(self, get_driver):
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys(UserData.current_user.get('email'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(
            UserData.current_user.get('password'))
        get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
        get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.LINK_LOGO))
        get_driver.find_element(*ProfilePageLocators.LINK_LOGO).click()
        assert get_driver.find_element(*ConstructorLocators.HEADING_IN_PAGE).text == 'Соберите бургер'
