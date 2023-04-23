from selenium.webdriver.common.by import By

class Other:
    ADMINIRIROVANIE=(By.XPATH,"/html/body/div/div/div[2]/ul/li[9]/a/span")#Админимтрирование
    SELECT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/div[1]/div/div[1]/span") #ВЫьор
    CONTROL_DATA=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/div[1]/div/ul/li/div[3]/span") #контроль дата
    SAVE=(By.CLASS_NAME,"fa fa-2x fa-save") #Сохранить

    MESSAGE=(By.XPATH,"/html/body/div[1]/div/div[2]/ul/li[5]/a") #Уведомления
    ADD_MESSAGE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[2]/div/div/div/div[3]/a")#Отпраить кведомления
    USERS=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/span/div/button")#Пользователи
    ADMIM=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/span/div/ul/li[7]/a")#админ
    TITLE=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[5]/input")#Тема
    ROLES=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/span/div/button")#Роли
    TEST_ROLE=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/span/div/ul/li[7]/a")#Тестовая роль
    TEXT=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[7]/text-angular/div[2]/div[3]")#Текст
    SITE=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/ins")#чек бокс на сайте
    MAIL=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div/ins")#Тчек бокс на почту
    SEND=(By.XPATH,"/html/body/div[1]/div/div/div[3]/button[1]") #Отправить


    #импортирование данных
    IMPORT_DATA=(By.XPATH,"/html/body/div/div/div[2]/ul/li[7]/a/span") #Импорт данных
    CHOICE_TABLE=(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td[1]/div/div[1]/span") #Выбор таблицы
    INPUT_CHOICE_TABLE=(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input[1]") #ввод таблицы
    CHOICE_EXCEL=(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/div/div/button") #Выбрать Excel файл
    CHOICE_EX=(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/input") #Выбрать Excel файл
    CHOICE_LIST=(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td[3]/div/div[1]/span/span[2]") #Выбрать страницу
    INPUT_CHOICE_LIST=(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td[3]/div/input[1]") #ВВод страницы
    IMPORT_BUTTON=(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[3]/div/table/tbody/tr/td[1]/button") #Импорт
    TEXT_RESULT=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div[3]/div/table/tbody/tr/td[2]/div") #Текст результат
