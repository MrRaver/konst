from selenium.webdriver.common.by import By

class Filtesr_Locators:
    ADDITIONAL_EDIT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[5]/td/div/div/div[3]/a") #справочник
    TABLE3=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[7]/td/div/div/div[3]/a") #Таблица3
    ID_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[1]/div[1]/input") #Ввод id
    MANY_STRING_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[2]/div[1]/input") #ввод множественной строки
    STRING_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[3]/div[1]/input") #ввод строки
    INTENGER_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[4]/div[1]/input") #ввод целого элемента
    FLOAT_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[5]/div[1]/input") #ввод плавающей точки элемента
    DATA_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[6]/div[1]/input") #ввод даты элемента
    DATA_TIME_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[7]/div[1]/input") #ввод даты и времени

    TABLE3_STRING_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[3]/div[1]/div/sb-multy-select/div/div/div[1]/div[2]/input") #ввод строки
    TABLE3_ID_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[2]/div[1]/input") #ввод строки
    TABLE3_MANY_STRING_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[4]/div[1]/div/sb-multy-select/div/div/div[1]/div[2]/input") #ввод множественной строки
    TABLE3_INTENGER_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[5]/div[1]/div/sb-multy-select/div/div/div[1]/div[2]/input") #ввод целого числа
    TABLE3_FLOAT_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[6]/div[1]/div/sb-multy-select/div/div/div[1]/div[2]/input") #ввод плавающей запятой
    TABLE3_DATA_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[7]/div[1]/div/sb-multy-select/div/div/div[1]/div[2]/input") #ввод даты
    TABLE3_DATA_TIME_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[8]/div[1]/div/sb-multy-select/div/div/div[1]/div[2]/input") #ввод даты и времени
    TABLE3_BOOLEAN_INPUT=(By.XPATH,"/html/body/div/div/div[3]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[3]/th[9]/div[1]/div/sb-multy-select/div/div/div[1]/div[2]/input") #ввод логического типа данных
    #Представления и фильтры
    EDIT_ADDITIONAL = (By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[5]/td/div/div/div[4]/a")  # настройки справочника таблицы
    KONSTRUCTOR_CONDITION = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[5]/a/span/span")  # конструктор условий
    VIEW=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[1]/ul/li[7]/a") #Представление
    ELLIPSIS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/view-table/div/div[3]/div[2]/div/button[3]/div") #троеточие
    VIEW_TABLE=(By.XPATH,"/html/body/ul/li[5]/a") #вид->таблица
    CHECKBOX_STATUS=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/input") #чек бокс статус
    CHECKBOX_NUMBER=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/input") #чек бокс номер
    DATA=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/view-table/div/custom-grid/div[1]/div[2]/table/thead/tr[1]/th[8]/ng-html-include/div[1]") #Столбик дата
    CHOICE_ORDER=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/span/span[2]/span") #Выбрать порядок
    ASCENDING=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/ul/li/div[3]/span/span") #По возростанию
    SAVE_VIEW=(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/button[1]") #Сохранить представление
    SAVE_AS=(By.XPATH,"/html/body/ul/li[8]/a") #Сохранить как
    INPUT_NAME_VIEW=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/form/div/input") #Ввод имя представления
    SAVE_NAME_VIEW=(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/button[1]") #Сохранить представление
    DEFAULT=(By.XPATH,"/html/body/ul/li[6]")# по умолчанию
    VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/p") #Видимый
    STATUS_VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/input") #Видимый статус
    NUMBER_VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/input") #Видимый номер
    MANY_STRING_VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[3]/div[2]/input") #Видимая многострочная строка
    STRING_VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/input") #Видимая строка MANY_STRING_VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[3]/div[2]/input") #Видимая многострочная строка
    INTENGER_VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[5]/div[2]/input") #Видимая строка
    FLOAT_VISIBLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[6]/div[2]/input") #Видимая строка
    LENGTH_STATUS=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]/input") #ширина статуса

    VIEW_TABLE1 = (By.XPATH, "/html/body/ul/li[6]/a")  # вид->таблица
    VIEW_TABLE2 = (By.XPATH, "/html/body/ul/li[7]/a")  # вид->таблица
    SAVE_AS1 = (By.XPATH, "/html/body/ul/li[9]/a")  # Сохранить как
    DEFAULT1 = (By.XPATH, "/html/body/ul/li[7]/a")  # Сохранить как


    TEST_VIEW2=(By.XPATH,"/html/body/ul/li[4]/a") #Выбрать тестовое предтслаение 2
    STATUS=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]") #Статус
    DATA_EDIT=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[16]/div[1]") #Дата изменения
    DATA_ELEMENT=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[6]/div[1]")
    SAVE=(By.XPATH,"/html/body/ul/li[10]/a") #Сохранить
    PRELAST=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[15]/div[1]")
    SECOND = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div[1]")
