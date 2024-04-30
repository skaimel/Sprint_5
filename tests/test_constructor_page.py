from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import ConstructorLocators

class TestConstructor:
    def test_go_to_section_bread(self, get_driver):
        WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.NAME_BUTTON_SECTION_SAUCES))
        get_driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_SAUCES).click()
        WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.NAME_BUTTON_SECTION_BREAD))
        get_driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_BREAD).click()
        WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.SECTION_BREAD))
        section_text = get_driver.find_element(*ConstructorLocators.SECTION_BREAD).text
        assert section_text == 'Булки'

    def test_go_to_section_sauces(self, get_driver):
        WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.NAME_BUTTON_SECTION_SAUCES))
        get_driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_SAUCES).click()
        WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.SECTION_SAUCES))
        section_text = get_driver.find_element(*ConstructorLocators.SECTION_SAUCES).text
        assert section_text == 'Соусы'

    def test_go_to_section_toppings(self, get_driver):
        WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.NAME_BUTTON_SECTION_TOPPING))
        get_driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_TOPPING).click()
        WebDriverWait(get_driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.SECTION_TOPPING))
        section_text = get_driver.find_element(*ConstructorLocators.SECTION_TOPPING).text
        assert section_text == 'Начинки'