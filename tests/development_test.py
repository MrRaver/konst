import time

from pages.development_page import Test_Development
from tests.base_test import BaseTest

class TestDevelopment(BaseTest):

    def test_create_DHTML(self, driver): # 1.Создание DHTML страниц
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.create_DHTML()
        time.sleep(4)

    def test_edit_DHTML(self,driver):  # 2.Редактирование DHTML
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.create_DHTML()
        time.sleep(4)
    def test_delete_DHTML(self,driver):  # 3.Удаление DHTML
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.delete_DHTML()
        time.sleep(4)

    def test_filter_additional(self, driver): # 30.Проверка отображения
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.table_reports()
        time.sleep(4)