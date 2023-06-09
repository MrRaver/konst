import time

from pages.users_page import User
from tests.base_test import BaseTest


class TestRoleUser(BaseTest):

    def test_create_role_GR1_GR2(self, driver):  # 1.Создание роли
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.create_role_GR1_GR2()

    def test_create_user_GR1_GR2(self, driver):  # 2.Создание пользователя
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.create_user_GR1_GR2()

    def test_reg_by_email(self,driver):  # 3 Регистрация пользователя по почте
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.reg_by_email()

    def test_reg_by_url(self,driver):  # 4.Регистрация пользователя по ссылке
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.reg_by_url()

    def test_add_inserted_users(self,driver):  # 5.Добавление пользователя в роли
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.add_inserted_users()

    def test_off_users(self, driver):  # 6.Отключение пользователя
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        text= user.off_users()
        print(text)

    def test_GR12_password_test(self, driver):  # 7.Пользователи (Несовпадающие пароли)
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        erorr=user.GR12_password_test()
        print(erorr)
    def test_empty_name(self, driver):  # 8.Пользователи (Отсутствует Имя пользователя)
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        erorr=user.GR12_name_test()
        print(erorr)



    def test_add_additional_role_GR1(self,driver): #11 Добавление роли в таблицу
        user=User(driver,self.main_url()+self.login_url())
        user.open()
        user.add_role_GR1()

    def test_delete_role_GR1(self, driver): #12.Удаление роли в таблице
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.delete_role_GR1()

    def test_tree_status(self, driver):  # 13.Дерево статусов
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.tree_status()
    def test_role2_inheritance(self,driver): #14. Наследование
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.role2_inheritance()
    def test_give_rigth(self,driver): #1. Выдача прав пользователям
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.give_rigth()

    def test_off_visible(self,driver):  # 2. Скрытие столбцов через права
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.off_visible()
    def test_delete_right(self,driver):  # 3. Удаление прав
        user = User(driver, self.main_url()+self.login_url())
        user.open()
        user.delete_right()
