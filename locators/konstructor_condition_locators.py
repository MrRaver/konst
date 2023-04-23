from selenium.webdriver.common.by import By

class Konstructor_Condition_Locators_save:
    TEST1_EDITS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[9]/td/div/div/div[4]/a") #редактировать тест1
    KONSTRUCTOR_CONDITION=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[5]/a/span/span")#конструктор условий
    ADD_CONTITION=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[2]/panel-body/condition-table/table/thead/tr/th[4]/a") #Добавить  условие
    NAMES_CONDITION=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/div/div[1]/div/input") #Название условия
    CONDITION_SAVE_INSTALLER=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/div/div[2]/div/div/div/button") #Сохранение строки при условии
    TEXT_ERROR_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/div/div[3]/div/textarea") #Текст ошибки
    ADD_GROUP_FILTERS=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div/a[2]") #Добавить группу фильтров
    ADD_FILTERS=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div/a[1]") #Добавить фильтр

    ALREADY=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/div/div[2]/div/div/div/ul/li[6]/a") #готов, при условия строку можно сохранить
    OR_FIRST_ROWS=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[1]/div[2]/label/input")#первая или
    ADD_FILTERS_TWO_ROWS=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[1]/a[1]") #Добавить фильтр 2 строка

    FIRST_ROW_SECOND_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]/span/span[2]")#первая строка второй
    FIRST_ROW_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]") #первая строка четвертая
    FIRST_ROW_FIFTH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[2]/input")  #первая строка пятая

    SECOND_ROW_SECOND_INPUT = (By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]/span/span[2]")  #вторая строка второй
    SECOND_ROW_THIRD_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[2]/div/div[1]/span") #вторая строка третий
    SECOND_ROW_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]")  #вторая строка четвертая
    SECOND_ROW_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/input")  #вторая строка пятая
    INPUT_EQUALS=(By.XPATH,"/html/body/div[4]/input[1]") #Ввод даннных

    ADD_GROUP_FILTERS3=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[1]/a[2]") #Добавить группу фильтров в 3 строке
    ADD_FILTERS3=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[1]/a[1]") #Добавить фильтр в 3 строке
    OR_THIRD_ROWS=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div/div[2]/label/input") #или в 3 строке
    ADD_FILTERS4=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div[1]/a[1]")#Добавить фильтр в 4 строке
    NOT_EQUALS=(By.XPATH,"/html/body/div[4]/ul/li/div[4]/span") # не равно
    ADDITIONAL=(By.XPATH,"/html/body/div[4]/ul/li/div[7]/span") #справочник

    THIRD_ROW_SECOND_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]/span/span[2]") #третья строка второй
    THIRD_ROW_THIRD_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[2]/div/div[1]/span/span[2]") #третья строка третья
    THIRD_ROW_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]")#третья строка четвертая
    THIRD_ROW_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[2]/input") #третья строка пятая

    FOURTH_ROW_SECOND_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]") #четвертая строка второй
    FOURTH_ROW_THIRD_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[2]/div/div[1]") #четвертая строка третий

    FIFTH_ROW_SECOND_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]/span/span[2]") #пятая строка второй
    FIFTH_ROW_THIRD_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[3]/condition-item/div/div/div[2]/div/div[1]/span/span[2]") #пятая строка третий
    FIFTH_ROW_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]") #пятая строка четвертая
    FIFTH_ROW_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/input") #пятая строка пятый
    SAVE_CONDITION=(By.XPATH,"/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[3]/ul/li[2]/button") #сохранить
    SAVE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/div/button") #точно сохранить

