from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import AutorizationPageLocators, ProfilePageLocators
from User_data import UserData
from URLs import URL


def test_go_to_personal_account_page(get_driver):
    WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
    get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
    get_driver.find_element(*AutorizationPageLocators.LOGIN_EMAIL_INPUT).send_keys(UserData.current_user.get('email'))
    get_driver.find_element(*AutorizationPageLocators.LOGIN_PASSWORD_INPUT).send_keys(UserData.current_user.get(
        'password'))
    get_driver.find_element(*AutorizationPageLocators.LOGIN_SUBMIT).click()
    WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PERSONAL_ACCOUNT))
    get_driver.find_element(*ProfilePageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(get_driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.BUTTON_LOG_OUT))
    assert URL.profile_page == get_driver.current_url
