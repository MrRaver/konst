import time

from pages.konstructor_condition_page import Test_Konstructors_Condition
from tests.base_test import BaseTest

class TestConditionKonstructors(BaseTest):
    def test_create_folder(self,driver): # 1.Предварительная подготовка
        cond=Test_Konstructors_Condition(driver,self.main_url()+self.login_url())
        cond.open()
        cond.create_table_test1()


    def test_konstructor_condition_save(self,driver): # 2.Конструктор условий. Сохранение
        cond=Test_Konstructors_Condition(driver,self.main_url()+self.login_url())
        cond.open()
        cond.konstructor_condition_save()

    def test_konstructor_condition_edit(self,driver): # 3.Конструктор условий. Редактирование
        cond=Test_Konstructors_Condition(driver,self.main_url()+self.login_url())
        cond.open()
        cond.konstructor_condition_edit()
    def test_konstructor_condition_status(self,driver): # #4.Конструктор условий. Перевод в статусы
        cond=Test_Konstructors_Condition(driver,self.main_url()+self.login_url())
        cond.open()
        cond.konstructor_condition_status()

    def test_konstructor_condition_filter_directory(self, driver):  #5.Конструктор условий. Фильтрация в качестве справочника
        cond = Test_Konstructors_Condition(driver, self.main_url()+self.login_url())
        cond.open()
        cond.konstructor_condition_filter_directory()

    def test_konstructor_condition_filter(self, driver):  # 6.Конструктор условий. Фильтрация
        cond = Test_Konstructors_Condition(driver, self.main_url()+self.login_url())
        cond.open()
        cond.konstructor_condition_filter()
    def test_konstructor_condition_edits_predict(self, driver):  # 8.Конструктор условий. Изменение предикатов
        cond = Test_Konstructors_Condition(driver, self.main_url()+self.login_url())
        cond.open()
        cond.konstructor_condition_edits_predict()