class Konstructor_Condition_Locators_edit:
    TEST1_EDITS = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[9]/td/div/div/div[4]/a")  # редактировать тест1
    KONSTRUCTOR_CONDITION = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[5]/a/span/span")  # конструктор условий
    EDITS_CONDITION=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[1]/panel-title/ul/li[2]/a") #Редактирование конструктор условий
    ADD_CONTITION = (By.XPATH,
                     "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[2]/panel-body/condition-table/table/thead/tr/th[4]/a")  # Добавить  условие
    OR_SECOND_ROWS=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div/div[2]/label/input") #или во строке  редактирование

    ADD_GROUP_FILTERS_EDIT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div/a[2]") #Добавить группу фильтров в редактирование
    ADD_FILTERS_EDIT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div/a[1]") #Добавить фильтр в редактирование
    ADD_FILTERS_EDIT2=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[1]/a[1]") #Добавить фильтр во второй строке в редактирование
    EDITS_NAME_CONDITION=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/div/div[1]/div/input") #Название условия в редактирование
    EDITS_ROW=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/div/div[2]/div/div/div/button") #выбрать столбец в редактирование
    INPUT_EDITS_ROW=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/div/div[2]/div/div/div/ul/li[4]/div/input")  #ввести столбец в редактирование
    INPUT_FIRST_EDITS_ROW=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/div/div[2]/div/div/div/ul/li[6]/a")  #выбор первого по поиску столбец в редактирование


    EDIT_FIRST_SECOND_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]/span/span[2]/span") #первая строка второй элемент редактирования
    EDIT_FIRST_THIRD_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[2]/div/div[1]/span/span[2]/span") #первая  строка третий элемент редактирования
    EDIT_SECOND_SECOND_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]/span/span[2]/span") #вторая строка второй элемент редактирования
    EDIT_SECOND_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span") #вторая строка четвертый элемент редактирования
    EDIT_SECOND_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/input") #вторая строка пятый элемент редактирования
    EDIT_THIRD_FIRST_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[1]/div/div[1]/span") #третья строка первый элемент редактирования
    EDIT_THIRD_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]/span") #третья строка четвертый элемент редактирования
    EDIT_THIRD_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/div/div[1]/span/span[2]/span") #третья строка пятый элемент редактирования
    INPUT_TEXT=(By.XPATH,"/html/body/div[4]/input[1]")
    SAVE_CONDITION = ( By.XPATH, "/html/body/div[1]/div/div/edit-predicate-editor/modal-wnd/div[3]/ul/li[2]/button")  # сохранить
    SAVE = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/div/button")  # точно сохранить
class Konstructor_Condition_Locators_status:
    TEST1_EDITS = (By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[9]/td/div/div/div[4]/a")  # редактировать тест1
    KONSTRUCTOR_CONDITION = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[5]/a/span/span")  # конструктор условий
    TRANSLITION_STATUS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[1]/panel-title/ul/li[3]/a") #Перевод в статусы
    ADD_STATUS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[2]/panel-body/condition-table/table/thead/tr/th[4]/a") #Добавить статус
    NAMES_TRANSLITION_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/div/div[1]/div/input") #Название условие перевода в статус
    TEXT_ERROR_TRANSLITION_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/div/div[2]/div/textarea") #Текст ошибки строки в статусе
    CHOISE_TRANSLITION_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/div/div[3]/div/div/div/button") #Выбрать статус
    INPUT_CHOISE_TRANSLITION_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/div/div[3]/div/div/div/ul/li[4]/div/input") #Ввод статуса
    ENTER_CHOISE_TRANSLITION_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/div/div[3]/div/div/div/ul/li[6]/a") #Выбрать первый статус
    FIRST_OR_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div/div[2]/label/input") #Первое или
    ADD_GROUP_FILTERS_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div/a[2]") #Первое добавить группу фильтров
    ADD_FILTERS_STATUS=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div/a[1]") #Первое добавить фильтр
    ADD_FILTERS_STATUS2=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div/a[1]") #Первое добавить фильтр
    STATUS_FIRST_FIRST_INPUT=(By.XPATH,"/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[1]/operand/div/div[1]/div/div[1]/span/span[2]/span") #Первая строка первый элемент
    INPUT_TEXT=(By.XPATH,"/html/body/div[4]/input[1]") #ВВод текста
    STATUS_FIRST_FOURTH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span")  #Первая строка четвертый элемент
    STATUS_SECOND_SECOND_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[2]/div/div[1]/span/span[2]")  #вторая строка второй элемент
    STATUS_SECOND_THIRTH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[2]/div/div[1]/span/span[2]")  #вторая строка третий элемент
    STATUS_SECOND_FOURTH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span")  #вторая строка четвертый элемент
    STATUS_SECOND_FIFTH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/input")  #вторая строка пятый элемент
    STATUS_THIRD_FIRST_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[1]/div/div[1]/span")  #третья строка первый элемент
    STATUS_THIRD_FOURTH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]/span")  #третья строка четвертый элемент
    STATUS_THIRD_FIFTH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/div/div[1]/span/span[2]/span")  #Третья строка пятый элемент
    SAVE_CONDITION = (By.XPATH, "/html/body/div[1]/div/div/status-transmit-condition-editor/modal-wnd/div[3]/ul/li[2]/button")  # сохранить
    SAVE = (By.XPATH,  "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/div/button")  # точно сохранить

