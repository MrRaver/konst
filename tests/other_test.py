import time

from pages.other_page import Others

class TestOther:
    def test_catalog_data(self,driver): #Открытие конструктора
        othe=Others(driver,"http://193.124.117.158/#/login")
        othe.open()
        othe.catalog_data()
        time.sleep(3)

    def test_message(self, driver): #Отправка уведомлений
        othe = Others(driver, "http://193.124.117.158/#/login")
        othe.open()
        othe.message()
        time.sleep(3)

    def test_import_data(self, driver):  # импорт данных
        othe = Others(driver, "http://193.124.117.158/#/login")
        othe.open()
        res=othe.import_dat()
        print(res)
        time.sleep(3)
