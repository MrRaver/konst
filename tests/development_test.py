import time

from pages.development_page import Test_Development
from tests.base_test import BaseTest


class TestDevelopment(BaseTest):
    def test_create_DHTML(self, driver):  # 1.Создание DHTML страниц
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_DHTML()

    def test_edit_DHTML(self, driver):  # 2.Редактирование DHTML
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_DHTML()

    def test_delete_DHTML(self, driver):  # 3.Удаление DHTML
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_DHTML()

    def test_create_actions_string(self, driver):  # 4 Действия над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_actions_string()

    def test_create_right_on_string(self, driver):  # 5.Создание команд над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_right_on_string()
        time.sleep(15)

    def test_edit_actions_string(self, driver):  # 6 Редактировнаие действия над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_actions_string()

    def test_delete_actions_string(self, driver):  # 7.удаление действия над строками
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_actions_string()

    def test_create_js_trigger(self, driver):  # 8.создание js триггера
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_js_trigger()

    def test_edit_js_trigger(self, driver):  # 9 редактирование js тригера
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_js_trigger()

    def test_delete_js_trigger(self, driver):  # 10 удаление js тригера
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_js_trigger()

    def test_create_dynamic_API(self, driver):  # 11 Добавление динамического API
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_dynamic_API()

    def test_edit_dynamic_API(self, driver):  # 12 редактирование динамического API
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_dynamic_API()

    def test_delete_dynamic_API(self, driver):  # 13 удаление динамического API
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_dynamic_API()

    """Не работает def test_create_tasks(self, driver):  # 14  создания задания
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_tasks()

     Не работает def edit_create_tasks(self, driver):  # 15  редактирования задания
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_tasks()

     Не работает def delete_create_tasks(self, driver):  # 16  удаление задания
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_tasks()
        """

    def test_create_server_function(self, driver):  # 17 создание серверной функции
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_server_function()

    def test_edit_server_function(self, driver):  # 18 редактирование серверной функции
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_server_function()

    def test_delete_server_function(self, driver):  # 19 удаление серверной функции
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_server_function()

        """
    # Не работает  def test_create_sample_cell(self, driver):  # 20 создании ячейки шаблона
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.create_sample_cell()
        time.sleep(12)

    # Не работаетdef test_edit_sample_cell(self, driver):  # 21 редактирование ячейки шаблона
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.edit_sample_cell()

    # Не работаетdef test_delete_sample_cell(self, driver):  # 23 удаление ячейки шаблона
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.delete_sample_cell()

    # Не работает def test_table_reports(self, driver):  # 25. создания отчета
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.table_reports()

"""
    def test_check_reports(self, driver):  # 26 проверка просмотра и скачивания
        dev = Test_Development(driver, self.main_url() + self.login_url())
        dev.open()
        dev.check_reports()
        time.sleep(2)
