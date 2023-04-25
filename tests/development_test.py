import time

from pages.development_locator import Test_Development

class TestDevelopment:
    def test_filter_additional(self, driver): # 30.Проверка отображения
        dev = Test_Development(driver, "http://193.124.117.158/#/login")
        dev.open()
        dev.table_reports()
        time.sleep(4)