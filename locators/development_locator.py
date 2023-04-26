from selenium.webdriver.common.by import By

class Reports:
    DEVELOPMENT=(By.XPATH,"/html/body/div/div/div[2]/ul/li[8]/a") #Разработка
    REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[1]/ul/li[3]/a")  #Отчеты
    SERVER_PROGRAMMING=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[1]/ul/li[2]/a/span") #Серверное программироние
    PRINTS_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[1]/ul/li[2]/a") #Печатные отчеты
    ADD_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table[1]/tbody/tr/td[3]") #Добавить отчет
    NAMES_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[1]/input")#Имя отчета
    THEME_REPORTS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/form/ul/li[2]/textarea")#Тема отчета
    CHOICE_DATA=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/button/span[1]")#Выбор данных
    REPORTS_FIRST=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table[2]/tbody/tr/td[1]/a") #Первыйотчет

class CLIENTPROGRAMMING:
    DEVELOPMENT = (By.XPATH, "/html/body/div/div/div[2]/ul/li[8]/a")  # Разработка
    ADD_DHTML=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[1]/div[1]/button") #Добавить DHTML
    ADD_DHTML2=(By.CLASS_NAME,"pi pi-plus-circle p-button-icon") #Добавить DHTML
    NAMES_DHTML=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") #имя DHTML
    HTML=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/ul/li[2]") #HTML
    INPUT_DATA=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[5]") # Ввод HTML
    JS=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/ul/li[3]") #JS
    ROUTE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/ul/li[4]") #маршрутор
    ADD_ROUTE=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]/button/span[1]") #Добавить маршрут
    STATE_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/input")# ввод state
    URL_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/input") #ввод url
    CONTROLLER_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[4]/input") #ввод controller
    NAMES_INPUT=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[5]/input") #ввод имени
    SAVE_DHTML=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/button[1]") #Cохранить
    CLOSE=(By.XPATH,"/html/body/div[3]/div/div[1]/div/button/span[1]") #Закрыть
    SERVER_PROGRAMMING=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[1]/ul/li[2]/a")
    EDIT=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/div/button[1]")
    DELETE=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/div/button[2]")
    YES_DELETE=(By.XPATH,"/html/body/div[3]/div/div[3]/button[2]") #Да, удалить
    ACTIONS_STRING=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/ul/li[2]/a") #Дейсвия над строками
    ADD_ACTIONS_STRING=(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[1]/div[1]/button") # добавить Дейсвиия над строками
    NAMES_ACTION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/input") #имя действий над строками
    BUTTON_NAMES_ACTION=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[4]/input") #имя кнопки действий над строками
    CHECKBOX_SHOW_GRID=(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/div[2]") #чекбокс показать грид









