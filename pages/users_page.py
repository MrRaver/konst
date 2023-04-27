import time

from selenium.webdriver.common import alert

from pages.base_page import BasePage
from locators.users_locators import Users as user
from selenium.webdriver import Keys

class User(BasePage):
    def create_role_GR1_GR2(self): #1 Создание роли
        self.add_role()
        names_role = self.RandomName("Тестовая роль GR1")
        print(names_role)
        names=self.element_is_visible(user.ROLES_NAME)
        names.click()
        names.clear()
        names.send_keys(names_role)
        self.element_is_visible(user.SAVE_ROLE).click()
        self.add_role()
        names = self.element_is_visible(user.ROLES_NAME)
        names.click()
        names.clear()
        names_role2 = self.RandomName("Тестовая роль GR1")
        print(names_role2)
        names.send_keys(names_role)
        self.element_is_visible(user.SAVE_ROLE).click()

    def create_user_GR1_GR2(self):  # 2.Создание пользователя
        self.add_users()
        names_role = self.RandomName("Тестовая роль GR")
        print(names_role)
        self.element_is_visible(user.LOGIN_USER).send_keys(names_role)
        self.element_is_visible(user.EMAIL_USER).send_keys("testgr@test.ru")
        self.element_is_visible(user.LASTNAME_USER).send_keys("test")
        self.element_is_visible(user.FIRSTNAME_USER).send_keys("Тестовая роль GR")
        self.element_is_visible(user.SURNAME_USER).send_keys("test")
        self.element_is_visible(user.PASSWORD_USER).send_keys("12345")
        self.element_is_visible(user.PASSWORD_USER2).send_keys("12345")
        self.element_is_visible(user.SAVE_USERS).click()
        self.add_users()
        names_role2 = self.RandomName("Тестовая роль GR TWO")
        print(names_role2)
        self.element_is_visible(user.LOGIN_USER).send_keys(names_role2)
        self.element_is_visible(user.EMAIL_USER).send_keys("testgr@test.ru")
        self.element_is_visible(user.LASTNAME_USER).send_keys("test")
        self.element_is_visible(user.FIRSTNAME_USER).send_keys("Тестовая роль GR TWO")
        self.element_is_visible(user.SURNAME_USER).send_keys("test")
        self.element_is_visible(user.PASSWORD_USER).send_keys("12345")
        self.element_is_visible(user.PASSWORD_USER2).send_keys("12345")
        self.element_is_visible(user.SAVE_USERS).click()


    def reg_by_email(self): #3 Регистрация пользователя по почте
        self.add_users()
        self.element_is_visible(user.REGISTRATION_EMAIL).click()
        self.element_is_visible(user.ADD_EMAIL_USERS).click()
        self.element_is_visible(user.EMAIL_BY_REGISTRATION).send_keys("test@test.ru")
        self.element_is_visible(user.CHOICE_ROLE).click()
        self.element_is_visible(user.INPUT_CHOICE_ROLE).send_keys("Тестовая роль GR")
        self.element_is_visible(user.CHOICES_ROLES).click()
        self.element_is_visible(user.SAVE_EMAIL).click()

    def reg_by_url(self):  # 4.Регистрация пользователя по ссылке
        self.add_users()
        self.element_is_visible(user.REGISTRATION_BY_URL).click()
        self.element_is_visible(user.ADD_LINK_URL).click()
        self.element_is_visible(user.CHOICE_URL).click()
        self.element_is_visible(user.INPUT_CHOICE_URL).send_keys("Тестовая роль GR")
        self.element_is_visible(user.CHOICES_URL).click()
        self.element_is_visible(user.SAVE_URL_LINK).click()

    def add_inserted_users(self):  # 5.Добавление пользователя в роли
        self.autorization()
        self.element_is_visible(user.ROLES).click()
        self.element_is_visible(user.TEST_ROLE_GR1).click()
        self.element_is_visible(user.ADD_USERS_IN_ROLES).click()
        self.element_is_visible(user.CHOICE_ELEMENT).click()
        self.element_is_visible(user.INPUT_INUSERS).send_keys("Тестовая роль GR")
        self.element_is_visible(user.CHOICE_FIRST_VARIANT).click()
        self.element_is_visible(user.SAVE_INUSERS).click()

    def off_users(self):  # 6.Отключение пользователя
        self.element_is_visible(user.USERS).click()
        self.element_is_visible(user.OFF_URL).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.element_is_visible(user.ENTER_BY_URL).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        return self.element_is_visible(user.TEXT_ERROR).text

    def GR12_password_test(self):  #7.Пользователи (Несовпадающие пароли)
        self.add_users()
        self.element_is_visible(user.LOGIN_USER).send_keys("Тестовая роль GR12")
        self.element_is_visible(user.EMAIL_USER).send_keys("testgr@test.ru")
        self.element_is_visible(user.LASTNAME_USER).send_keys("test")
        self.element_is_visible(user.FIRSTNAME_USER).send_keys("Тестовая роль GR12")
        self.element_is_visible(user.SURNAME_USER).send_keys("test")
        self.element_is_visible(user.PASSWORD_USER).send_keys("12345")
        self.element_is_visible(user.PASSWORD_USER2).send_keys("123456")
        return self.element_is_visible(user.PASSWORD_NOT_MATHES).text
    def GR12_name_test(self):  #8.Пользователи (Отсутствует Имя пользователя)
        self.add_users()
        self.element_is_visible(user.LOGIN_USER).send_keys("Тестовая роль GR12")
        self.element_is_visible(user.EMAIL_USER).send_keys("testgr@test.ru")
        self.element_is_visible(user.LASTNAME_USER).send_keys("test")
        self.element_is_visible(user.SURNAME_USER).send_keys("test")
        self.element_is_visible(user.PASSWORD_USER).send_keys("12345")
        self.element_is_visible(user.PASSWORD_USER2).send_keys("12345")
        self.element_is_visible(user.SAVE_USERS).click()
        return self.element_is_visible(user.NOT_NAMES).text


    def add_role_GR1(self): #11 Добавление роли в таблицу
        self.rigth()
        self.element_is_visible(user.ADD_THE_RIGHT).click()
        self.element_is_visible(user.NAMES_ROLE).click()
        self.element_is_visible(user.NAMES_ROLE_ENTER).click()
        names=self.element_is_visible(user.INPUT_NAMES_ROLE_ENTER)
        names.send_keys("GR1")
        names.send_keys(Keys.ENTER)
        self.element_is_visible(user.SEES).click()
        self.element_is_visible(user.FIND_ELEMENT).click()
        self.element_is_visible(user.NUMBER_ID).click()
        self.element_is_visible(user.STRING).click()
        self.element_is_visible(user.OK).click()
        self.element_is_present(user.CHECKBOX_ALL_STATUS).click()
        self.element_is_visible(user.EDITS).click()
        self.element_is_present(user.ADD_FIELD).click()
        self.element_is_present(user.EDIT_FIELD).click()
        self.element_is_visible(user.BUSINESS_PROCESS).click()
        self.element_is_present(user.TRANSLITION_ALL_STATUS).click()
        self.element_is_visible(user.SAVE).click()
    def delete_role_GR1(self): #12.Удаление роли в таблице
        self.rigth()
        self.element_is_visible(user.DELETE_GR1).click()
        self.element_is_visible(user.OKAY).click()
        self.element_is_visible(user.SAVE).click()

    def tree_status(self):  # 13.Дерево статусов
        self.rigth()
        self.element_is_visible(user.BUSINESS_PROCESS).click()
        self.element_is_present(user.TRANSLITION_ALL_STATUS).click()
        self.element_is_present(user.SETTING_STATUS).click()
        self.element_is_present(user.CHER_READY).click()
        self.element_is_visible(user.SAVE_BUSINESS_STATUS).click()
        self.element_is_visible(user.SAVE).click()
        self.element_is_visible(user.TREE_STATUS).click()

    def role2_inheritance(self):  # 14.Наследование
        self.element_is_visible(user.EDIT_ORDER).click()
        self.element_is_visible(user.THE_RIGHT).click()
        self.element_is_visible(user.ADD_THE_RIGHT).click()
        self.element_is_visible(user.NAMES_ROLE).click()
        self.element_is_visible(user.NAMES_ROLE_ENTER).click()
        names = self.element_is_visible(user.INPUT_NAMES_ROLE_ENTER)
        names.send_keys("GR1")
        names.send_keys(Keys.ENTER)
        self.element_is_visible(user.SEES).click()
        self.element_is_visible(user.FIND_ELEMENT).click()
        self.element_is_visible(user.NUMBER_ID).click()
        self.element_is_visible(user.STRING).click()
        self.element_is_visible(user.OK).click()
        self.element_is_present(user.CHECKBOX_ALL_STATUS).click()
        self.element_is_visible(user.EDITS).click()
        self.element_is_present(user.ADD_FIELD).click()
        self.element_is_present(user.EDIT_FIELD).click()
        self.element_is_visible(user.BUSINESS_PROCESS).click()
        self.element_is_present(user.TRANSLITION_ALL_STATUS).click()
        self.element_is_visible(user.SAVE).click()
        self.element_is_visible(user.ROLES).click()
        self.element_is_visible(user.TEST_ROLE_GR2).click()
        self.element_is_visible(user.EYES).click()
        self.element_is_visible(user.CHOICE_EL_GR2).click()
        input = self.element_is_visible(user.PLACEHOLDER_GR2)
        input.send_keys("Тестовая роль GR2")
        input.send_keys(Keys.ENTER)
        self.element_is_visible(user.SAVE_GR2).click()
        self.element_is_visible(user.ROLES).click()
        self.element_is_visible(user.TEST_ROLE_GR2).click()
        self.element_is_visible(user.TEST_SCHEMA).click()

    def give_rigth(self):  # 1. Выдача прав пользователям
        self.rigth()
        self.element_is_visible(user.ADD_THE_RIGHT).click()
        self.element_is_visible(user.NAMES_ROLE).click()
        self.element_is_visible(user.NAMES_ROLE_ENTER).click()
        names = self.element_is_visible(user.INPUT_NAMES_ROLE_ENTER)
        names.send_keys("GR1")
        names.send_keys(Keys.ENTER)
        self.element_is_visible(user.SEES).click()
        self.element_is_visible(user.ALL_FIELDS).click()
        self.element_is_visible(user.CHECKBOX_ALL_STATUS).click()
        self.element_is_visible(user.EDITS).click()
        self.element_is_visible(user.ADD_FIELD).click()
        self.element_is_visible(user.EDITS_EDIT).click()
        self.element_is_visible(user.DRAFT).click()
        self.element_is_visible(user.READ_TWO).click()
        self.element_is_visible(user.READ_FOUR).click()
        self.element_is_visible(user.CONFIRM_ONE).click()
        self.element_is_visible(user.CONFIRM_THREE).click()
        self.element_is_visible(user.CONFIRM_FIVE).click()
        self.element_is_visible(user.SAVE_EDIT).click()
        self.element_is_visible(user.BUSINESS_PROCESS).click()
        self.element_is_visible(user.EDITS_PROCESS).click()
        self.element_is_visible(user.DRAFT_READY).click()
        self.element_is_visible(user.SAVE_EDITS_PROCESS).click()
        self.element_is_visible(user.ADD_THE_RIGHT).click()
        self.element_is_visible(user.NAMES_ROLE2).click()
        self.element_is_visible(user.NAMES_ROLE_ENTER2).click()
        names = self.element_is_visible(user.INPUT_NAMES_ROLE_ENTER)
        names.send_keys("GR2")
        names.send_keys(Keys.ENTER)
        self.element_is_visible(user.SEES2).click()
        self.element_is_visible(user.ALL_FIELDS2).click()
        self.element_is_visible(user.CHECKBOX_ALL_STATUS2).click()
        self.element_is_visible(user.EDITS2).click()
        self.element_is_visible(user.ADD_FIELD2).click()
        self.element_is_visible(user.EDIT_FIELD2).click()
        self.element_is_visible(user.BUSINESS_PROCESS2).click()
        self.element_is_visible(user.ALL_STATUS2).click()
        self.element_is_visible(user.SAVE).click()

    def off_visible(self):  # 2. Скрытие столбцов через права
        self.rigth()
        self.element_is_visible(user.SEES).click()
        self.element_is_visible(user.ALL_FIELDS).click()
        self.element_is_visible(user.FIND_ELEMENT).click()
        self.element_is_visible(user.ALL_CHOICE).click()
        self.element_is_visible(user.MANY_STRING).click()
        self.element_is_visible(user.INTENGER).click()
        self.element_is_visible(user.OK).click()
        self.element_is_visible(user.SAVE).click()

    def delete_right(self):  # 3. Удаление прав
        self.rigth()
        self.element_is_visible(user.EDITS).click()
        self.element_is_visible(user.ADD_FIELD).click()
        self.element_is_visible(user.EDITS_EDIT).click()
        self.element_is_visible(user.DRAFT).click()
        self.element_is_visible(user.READY).click()
        self.element_is_visible(user.READY).click()
        self.element_is_visible(user.CONFIRM).click()
        self.element_is_visible(user.CONFIRM).click()
        self.element_is_visible(user.SAVE_EDIT).click()
        self.element_is_visible(user.SAVE).click()
    def add_users(self):
        self.element_is_visible(user.USERS).click()
        self.element_is_visible(user.ADD_USERS).click()
    def rigth(self):
        self.element_is_visible(user.EDIT_ADDITIONAL).click()
        self.element_is_visible(user.THE_RIGHT).click()

    def add_role(self):
        self.element_is_visible(user.ROLES).click()
        self.element_is_visible(user.ADD_ROLE).click()
