class Konstructor_Condition_Locators_filter_directory:
    EDITS_TABLE_PNPPK=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[11]/td/div/div/div[4]") #редактирование таблицы тип изделия ПНППК
    KONSTRUCTOR_CONDITION = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[5]/a/span/span")  # конструктор условий
    FILTERS_DIRECTORY=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[1]/panel-title/ul/li[4]/a") #Фильтрация в качестве справочника
    ADD_FILTERS_DIRECTORY=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[2]/panel-body/condition-table/table/thead/tr/th[4]/a") # Добавить Фильтрация в качестве справочника
    NAMES_FILTERS_DIRECTORY=(By.XPATH,"/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[2]/body-block/div/div[1]/div/input") # имяФильтрация в качестве справочника
    CHOICE_DATA=(By.XPATH,"/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[2]/body-block/div/div[2]/div/div/div/button") #Выбрать столбцы
    ALL_CHOICE=(By.XPATH,"/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[2]/body-block/div/div[2]/div/div/div/ul/li[1]/a") #Выбрать все столбцы
    ADD_FILTERS=(By.XPATH,"/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[1]/a[1]") #ДОбавить фильтр
    FILTERS_DIRECTORY_FIRST_THIRTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-item/div/div/div[2]/div/div[1]/span") #ПЕрвая строка третий элемент
    FILTERS_DIRECTORY_FIRST_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]/span") #ПЕрвая строка третий элемент
    FILTERS_DIRECTORY_FIRST_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[2]/input") #ПЕрвая строка пятый элемент
    INPUT_DATA=(By.XPATH,"/html/body/div[4]/input[1]") #Ввод данных
    SAVE_CONDITION = (By.XPATH,  "/html/body/div[1]/div/div/dictionary-filter-predicate-editor/modal-wnd/div[3]/ul/li[2]/button")  # сохранить
    SAVE = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/div/button")  # точно сохранить
class Konstructor_Condition_Locators_filter:
    TEST1_EDITS = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[9]/td/div/div/div[4]/a")  # редактировать тест1
    KONSTRUCTOR_CONDITION = ( By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[5]/a/span/span")  # конструктор условий
    FILTERS = ( By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[1]/panel-title/ul/li[5]/a")  # фильтрации
    FIRST_OR=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[1]/div[2]") #Первое имя
    ADD_FILTERS = (By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[2]/panel-body/condition-table/table/thead/tr/th[4]/a")  # Добавить Фильтрация в качестве справочника
    NAMES_FILTERS=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/div/div/div/input") # Название условия
    FILTERS_ADD_GROUP_FILTERS=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[1]/a[2]") #Добавить группу фильтров
    FILTERS_ADD_FILTERS=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[1]/a[1]") #Добавить фильтр
    FILTERS_ADD_FILTERS2=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[1]/a[1]") #Добавить фильтр
    FILTERS_FIRST_FIRST_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[1]/operand/div/div[1]/div/div[1]/span") #Первая строка первый элемент
    FILTERS_FIRST_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[2]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span/span[2]/span") #Первая строка первый элемент
    FILTERS_SECOND_FIRST_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[1]/div/div[1]/span/span[2]/span") # вторая строка первый элемент
    FILTERS_SECOND_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span") # вторая строка четвертый элемент
    FILTERS_SECOND_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[2]/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/div/div[1]/span/span[2]/span") # вторая строка четвертый элемент
    FILTERS_THIRD_FIRST_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[1]/operand/div/div[1]/div/div[1]/span/span[2]") # третья  строка первый элемент
    FILTERS_THIRD_THIRD_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[2]/div/div[1]/span") # третья  строка третий элемент
    FILTERS_THIRD_FOURTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[1]/div/div[1]/span") # третья  строка четвертый элемент
    FILTERS_THIRD_FIFTH_INPUT=(By.XPATH,"/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[2]/body-block/condition-manager/condition-group/div/div[3]/condition-item/div/div/div[3]/operand/div/div[2]/div/div[1]/span") # третья  строка четвертый элемент
    INPUT_DATA=(By.XPATH,"/html/body/div[4]/input[1]") #Ввод данных
    SAVE_CONDITION = (By.XPATH, "/html/body/div[1]/div/div/filter-condition-editor/modal-wnd/div[3]/ul/li[2]/button")  # сохранить
    SAVE = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/div/button")  # точно сохранить
    NOT_EQUALS = (By.XPATH, "/html/body/div[4]/ul/li/div[4]/span")  # не равно

class Konstructor_Condition_Locators_edits_predict:
    TEST1_EDITS = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[9]/td/div/div/div[4]/a")  # редактировать тест1
    KONSTRUCTOR_CONDITION = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[5]/a/span/span")  # конструктор условий
    ADD_CONTITION = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[2]/panel-body/condition-table/table/thead/tr/th[4]/a")  # Добавить  условие
    EDITS_SAVE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/panel/div/div[2]/panel-body/condition-table/table/tbody/tr/td[2]/a") #Редактирование
    TEXT_ERROR_INPUT = (By.XPATH, "/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[2]/body-block/div/div[3]/div/textarea")
    SAVE_CONDITION = (By.XPATH, "/html/body/div[1]/div/div/save-predicate-editor/modal-wnd/div[3]/ul/li[2]/button")  # сохранить
    SAVE = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/condition-constructor/div/button")  # точно сохранить





