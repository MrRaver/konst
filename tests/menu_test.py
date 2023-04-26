from pages.menu_page import Test_Menu


class TestMenu:
    def test_create_url_order(self,driver): #1.Создание пункта меню
        menu = Test_Menu(driver, "http://193.124.117.158/#/login")
        menu.open()
        menu.create_url_order()

    def test_create_url_order_picture(self, driver):  # 2.Добавление картинки
        menu = Test_Menu(driver, "http://193.124.117.158/#/login")
        menu.open()
        menu.create_url_order_picture()

    def test_create_url_order_view(self,driver):  # 3.Отображение
        menu = Test_Menu(driver, "http://193.124.117.158/#/login")
        menu.open()
        menu.create_url_order_view()
    def test_create_url_order_delete(self,driver):   # 4.Удаление
        menu = Test_Menu(driver, "http://193.124.117.158/#/login")
        menu.open()
        menu.create_url_order_delete()