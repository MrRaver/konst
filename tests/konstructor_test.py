import time

from pages.konsructor_page import Test_Konstructor,Table_in_table,Test_dependent_directory

class TestKonstructors:
    def test_create_folder(self,driver): # 2.Создание папки
        cons=Test_Konstructor(driver,"http://193.124.117.158/#/login")
        cons.open()
        cons.create_folder()
    def test_delete_folder(self,driver):#3.Удаление папки
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.delete_folder()
    def test_create_table(self,driver): #6.Создание таблицы: справочника
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.create_table_directory()
        time.sleep(3)

    def test_hints(self, driver): #7.Создание подсказок
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.Add_help()
        time.sleep(3)

    def test_use_directory(self, driver):#8.Создание таблицы, использующей справочник
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.use_directory()
        time.sleep(20)



    def test_type_data_into_table(self,driver): #10.Создание типа данных таблица внутри таблицы
        cons = Table_in_table(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.table_order()
        cons.create_position_order()
        cons.create_position()
        time.sleep(3)
    def test_create_copy_table1(self,driver):#14.Создание зависимых справочников
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.add_copy()
        time.sleep(3)

    def test_dependent_directory(self,driver):#13.Создание зависимых справочников
        cons = Test_dependent_directory(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.create_table_type()
        cons.create_table_data()
        cons.create_table_addiction()
        time.sleep(3)
    def test_multiple_choice(self,driver):#15.Создание таблицы, использующей справочник с множественным выбором
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.multiple_table()
        time.sleep(20)
    def test_transition_between_tables(self,driver):#16.Создание перехода в другую таблицу
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.between_tables()
        time.sleep(3)

    def test_add_form_edit(self,driver):#17.Создание разрешения добавления в форме редактирования для справочника
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.add_editForm()
        time.sleep(3)

    def test_delete_table(self,driver):  #  20.Создание разрешения добавления в форме редактирования для справочника
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        data=cons.delete_table()
        print(data)
        time.sleep(3)
    def test_edit_table_name(self,driver): #21.Редактирование Alias и названий таблиц
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.edit_table_name()
        time.sleep(3)
    def test_matches_rows(self,driver): #22.Смена местами Alias и названий нескольких столбцов
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        data=cons.matches_row()
        print(data)
        time.sleep(3)
    def test_moving_rows(self,driver): #23.Перемещение столбцов
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.moving_rows()
        time.sleep(4)
    def test_fix_number(self,driver): #24.Закрепление столбца
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.fix_number()
        time.sleep(4)
    def test_status_checkbox(self,driver): #25.Отключение статусов
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.test_status()
        time.sleep(4)

    def test_change_dimesnion(self,driver):  # 26.Изменение ширины ячейки в форме редактирования
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.change_dimesnion()
        time.sleep(4)

    def test_change_sample(self,driver):  # 27.Изменение шаблона ячейки
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.change_sample()
        time.sleep(3)

    def test_edit_rows(self,driver):  # 28.Возможность редактирования в строке
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.chance_edit_rows()
        time.sleep(3)

    def test_add_unique_row(self,driver):  # 30.Создание уникального и обязательного для заполнения поля
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.add_unique_row()
        time.sleep(3)

    def test_off_unique_checkbox(self,driver):  # 31.Создание уникального и обязательного для заполнения поля
        cons = Test_Konstructor(driver, "http://193.124.117.158/#/login")
        cons.open()
        cons.off_unique_checkbox()
        time.sleep(3)




