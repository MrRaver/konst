import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.other_locator import Other as other


class Others(BasePage):
    def catalog_data(self):
        self.element_is_present(other.ADMINIRIROVANIE).click()
        self.element_is_present(other.SELECT).click()
        self.element_is_present(other.CONTROL_DATA).click()
        self.element_is_present(other.SAVE).click()
    def message(self):
        self.element_is_present(other.MESSAGE).click()
        self.element_is_visible(other.ADD_MESSAGE).click()
        self.element_is_visible(other.USERS).click()
        self.element_is_visible(other.ADMIM).click()
        self.element_is_visible(other.USERS).click()
        self.element_is_visible(other.TITLE).send_keys("Тест 31.03.2023")
        self.element_is_visible(other.ROLES).click()
        self.element_is_visible(other.TEST_ROLE).click()
        self.element_is_visible(other.ROLES).click()
        self.element_is_visible(other.TEXT).send_keys("Текстовый текст")
        self.element_is_present(other.SITE).click()
        self.element_is_present(other.MAIL).click()
        self.element_is_visible(other.SEND).click()
    def import_dat(self):
        self.element_is_visible(other.IMPORT_DATA).click()
        self.element_is_visible(other.CHOICE_TABLE).click()
        names=self.element_is_visible(other.INPUT_CHOICE_TABLE)
        names.send_keys("Таблица 1 31.03.2023")
        names.send_keys(Keys.ENTER)
        path=rf'F:\konst\test.xlsx'
        self.element_is_not_visible(other.CHOICE_EX).send_keys(path)
        time.sleep(2)
        self.element_is_visible(other.IMPORT_BUTTON).click()
        return self.element_is_visible(other.TEXT_RESULT).text







