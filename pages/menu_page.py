from pages.base_page import BasePage
from locators.menu_locator import Menu as menu
from tests.base_test import BaseTest

class Test_Menu(BasePage,BaseTest):
    def create_url_order(self): #1.Создание пункта меню
        self.add_menu()
        names_table=self.RandomName("Заказы")
        self.element_is_visible(menu.SECOND_ROW).click()
        names=self.element_is_visible(menu.NAMES)
        names.clear()
        names.send_keys(names_table)
        print(names_table)
        url=self.element_is_visible(menu.URL)
        url.clear()
        url.send_keys(self.main_url()+self.table_order())
        self.element_is_visible(menu.CHOICE_ROLE).click()
        self.element_is_visible(menu.INPUT_CHOICE_ROLE).send_keys("Тестовый пользователь")
        self.element_is_visible(menu.FIRST_CHOICE_ROLE).click()
        self.element_is_visible(menu.CHOICE_ROLE).click()
        self.element_is_visible(menu.SAVE).click()

    def create_url_order_picture(self):   # 2.Добавление картинки
        self.add_menu()
        self.element_is_visible(menu.THIRD_ROW).click()
        names_table = self.RandomName("Заказы  с картинкой")
        names = self.element_is_visible(menu.NAMES)
        names.clear()
        names.send_keys(names_table)
        self.element_is_visible(menu.URL).send_keys("http://193.124.117.158/#/main/tableview/10022")
        self.element_is_visible(menu.CHOICE_ROLE).click()
        self.element_is_visible(menu.INPUT_CHOICE_ROLE).send_keys("Тестовый пользователь")
        self.element_is_visible(menu.FIRST_CHOICE_ROLE).click()
        self.element_is_visible(menu.CHOICE_ROLE).click()
        self.element_is_visible(menu.CHOICE_ICON).click()
        self.element_is_visible(menu.ICON).click()
        self.element_is_visible(menu.SAVE).click()
    def create_url_order_view(self):   # 3.Отображение
        self.add_menu()
        self.element_is_visible(menu.FOURTH_ROW).click()
        names_table = self.RandomName("Заказы в папке")
        print(names_table)
        names = self.element_is_visible(menu.NAMES)
        names.clear()
        names.send_keys(names_table)
        self.element_is_visible(menu.URL).send_keys("http://193.124.117.158/#/main/tableview/10022")
        self.element_is_visible(menu.CHOICE_ROLE).click()
        self.element_is_visible(menu.INPUT_CHOICE_ROLE).send_keys("Тестовый пользователь")
        self.element_is_visible(menu.FIRST_CHOICE_ROLE).click()
        self.element_is_visible(menu.CHOICE_ROLE).click()
        self.element_is_visible(menu.ADDITIONAL_SETTING).click()
        self.element_is_visible(menu.CHOICE_FOLDER).click()
        self.element_is_visible(menu.INPUT_CHOICE_FOLDER).send_keys("30.03.2022")
        self.element_is_visible(menu.FIRST_FOLDER_VARIANT).click()
        self.element_is_visible(menu.CHOICE_FOLDER).click()
        self.element_is_visible(menu.SAVE).click()
    def create_url_order_delete(self):   # 4.Удаление
        self.element_is_visible(menu.MENU).click()
        self.element_is_visible(menu.FOURTH_ROW).click()
        self.element_is_visible(menu.DELETE).click()
        self.driver.switch_to.alert.accept()
        self.element_is_visible(menu.SAVE).click()
    def add_menu(self):
        self.element_is_visible(menu.MENU).click()
        self.element_is_visible(menu.ADD_MENU).click()






