from selenium.webdriver.common.by import By

class Reports:
    DEVELOPMENT=(By.XPATH,"/html/body/div/div/div[2]/ul/li[8]/a") #Разработка
    REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[1]/ul/li[3]/a")  #Отчеты
    ADD_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table[1]/tbody/tr/td[3]") #Добавить отчет
    NAMES_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[1]/input")#Имя отчета
    THEME_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[2]/textarea")#Тема отчета
    CHOICE_DATA=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/button/span[1]")#Выбор данных
    REPORTS_FIRST=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table[2]/tbody/tr/td[1]/a") #Первый отчет
    INPUT_DATA=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/ul/li[4]/div/input") # ввод даты
    FIRST_DATA = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/ul/li[6]") # первая даты
    CHOICE_ROLE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/div[4]/div/div/button") #выбор роли
    INPUT_ROLE = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/div[4]/div/div/ul/li[4]/div/input") #вводи роли
    FIRST_ROLE = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/div[4]/div/div/ul/li[6]") #Первая роль
    ADD_FIELD=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div/button[2]") #Добавить поле
    FIRST_ROW=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[1]/div/div/ul/li[1]/div/div") #Первое поле
    SECOND_ROW=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[1]/div/div/ul/li[2]/div/div") #второе поле
    THIRD_ROW=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[1]/div/div/ul/li[3]/div/div") # третье поле
    NAMES_FIELD=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[2]/div/div/ul/li[1]/input") #ввод имени
    NAME_IN_BASE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[2]/div/div/ul/li[3]/input") #имя в базе
    TYPE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[2]/div/div/ul/li[5]/select") #тип
    MANY_STRING=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[2]/div/div/ul/li[5]/select/option[6]") #многострочная строк
    DATE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[5]/div/div[2]/div/div[2]/div/div/ul/li[5]/select/option[5]") #дата
    REQUEST = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[2]")  # запрос
    SQL=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div")
    INPUT_SQL = (By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[3]/div/textarea")
    SAVE_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[3]/button[2]") # сохранить отчет
    FIRST_REPORT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table[2]/tbody/tr/td[1]/a") #Первый отчет
    EXPORT_EXCEL=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/span/button[2]") #Экспорт эксел


class CLIENTPROGRAMMING:
    IFRAME = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/next-gen/iframe")  # iframe
    DEVELOPMENT = (By.XPATH, "/html/body/div/div/div[2]/ul/li[8]/a")  # Разработка
    ADD=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[1]/div[1]/button") #Добавить DHTML
    ADD_DHTML2=(By.CLASS_NAME,"pi pi-plus-circle p-button-icon") #Добавить DHTML
    NAMES_DHTML=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") #имя DHTML
    HTML=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/ul/li[2]") #HTML
    INPUT_DHTML=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/textarea") # Ввод DHTML-блоки
    INPUT_ACTION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/textarea") # Ввод действия над строками
    JS=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/ul/li[3]") #JS
    ROUTE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/ul/li[4]") #маршрутор
    ADD_ROUTE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]/button/span[1]") #Добавить маршрут
    STATE_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/input")# ввод state
    URL_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/input") #ввод url
    CONTROLLER_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[4]/input") #ввод controller
    NAMES_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[5]/input") #ввод имени
    SAVE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/button[1]") #Cохранить
    CLOSE=(By.XPATH,"/html/body/div[3]/div/div[1]/div/button/span[1]") #Закрыть
    SERVER_PROGRAMMING=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[1]/ul/li[2]/a")
    EDIT=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/div/button[1]")
    EDIT2=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/div/div/button[1]")
    DELETE=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/div/button[2]")
    DELETE2=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/div/div/button[2]")
    YES_DELETE=(By.XPATH,"/html/body/div[3]/div/div[3]/button[2]") #Да, удалить
    YES_DELETE2=(By.XPATH,"/html/body/div[3]/div/div[3]/button[2]") #Да, удалить
    ACTIONS_STRING=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/ul/li[2]/a") #Дейсвия над строками
    NAMES_ACTION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") #имя действий над строками
    BUTTON_NAMES_ACTION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[4]/input") #имя кнопки действий над строками
    CHECKBOX_SHOW_GRID=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/div[2]") #чекбокс показать грид
    RIGHT_ON_STRING=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/ul/li[4]") #права над строками
    ROLE=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]/div/span") #Роли
    INPUT_ROLE=(By.XPATH,"/html/body/div[3]/div[1]/div/input") #ввод роли
    FIRST_ROVE_VARIANT=(By.XPATH,"/html/body/div[3]/div[2]/div/ul/li") #Первый вариант роли
    ACTION = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/span")  # Действие
    FIRST_ACTION_VARIANT = (By.XPATH, "/html/body/div[3]/div[2]/ul")  # Первый вариант роли
    INPUT_ACT=(By.XPATH,"/html/body/div[3]/div[1]/div/input")
    TABLE=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/span") #Таблицы
    INPUT_TABLE=(By.XPATH,"/html/body/div[3]/div[1]/div/input")
    FIRST_TABLE_VARIANT=(By.XPATH,"/html/body/div[3]/div[2]/div/ul/li[1]")
    STATUS=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/span") #Статус
    INPUT_STATUS=(By.XPATH,"/html/body/div[3]/div[1]/div/input") # ввод Статус
    FIRST_STATUS_VARIANT=(By.XPATH,"/html/body/div[3]/div[2]/ul/li[1]") # первый вариант Статус
    CHECKBOX_DRAFT=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]")
    SAVE_RIGHT_ON_STRING = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button[5]/span[1]")  # сохранение прав над строками
    JS_TRIGGER=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/ul/li[5]") #Js trigger
    NAMES_JS_TRIGGER=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") # имя  JS  trigger
    STATE_JS_TRIGGER=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[4]/input") # state  JS  trigger
    CODE_JS_TRIGGER=(By.XPATH,"//html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/textarea") # код  JS  trigger
    SAVE_JS_TRIGGER=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/button[1]") # сохранить  JS  trigger
    SAMPLE_CELL=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/ul/li[3]") #Шаблоны ячеек
    NAMES_SAMPLE_CELL=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") # имя шаблоны ячеек
    CHOICE_FIELD=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/span") #Выбрать поле
    FLOAT=(By.XPATH,"/html/body/div[5]/div/ul/li[2]") #Чило с плавающей точкой
    CHOICE_TYPE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div[2]") #Выбрать тип
    CELL=(By.XPATH,"/html/body/div[5]/div/ul/li[2]") #Ячейка
    INPUT_HTML_CELL=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[4]/div/div[2]/div/div/div[2]/div/div[1]/textarea") #Ввод html
    JS_CELL=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div/ul/li[2]") #js
    JS_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[4]/div/div[2]/div/div/div[2]/div/div[1]/textarea")

