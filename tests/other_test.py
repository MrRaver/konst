import time

from pages.other_page import Others
from tests.base_test import BaseTest

class TestOther(BaseTest):
    def test_catalog_data(self,driver): #Открытие конструктора
        othe=Others(driver, self.main_url()+self.login_url())
        othe.open()
        othe.catalog_data()

    def test_message(self, driver): #Отправка уведомлений
        othe = Others(driver, self.main_url()+self.login_url())
        othe.open()
        othe.message()

    def test_import_data(self, driver):  # импорт данных, нужно указаьть путь pages>other_page>import_dat
        othe = Others(driver, self.main_url()+self.login_url())
        othe.open()
        res=othe.import_dat()
        print(res)
        time.sleep(4)
    def test_rc(self,driver):
        othe = Others(driver, self.main_url_rc()+self.login_url())
        othe.open2()
        time.sleep(4)


