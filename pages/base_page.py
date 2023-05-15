from datetime import date
import uuid

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.konstructor_locator import Autorization as au


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        self.autorization()
    def open2(self):
        self.driver.get(self.url)
        self.autorization_rc()

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self):
        self.driver.execute_script("argument[0].scrollView;")

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def context_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def autorization(self):
        self.element_is_visible(au.PERSONNEL_NUMBER).send_keys(self.login_admin())
        self.element_is_visible(au.PASSWORD).send_keys(self.password_admin())
        self.element_is_visible(au.BUTTON_ENTER).click()

    def login_admin(self):
        return "admin"
    def password_admin(self):
        return "admin"


    def autorization_rc(self):
        self.element_is_visible(au.PERSONNEL_NUMBER).send_keys(self.login_admin_rc())
        self.element_is_visible(au.PASSWORD).send_keys(self.password_admin_rc())
        self.element_is_visible(au.BUTTON_ENTER).click()

    def login_admin_rc(self):
        return "6669991"

    def password_admin_rc(self):
        return "Rhjrjlbk1988"
    def RandomName(self, name):
        return name + "_" + str(uuid.uuid4())
    def clear_text(self,firstrow):
        firstrow.send_keys(Keys.CONTROL + "a")
        firstrow.send_keys(Keys.DELETE)

