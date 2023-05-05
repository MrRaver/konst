import time

from pages.filters_page import Test_Filters
from tests.base_test import BaseTest


class TestFilters(BaseTest):
     def test_filter_additional(self, driver):  # 1.Фильтрация данных в таблице
        fil = Test_Filters(driver, self.main_url() + self.login_url())
        fil.open()
        fil.filter_additional()


     def test_filter_table3(self, driver):  # 2.Фильтрация данных в таблице
        fil = Test_Filters(driver, self.main_url() + self.login_url())
        fil.open()
        fil.filter_table3()


def test_filter_additional_zakr(self, driver):  # 1.Закрепление столбцов и сортировка (представление администратора)
    fil = Test_Filters(driver, self.main_url() + self.login_url())
    fil.open()
    fil.filter_additional_zakr()


def test_filter_additional_visible(self,driver):  # 2.Скрытие столбцов и настройка ширины (представление администратора)
    fil = Test_Filters(driver, self.main_url() + self.login_url())
    fil.open()
    fil.filter_additional_visible()


def test_filter_additional_visible_and_move(self, driver):  # 3.Скрытие столбцов и настройка ширины (представление администратора)
    fil = Test_Filters(driver, self.main_url() + self.login_url())
    fil.open()
    fil.filter_additional_visible_and_move()

