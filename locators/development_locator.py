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


