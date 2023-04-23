from selenium.webdriver.common.by import By


class Menu:
    MENU=(By.XPATH,"/html/body/div/div/div[2]/ul/li[4]/a") #Меню
    ADD_MENU=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/span[2]/button") #Добавить пункт меню
    SECOND_ROW=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/ul/li[2]") #Вторая строка
    NAMES=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[2]/tr[1]/td[2]/input") #Название
    URL=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[2]/tr[2]/td[2]/input") #Ссылка
    CHOICE_ROLE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[2]/tr[3]/td[2]/div/div/button")  #ВЫбрать роль
    INPUT_CHOICE_ROLE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[2]/tr[3]/td[2]/div/div/ul/li[4]/div/input")  #ввод роли
    FIRST_CHOICE_ROLE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[2]/tr[3]/td[2]/div/div/ul/li[6]/a")  #первый вариант
    CHOICE_ICON=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[2]/tr[4]/td[2]/div/div[2]/div/div[1]/span") #Выбрать иконку
    ICON=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[2]/tr[4]/td[2]/div/div[2]/div/ul/li/div[6]/span") # иконка
    ADDITIONAL_SETTING=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[3]/tr/th/a") #Доп. Настройки
    CHOICE_FOLDER=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[4]/tr[1]/td[2]/div/div/button/span[1]") # выбрать каталог
    INPUT_CHOICE_FOLDER=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[4]/tr[1]/td[2]/div/div/ul/li[4]/div/input") # ввод каталог
    SAVE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/a") #Сохранить
    THIRD_ROW=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/ul/li[3]") #Третья строка
    FOURTH_ROW=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/ul/li[4]") #четвертая строка
    FIRST_FOLDER_VARIANT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/table/tbody[4]/tr[1]/td[2]/div/div/ul/li[6]/a") #Выбрать первую папку
    DELETE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/ul/li[4]/div/div/div/ul/li/table/tbody/tr/td[2]/div/i[5]") #Удалить
