import time

from pages.konstructor_condition_page import Test_Konstructors_Condition

class TestConditionKonstructors:
    def test_create_folder(self,driver): # 1.Предварительная подготовка
        cond=Test_Konstructors_Condition(driver,"http://193.124.117.158/#/login")
        cond.open()
        cond.create_table_test1()


    def test_konstructor_condition_save(self,driver): # 2.Конструктор условий. Сохранение
        cond=Test_Konstructors_Condition(driver,"http://193.124.117.158/#/login")
        cond.open()
        cond.konstructor_condition_save()

    def test_konstructor_condition_edit(self,driver): # 3.Конструктор условий. Редактирование
        cond=Test_Konstructors_Condition(driver,"http://193.124.117.158/#/login")
        cond.open()
        cond.konstructor_condition_edit()
        time.sleep(4)
    def test_konstructor_condition_status(self,driver): # #4.Конструктор условий. Перевод в статусы
        cond=Test_Konstructors_Condition(driver,"http://193.124.117.158/#/login")
        cond.open()
        cond.konstructor_condition_status()

    def test_konstructor_condition_filter_directory(self, driver):  #5.Конструктор условий. Фильтрация в качестве справочника
        cond = Test_Konstructors_Condition(driver, "http://193.124.117.158/#/login")
        cond.open()
        cond.konstructor_condition_filter_directory()
        time.sleep(4)

    def test_konstructor_condition_filter(self, driver):  # 6.Конструктор условий. Фильтрация
        cond = Test_Konstructors_Condition(driver, "http://193.124.117.158/#/login")
        cond.open()
        cond.konstructor_condition_filter()
        time.sleep(4)
    def test_konstructor_condition_edits_predict(self, driver):  # 8.Конструктор условий. Изменение предикатов
        cond = Test_Konstructors_Condition(driver, "http://193.124.117.158/#/login")
        cond.open()
        cond.konstructor_condition_edits_predict()
        time.sleep(4)

