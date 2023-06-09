import time

from selenium.webdriver import Keys, ActionChains

from pages.base_page import BasePage
from locators.filter_locator import Filtesr_Locators as filter

class Test_Filters(BasePage):
    def filter_additional(self):  #1.В гриде таблице для всех столбцов пофильтровать данные
        self.element_is_visible(filter.ADDITIONAL_EDIT).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        id=self.element_is_visible(filter.ID_INPUT)
        id.send_keys("5")
        id.send_keys(Keys.ENTER)
        id.clear()
        time.sleep(2)
        first=self.element_is_visible(filter.MANY_STRING_INPUT)
        first.send_keys("test2")
        first.send_keys(Keys.ENTER)
        first.clear()
        time.sleep(2)
        second = self.element_is_visible(filter.STRING_INPUT)
        second.send_keys("proba")
        second.send_keys(Keys.ENTER)
        second.clear()
        time.sleep(2)
        third = self.element_is_visible(filter.INTENGER_INPUT)
        third.send_keys("42")
        third.send_keys(Keys.ENTER)
        third.clear()
        time.sleep(2)
        fourth = self.element_is_visible(filter.FLOAT_INPUT)
        fourth.send_keys("13.22")
        fourth.send_keys(Keys.ENTER)
        fourth.clear()
        time.sleep(2)
        fifth = self.element_is_visible(filter.DATA_INPUT)
        fifth.send_keys("08.04.2023")
        fifth.send_keys(Keys.ENTER)
        fifth.clear()
        time.sleep(2)
        sixth = self.element_is_visible(filter.DATA_TIME_INPUT)
        sixth.send_keys("07.04.2023")
        sixth.send_keys(Keys.ENTER)
        sixth.clear()
        time.sleep(2)


    """ не работает def filter_table3(self):  # 2.Фильтрация данных в таблице
        self.element_is_visible(filter.TABLE3).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        id = self.element_is_visible(filter.TABLE3_ID_INPUT)
        id.send_keys("4")
        id.send_keys(Keys.ENTER)
        time.sleep(4)
        id = self.element_is_visible(filter.TABLE3_ID_INPUT)
        id.clear()
        firs = self.element_is_visible(filter.TABLE3_STRING_INPUT)
        firs.send_keys("ex")
        firs.send_keys(Keys.ENTER)
        time.sleep(4)
        firs = self.element_is_visible(filter.TABLE3_STRING_INPUT)
        firs.clear()
        secon = self.element_is_visible(filter.TABLE3_MANY_STRING_INPUT)
        secon.send_keys("tt")
        secon.send_keys(Keys.ENTER)
        time.sleep(4)
        secon = self.element_is_visible(filter.TABLE3_MANY_STRING_INPUT)
        secon.clear()
        thir = self.element_is_visible(filter.TABLE3_INTENGER_INPUT)
        thir.send_keys("10")
        thir.send_keys(Keys.ENTER)
        time.sleep(4)
        thir = self.element_is_visible(filter.TABLE3_INTENGER_INPUT)
        thir.clear()
        fourt = self.element_is_visible(filter.TABLE3_FLOAT_INPUT)
        fourt.send_keys("13.22")
        fourt.send_keys(Keys.ENTER)
        time.sleep(4)
        fourt = self.element_is_visible(filter.TABLE3_FLOAT_INPUT)
        fourt.clear()
        fifth = self.element_is_visible(filter.TABLE3_DATA_INPUT)
        fifth.send_keys("2023-04-07")
        fifth.send_keys(Keys.ENTER)
        time.sleep(4)
        fifth = self.element_is_visible(filter.TABLE3_DATA_INPUT)
        fifth.clear()
        sixth = self.element_is_visible(filter.TABLE3_DATA_TIME_INPUT)
        sixth.send_keys("Apr 7 2023 3:00PM")
        sixth.send_keys(Keys.ENTER)
        time.sleep(4)
        sixth = self.element_is_visible(filter.TABLE3_DATA_TIME_INPUT)
        sixth.clear()
        seventh = self.element_is_visible(filter.TABLE3_BOOLEAN_INPUT)
        seventh.send_keys("1")
        seventh.send_keys(Keys.ENTER)
        time.sleep(4)
        seventh = self.element_is_visible(filter.TABLE3_BOOLEAN_INPUT)
        seventh.clear()
    """

    def filter_additional_zakr(self):  # 1.Закрепление столбцов и сортировка (представление администратора)
        self.View()
        self.element_is_visible(filter.DATA).click()
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.VIEW_TABLE).click()
        self.element_is_visible(filter.CHECKBOX_STATUS).click()
        self.element_is_visible(filter.CHECKBOX_NUMBER).click()
        self.element_is_visible(filter.CHOICE_ORDER).click()
        self.element_is_visible(filter.ASCENDING).click()
        self.element_is_visible(filter.SAVE_VIEW).click()
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.SAVE_AS).click()
        names = self.RandomName("Тестовое представление 1")
        print(names)
        self.element_is_visible(filter.INPUT_NAME_VIEW).send_keys(names)
        self.element_is_visible(filter.SAVE_NAME_VIEW).click()
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.DEFAULT).click()


    def filter_additional_visible(self):  # 2.Скрытие столбцов и настройка ширины (представление администратора)
        self.View()
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.VIEW_TABLE1).click()
        self.element_is_visible(filter.VISIBLE).click()
        self.element_is_visible(filter.STATUS_VISIBLE).click()
        self.element_is_visible(filter.NUMBER_VISIBLE).click()
        self.element_is_visible(filter.MANY_STRING_VISIBLE).click()
        self.element_is_visible(filter.STRING_VISIBLE).click()
        self.element_is_visible(filter.LENGTH_STATUS).send_keys("200")
        self.element_is_visible(filter.SAVE_VIEW).click()
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.SAVE_AS1).click()
        names = self.RandomName("Тестовая представление")
        print(names)
        self.element_is_visible(filter.INPUT_NAME_VIEW).send_keys(names)
        self.element_is_visible(filter.SAVE_NAME_VIEW).click()
        time.sleep(2)
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.DEFAULT1).click()

"""
    def filter_additional_visible_and_move(self):  # 3.Скрытие столбцов и настройка ширины (представление администратора)
        self.View()
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.VIEW_TABLE2).click()
        self.element_is_visible(filter.INTENGER_VISIBLE).click()
        self.element_is_visible(filter.FLOAT_VISIBLE).click()
        status = self.element_is_present(filter.STATUS)
        data_edit = self.element_is_present(filter.DATA_EDIT)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(status, data_edit).perform()
        prelast = self.element_is_visible(filter.PRELAST)
        action_chains.drag_and_drop(data_edit, prelast).perform()
        data = self.element_is_visible(filter.DATA_ELEMENT)
        second = self.element_is_visible(filter.SECOND)
        action_chains.drag_and_drop(data, second).perform()
        action_chains.drag_and_drop(second, status).perform()
        self.element_is_visible(filter.SAVE_VIEW).click()
        self.element_is_visible(filter.ELLIPSIS).click()
        self.element_is_visible(filter.SAVE).click()
    """


def View(self):
    self.element_is_visible(filter.EDIT_ADDITIONAL).click()
    self.element_is_visible(filter.KONSTRUCTOR_CONDITION).click()
    self.element_is_visible(filter.VIEW).click()
















