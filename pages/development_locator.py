from pages.base_page import BasePage
from locators.development_locator import Reports as dev


class Test_Development(BasePage):
    def table_reports(self):
        self.autorization()
        self.element_is_visible(dev.DEVELOPMENT).click()
        self.element_is_visible(dev.REPORTS).click()
        self.element_is_visible(dev.REPORTS_FIRST).click()

