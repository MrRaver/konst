import time

from pages.filters_page import Test_Filters

class TestFilters:
    def test_filter_additional(self,driver): # 1.Фильтрация данных в таблице
        filt=Test_Filters(driver,"http://193.124.117.158/#/login")
        filt.open()
        filt.filter_additional()
    def test_filter_table3(self,driver): # 2.Фильтрация данных в таблице
        filt=Test_Filters(driver,"http://193.124.117.158/#/login")
        filt.open()
        filt.filter_table3()
        time.sleep(4)
    def test_filter_additional_zakr(self,driver): # 1.Закрепление столбцов и сортировка (представление администратора)
        filt=Test_Filters(driver,"http://193.124.117.158/#/login")
        filt.open()
        filt.filter_additional_zakr()
        time.sleep(4)
    def test_filter_additional_visible(self,driver): # 2.Скрытие столбцов и настройка ширины (представление администратора)
        filt=Test_Filters(driver,"http://193.124.117.158/#/login")
        filt.open()
        filt.filter_additional_visible()
        time.sleep(4)

    def test_filter_additional_visible_and_move(self,driver):  # 3.Скрытие столбцов и настройка ширины (представление администратора)
        filt = Test_Filters(driver, "http://193.124.117.158/#/login")
        filt.open()
        filt.filter_additional_visible_and_move()
        time.sleep(4)