class SERVERPROGRAMMING:
    IFRAME = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/next-gen/iframe")  # iframe
    DEVELOPMENT = (By.XPATH, "/html/body/div/div/div[2]/ul/li[8]/a")  # Разработка
    SERVER_PROGRAMMING = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[1]/ul/li[2]/a") #Серверная разработка
    ADD=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[1]/div[1]/button") #Добавить
    INPUT_DYNAMIC_NAMES=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") #Имя динамического API
    INPUT_DYNAMIC_CODE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/textarea") #код динамического API
    TASKS=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/ul/li[2]") #Задания
    INPUT_TASKS=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") # имя задания
    IN_TRANSATION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/ul/li[2]") #В транзакции
    INPUT_IN_TRANSATION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/textarea") #Ввод в транзакции
    SERVER_FUNCTION=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/ul/li[3]") #Серверные функции
    ADD_SERVER_FUNCTION=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/button") # Добавить серверную функцию
    INPUT_OBJECT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") #Ввод объекта
    INPUT_METHOD=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[4]/input") #Ввод метода
    INPUT_DESCRIPTION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[6]/textarea") #Ввод описания
    INPUT_CODE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/textarea") #Ввод  кода
    SHOW_All=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]") #Развернуть все
    EDIT=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td[1]/div/button[1]") #Редактировать
    DELETE=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td[1]/div/button[2]") #Удалить






















