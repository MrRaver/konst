import time

from pages.development_page import Test_Development
from tests.base_test import BaseTest

class TestDevelopment(BaseTest):
    def test_create_DHTML(self, driver): # 1.Создание DHTML страниц
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.create_DHTML()

    def test_edit_DHTML(self,driver):  # 2.Редактирование DHTML
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.edit_DHTML()
    def test_delete_DHTML(self,driver):  # 3.Удаление DHTML
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.delete_DHTML()

    def test_create_actions_string(self,driver):  # 4 Действия над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_actions_string()

    def test_create_right_on_string(self,driver):  # 5.Создание команд над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_right_on_string()

    def test_edit_actions_string(self,driver):  # 6 Редактировнаие действия над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_actions_string()

    def test_delete_actions_string(self,driver):  # 7.удаление действия над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_actions_string()

    def test_create_js_trigger(self,driver):  # 8.создание js триггера
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_js_trigger()
    def test_edit_js_trigger(self,driver):  # 9 редактирование js тригера
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_js_trigger()
    def test_delete_js_trigger(self,driver):  # 10 удаление js тригера
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_js_trigger()
    def test_create_dynamic_API(self, driver): # 11 Добавление динамического API
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.create_dynamic_API()


    def test_filter_additional(self, driver): # 30.Проверка отображения
        dev = Test_Development(driver, self.main_url()+self.login_url())
        dev.open()
        dev.table_reports()

