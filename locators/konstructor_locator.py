from selenium.webdriver.common.by import By

class Autorization:
  PERSONNEL_NUMBER=(By.XPATH,"/html/body/div/div/div/div/div[1]/div/div[2]/input") #Логин
  PASSWORD=(By.XPATH,"/html/body/div/div/div/div/div[1]/div/div[3]/input") #Пароль
  BUTTON_ENTER=(By.XPATH,"/html/body/div/div/div/div/div[1]/div/div[4]/button") #кнопка войти

class CreateFolder:
  ARROW_DOWN=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[1]/table/tbody/tr/td[5]/div/button") #стрелочка вниз
  ADD_FOLDER=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[1]/table/tbody/tr/td[5]/div/ul/li[4]/a") #создать папку
  EDIT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[6]/div/div/div/ul/li[1]/table/tbody/tr/td[3]/i") #иконка карандаша, вписать имя
  INPUT_TEXT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[6]/div/div/div/ul/li[1]/table/tbody/tr/td[4]/input")# поле имени
  CHECK_MARK=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[6]/div/div/div/ul/li[1]/table/tbody/tr/td[3]/i") #сохранить имя

class DeleteFolder:
  DELETE_PLACE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[1]/div/div[3]") # место удаления
  ARROW_DOWN = (By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[6]/div/div/div/ul/li[1]/table/tbody/tr/td[5]/div/button") #стрелочка вниз
  ADD_FOLDER = (By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[6]/div/div/div/ul/li[1]/table/tbody/tr/td[5]/div/ul/li[4]") #создать папку
  PLACE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div")# место в общей папки
  MOVING=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[6]/div/div/div/ul/li[2]/ul/li[2]/div/div/div/ul/li[1]/table/tbody/tr/td[1]/i")#созданная папка
  MOVING2=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[4]/div/div/div/ul/li[1]/table/tbody/tr/td[1]")#перенесенная созданная папка

class CreateTable:
  TABLE_NAME=(By.ID,"table-name")# имя таблицы
  ADD_TABLE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div/div/div/div/div/ul/li[2]/ul/li[6]/div/div/div/ul/li[1]/table/tbody/tr/td[5]/div/a")#создать таблицу
  ADD_ROW=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[3]")#добавить столбец
  ROW=(By.CLASS_NAME,"panel-body padded ng-scope") #первая строка
  SECOND_ROW=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[3]/div/div/div/div")#вторая строка
  NAMES=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[1]/tr/td[2]/input")# имя столбца
  THiRD_ROW=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[4]/div/div/div/div") #третья строка
  TYPE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/div[1]/span/span[2]") #тип даннных
  TYPE_MANY_STRING=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[5]/span") #тип множественная строка
  FOUR_ROW=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[5]/div/div/div/div")#четвертая строка
  TYPE_INTENGER=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[6]/span")# тип целое число
  FIFTH_ROW = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[6]/div/div/div/div") #пятая строка
  TYPE_FLOAT = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[7]/span")# тип число с плавающей точкой
  SIXTH_ROW = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[7]/div/div/div/div")#шестая строка
  TYPE_DATA = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[8]/span")#тип дата
  SEVENTH_ROW = (By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[8]/div/div/div/div")#седьмая строка
  TYPE_DATA_TIME= (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[9]/span")#тип дата и время
  EIGHTH_ROW= (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[9]/div/div/div/div")#восьмая строка
  TYPE_BOOLEAN_VALUE = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[10]/span")#тип логическое значение
  NINETH_ROW = (By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[10]/div/div/div/div")#девятая строка
  TENTH_ROW = (By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[11]/div/div/div/div")#десятая строка
  TYPE_FILE = (By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[11]/span")#тип файл
  TYPE_DIRECTORY=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[12]/span")#тип справочник
  TYPE_TABLE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[13]/span") #тип таблица
  TYPE_HTML=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[14]/span") #тип HTML
  SAVE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[3]/a[1]")#кнопка сохранить
  EDIT_ADDITIONAL=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[5]/td/div/div/div[4]/a")#настройки справочника таблицы
  ADD_ADDITINAL_SETTING=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[6]/tr[1]/th/a") #дополнительные настройки
  ADDITINAL_HEADER=(By.ID,"TooltipTableHeader") # подсказка в заголовке
  ADDITINAL_EDIT=(By.ID,"TooltipEditForm") #подсказка в форме редактирование
  SETTING_ADDITINAL=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[4]/tr/th/a") #настройки справочника пункт
  INPUT_NAMES_ADDITINAL=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[1]/td[2]/div/div/input[1]") # ввод  спраочника
  NAMES_ADDITINAL=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[1]/td[2]/div/div/div[1]") #справочник
  UNIQUE_COLUMN=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[2]/td[2]/div/div[1]/span") # уникальный столбец
  INPUT_UNIQUE_COLUMN=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[2]/td[2]/div/input[1]") #ввод уникального столбца
  COLUMN_VIEW=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[3]/td[2]/div/div[1]/span") #cтолбец отображения
  INPUT_COLUMN_VIEW=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[3]/td[2]/div/input[1]") #ввод отображени
  TYPE_STRING=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/div/div/div/div/ul/li/div[4]/span") #тип строка
  KONSTRUCTOR=(By.XPATH,"/html/body/div[1]/div/div[2]/ul/li[1]/a") #Раздел конструктор
  FIRST_ROW=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/div") #первая строка в таблице
  EDIT_ORDER=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td/div/div/div[4]")#редактировать таблицу заказ
  SETTING_TABLE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[3]/tr/th/a") # настройка тида данных "таблица"
  TAKE_DATA=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[4]/tr[1]/td[2]/div/div") #взять данные
  INPUT_TAKE_DATA=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[4]/tr[1]/td[2]/div/div/input[1]")# ввод двнных взять данные из
  POSITION_TAKE_DATA=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[4]/tr[1]/td[2]/div/div/ul/li/div[3]/span") #выбор позиции
  VIEW_DATA = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[4]/tr[2]/td[2]/div/div[1]/span") #В текущей таблице отобразить поле
  INPUT_VIEW_DATA = (By.XPATH,  "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[4]/tr[2]/td[2]/div/input[1]") #ввод в текущей таблице отобразить поле
  POSITION_VIEW_DATA = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[4]/tr[2]/td[2]/div/ul/li/div[4]/span") #выбор позиции
  MANY_CHOICE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[5]/td[2]/div") #Множественный выбор
  EDIT_TABLE1=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[6]/td/div/div/div[4]/a") #редактирование таблицы 1
  TRANSLITION_TABLE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[8]/tr[5]/td[2]/div")# Настроить переход в другую таблицу
  TRANSLITION=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[8]/tr[6]/td[2]/div/div[1]") #переход в таблицу
  INPUT_TRANSLITION_TABLE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[8]/tr[6]/td[2]/div/input[1]") # ввод переход в таблицу
  TRANSLITION_FROM=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[8]/tr[7]/td[2]/table/tbody/tr[2]/td[1]/div/div[1]")#перевод из
  INPUT_TRANSLITION_FROM=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[8]/tr[7]/td[2]/table/tbody/tr[2]/td[1]/div/input[1]")#ввод перевод из
  TRANSLITION_TO=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[8]/tr[7]/td[2]/table/tbody/tr[2]/td[3]/div/div[1]") #перевод в
  INPUT_TRANSLITION_TO=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[8]/tr[7]/td[2]/table/tbody/tr[2]/td[3]/div/input[1]")# ввод перевод в
  ADD_EDITDORM=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[5]/tr[4]/td[2]/div")#Настройки справочника/Разрешить добавление в форме редактирования

  EDITS_TABLE=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/a") # шестеренка у имени таблицы
  DELETE_TABLE=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/table/tbody/tr[9]/td[2]/a") #кнопка удалить таблицу
  INPUT_NAME_TABLE_DELETE=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/form/div/input") #ввести название таблицы для удаление
  DELETE_BUTTON_TABLE=(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/button[2]") #кнопка удаление таблицы
  ERRORS_TEXT=(By.XPATH,"/html/body/div[1]/div/div/alert-modal/div/alert-slider/table/tbody/tr/td[2]") # текст с ошибкой

  STRING_DOWN=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[3]/div/div/div/div/ul/li/table/tbody/tr/td[3]/div/i[5]") #перенести строку вниз
  fix=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[6]/tr[7]/td[2]/div") #закрепить строчку строчку
  STATUS=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[1]/div/div") #строчка статус
  CHECKBOX_STATUS=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div/table/tbody/tr/td[2]/div") #чек бокс не использовать статус
  CHANGE_DIMENSION=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[6]/tr[5]/td[2]/div/div[1]/span/span[2]") #изменение ширины
  DIMENSION12=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[6]/tr[5]/td[2]/div/ul/li/div[14]/span") #ширина 12/12
  SETTING_DEVELOP=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[9]/tr[1]/th/a") #настройки разработки
  SAMPLE_CELL=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[9]/tr[5]/td[2]/div/div[1]/span") #шаблон ячейки
  INPUT_SAMPLE_CELL=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[9]/tr[5]/td[2]/div/input[1]") # ввод шаблон ячейки
  EDIT_DATA_WINDOW=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/table/tbody/tr[4]/td[2]/div/ins")# чек бокс редактировать данные в окне
  EDIT_DATA_TABLE=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/table/tbody/tr[5]/td[2]/div/ins")#чек бокс Редактировать данные прямо в таблице
  ACCEPT=(By.XPATH,"/html/body/div[1]/div/div/div[3]/button[1]") #применить
  ELEVENTH_ROW = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/ul/li[12]/div/div/div/div")  # одинадцатая строка
  CHECK_UNIQUE = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[2]/td/div/div/div[2]/div/ins")  # чек бокс уникальное
  CHECK_REQUIRED = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[2]/tr[2]/td/div/div/div[4]/div/ins")  # чек бокс уникальное
  SAVE_AS=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div[3]/a[2]") #сохранить как
  NAMES_COPY_NAMES=(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/form/div/input") #вписать имя таблицы
  SAVES=(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/button[2]") #сохранить после сохранить как
  ALIAS_TABLE_NAME=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/input") #alias имени таблицы
  ALIAS_ROW_NAME=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/table/tbody[9]/tr[2]/td[2]/input") #alias имени строуи










