import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.development_locator import Reports as dev
from locators.development_locator import CLIENTPROGRAMMING as clpro
from locators.development_locator import SERVERPROGRAMMING as serpro


class Test_Development(BasePage):

    def create_DHTML(self):  # 1.Создание DHTML страниц
        self.Iframe()
        self.element_is_present(clpro.ADD).click()
        names = self.RandomName("Тестовая страница")
        print(names)
        self.element_is_visible(clpro.NAMES_DHTML).send_keys(names)
        self.element_is_visible(clpro.HTML).click()
        self.element_is_visible(clpro.INPUT_DHTML).send_keys(
            '<div class="page-header"><h3> Список пользователей </h3></div><div class="panel"><div class="form-inline"><div class="form-group"><div class="col-md-6"><input class="form-control" ng-model="fio" placegolder="ФИО"/></div></div> <div class="form-group"><div class="col-md-6"><input class="form-control" ng-model="department" placegolder="Отдел"/></div></div><div class="form-group"><div class="col-md-offset-2-col-md-8"><button class="form-control" ng-click="additem(fio,department)">Добавить</button> </div></div><table class="table table-striped"><thread><tr><th> ФИО </th><th> Отдел </th></tr></thread><tbody><tr ng-repeat="item in list.items"><td> {{item.fio}} </td><td> {{item.department}} </td></tr></tbody></table></div>')
        self.element_is_visible(clpro.JS).click()
        self.element_is_visible(clpro.INPUT_DHTML).send_keys(
            'reportsystemModule.controller["userEditorCtrl",["$scope","$state","$stateParams",function($scope,$state,$stateParams)val model={items:[{fio:"Иванов И.И",department:"Отдел продаж"},{fio:"Петров П.П",department:"Отдел продаж"},{fio:"Иванова ",department:"Бугалтерия"}, ]};$scope.list=model;$scope.additem=function(fioAdded,departmentAdded){ $scope.list.items.push {{      fio:fioAdded}department:departmentAdded });}}}};')
        self.element_is_visible(clpro.ROUTE).click()
        self.element_is_visible(clpro.ADD_ROUTE).click()
        self.element_is_visible(clpro.STATE_INPUT).send_keys("main.testDHTML")
        self.element_is_visible(clpro.URL_INPUT).send_keys("/testDHTML")
        self.element_is_visible(clpro.CONTROLLER_INPUT).send_keys("usersEditorCtrl")
        self.element_is_visible(clpro.NAMES_INPUT).send_keys(names)
        self.element_is_visible(clpro.SAVE).click()
        self.element_is_visible(clpro.CLOSE).click()

    def edit_DHTML(self):  # 2.Редактирование DHTML страниц
        self.Iframe()
        self.element_is_visible(clpro.EDIT).click()
        self.element_is_visible(clpro.HTML).click()
        self.element_is_visible(clpro.HTML).click()
        html = self.element_is_visible(clpro.INPUT_DHTML)
        html.clear()
        html.send_keys(
            '<div class="page-header"><h3> Список cотрудников </h3></div><div class="panel"><div class="form-inline"><div class="form-group"><div class="col-md-6"><input class="form-control" ng-model="fio" placegolder="ФИО"/></div></div> <div class="form-group"><div class="col-md-6"><input class="form-control" ng-model="department" placegolder="Отдел"/></div></div><div class="form-group"><div class="col-md-offset-2-col-md-8"><button class="form-control" ng-click="additem(fio,department)">Добавить</button> </div></div><table class="table table-striped"><thread><tr><th> ФИО </th><th> Отдел </th></tr></thread><tbody><tr ng-repeat="item in list.items"><td> {{item.fio}} </td><td> {{item.department}} </td></tr></tbody></table></div>')
        self.element_is_visible(clpro.SAVE).click()
        self.element_is_visible(clpro.CLOSE).click()

    def delete_DHTML(self):  # 3 Удаление DHTML страниц
        self.Iframe()
        self.delete_first_row_client_programming()

    def create_actions_string(self):  # 4 Действия над строками
        self.Iframe()
        self.element_is_visible(clpro.ACTIONS_STRING).click()
        self.element_is_visible(clpro.ADD).click()
        names = self.RandomName("Тестовая действие")
        print(names)
        self.element_is_visible(clpro.NAMES_ACTION).send_keys(names)
        self.element_is_visible(clpro.BUTTON_NAMES_ACTION).send_keys("TestAction")
        self.element_is_visible(clpro.CHECKBOX_SHOW_GRID).click()
        self.element_is_visible(clpro.INPUT_ACTION).send_keys("alert('hello world'); ")
        self.element_is_visible(clpro.SAVE).click()

    def create_right_on_string(self):  # 5.Создание команд над строками
        self.Iframe()
        self.element_is_visible(clpro.RIGHT_ON_STRING).click()
        self.element_is_visible(clpro.ACTION).click()
        self.element_is_visible(clpro.INPUT_ACT).send_keys("Тестовая действие_c108cc6b-af05-42ff-8d13-ec7117da7b0f")
        self.element_is_visible(clpro.FIRST_ACTION_VARIANT).click()
        self.element_is_visible(clpro.TABLE).click()
        self.element_is_visible(clpro.INPUT_TABLE).send_keys("Справочник 31.03.2023")
        self.element_is_visible(clpro.FIRST_TABLE_VARIANT).click()
        self.element_is_visible(clpro.STATUS).click()
        self.element_is_visible(clpro.INPUT_STATUS).send_keys("Черновик")
        self.element_is_visible(clpro.FIRST_STATUS_VARIANT).click()
        self.element_is_visible(clpro.TABLE).click()
        table=self.element_is_visible(clpro.INPUT_TABLE)
        self.clear_text(table)
        table.send_keys("Справочник 31.03.2023")
        self.element_is_visible(clpro.ROLE).click()
        self.element_is_visible(clpro.INPUT_ROLE).send_keys("Тестовая роль GR1")
        self.element_is_visible(clpro.FIRST_ROVE_VARIANT).click()
        self.element_is_present(clpro.CHECKBOX_DRAFT).click()
        self.element_is_visible(clpro.SAVE_RIGHT_ON_STRING).click()


    def edit_actions_string(self):  # 6 Редактировнаие действия над строками
        self.Iframe()
        self.element_is_visible(clpro.ACTIONS_STRING).click()
        self.element_is_visible(clpro.EDIT).click()
        html = self.element_is_visible(clpro.INPUT_ACTION)
        self.clear_text(html)
        html.send_keys("alert('bye bye'); ")
        self.element_is_visible(clpro.SAVE).click()

    def delete_actions_string(self):  # 7 удаление действия над строками
        self.Iframe()
        self.element_is_visible(clpro.ACTIONS_STRING).click()
        self.delete_first_row_client_programming()

    def create_js_trigger(self):  # 8 создание js тригера
        self.Iframe()
        self.element_is_visible(clpro.JS_TRIGGER).click()
        self.element_is_visible(clpro.ADD).click()
        names = self.RandomName("Тестовый триггер")
        print(names)
        self.element_is_visible(clpro.NAMES_JS_TRIGGER).send_keys(names)
        self.element_is_visible(clpro.STATE_JS_TRIGGER).send_keys("main")
        self.element_is_visible(clpro.CODE_JS_TRIGGER).send_keys("alert('Что-то произошло в клиентском триггере');")
        self.element_is_visible(clpro.SAVE).click()

    def edit_js_trigger(self):  # 9 редактирование js тригера
        self.Iframe()
        self.element_is_visible(clpro.JS_TRIGGER).click()
        self.element_is_visible(clpro.EDIT).click()
        code = self.element_is_visible(clpro.CODE_JS_TRIGGER)
        self.clear_text(code)
        code.send_keys("alert('Произошло что-то ужасное');")
        self.element_is_visible(clpro.SAVE).click()

    def delete_js_trigger(self):  # 10 удаление js тригера
        self.Iframe()
        self.element_is_visible(clpro.JS_TRIGGER).click()
        self.delete_first_row_client_programming()

    def create_dynamic_API(self):  # 11 Добавление динамического API
        self.Iframe_Server()
        self.element_is_visible(serpro.ADD).click()
        names = self.RandomName("user_getTestResul")
        print(names)
        self.element_is_visible(serpro.INPUT_DYNAMIC_NAMES).send_keys(names)
        self.element_is_visible(serpro.INPUT_DYNAMIC_CODE).send_keys(
            "var result = userMath.getSum (2, 3);dynamicApi.setValue('receivables', result);")
        self.element_is_visible(clpro.SAVE).click()

    def edit_dynamic_API(self):  # 12 редактирование динамического API
        self.Iframe_Server()
        self.element_is_visible(clpro.EDIT).click()
        code = self.element_is_visible(serpro.INPUT_DYNAMIC_CODE)
        self.clear_text(code)
        code.send_keys("var result = userMath.getSum (2, 8);dynamicApi.setValue('receivables', result);")
        self.element_is_visible(clpro.SAVE).click()

    def delete_dynamic_API(self):  # 13 удаление динамического API
        self.Iframe_Server()
        self.delete_first_row_client_programming()

    def create_tasks(self):  # 14  создания задания
        self.Iframe_Server()
        self.element_is_visible(serpro.TASKS).click()
        self.element_is_visible(serpro.ADD).click()
        names = self.RandomName("Задание")
        print(names)
        self.element_is_visible(serpro.INPUT_TASKS).send_keys(names)
        self.element_is_visible(serpro.IN_TRANSATION).click()
        self.element_is_visible(serpro.INPUT_IN_TRANSATION).send_keys("userMath.getConversion(3,4);")
        self.element_is_visible(clpro.SAVE).click()

    def edit_tasks(self):  # 15  редактирование задания
        self.Iframe_Server()
        self.element_is_visible(serpro.TASKS).click()
        self.element_is_visible(clpro.EDIT).click()
        code = self.element_is_visible(serpro.INPUT_IN_TRANSATION)
        self.clear_text(code)
        code.send_keys("userMath.getConversion(0,0);")
        self.element_is_visible(clpro.SAVE).click()

    def delete_tasks(self):  # 16 удаление задания
        self.Iframe_Server()
        self.element_is_visible(serpro.TASKS).click()
        self.delete_first_row_client_programming()

    def create_server_function(self):  # 17 создание серверной функции
        self.Iframe_Server()
        self.element_is_visible(serpro.SERVER_FUNCTION).click()
        self.element_is_visible(serpro.ADD_SERVER_FUNCTION).click()
        names = self.RandomName("UserMath")
        print(names)
        self.element_is_visible(serpro.INPUT_OBJECT).send_keys(names)
        self.element_is_visible(serpro.INPUT_METHOD).send_keys("getSum")
        self.element_is_visible(serpro.INPUT_DESCRIPTION).send_keys("получает сумму двух переданных параметров")
        self.element_is_visible(serpro.INPUT_CODE).send_keys("function getSum(a, b){ return a+b; }")
        self.element_is_visible(clpro.SAVE).click()

    def edit_server_function(self):  # 18 редактирование серверной функции
        self.Iframe_Server()
        self.element_is_visible(serpro.SERVER_FUNCTION).click()
        self.element_is_visible(serpro.SHOW_All).click()
        self.element_is_visible(serpro.EDIT).click()
        code = self.element_is_visible(serpro.INPUT_CODE)
        self.clear_text(code)
        code.send_keys("function getSum(a, b){ return a-b; }")
        self.element_is_visible(clpro.SAVE).click()

    def delete_server_function(self):  # 19 удаление серверной функции
        self.Iframe_Server()
        self.element_is_visible(serpro.SERVER_FUNCTION).click()
        self.element_is_visible(serpro.SHOW_All).click()
        self.element_is_visible(serpro.DELETE).click()
        self.element_is_visible(clpro.YES_DELETE).click()

    def create_sample_cell(self):  # 20 создание шаблона ячейки
        self.Iframe()
        self.element_is_visible(clpro.SAMPLE_CELL).click()
        self.element_is_visible(clpro.ADD).click()
        names = self.RandomName("Округление")
        print(names)
        self.element_is_visible(clpro.NAMES_SAMPLE_CELL).send_keys(names)
        self.element_is_visible(clpro.CHOICE_FIELD).click()
        self.element_is_visible(clpro.FLOAT).click()
        self.element_is_visible(clpro.CHOICE_TYPE).click()
        self.element_is_visible(clpro.CELL).click()
        self.element_is_visible(clpro.INPUT_HTML_CELL).send_keys("<span>{{round(value.DisplayValue,2)}}</span>")
        self.element_is_visible(clpro.JS_CELL).click()
        self.element_is_visible(clpro.JS_INPUT).send_keys( "$scope.round=function(number,digitsNumber){if(number===null|| digitsNumber===null)return null;var digits=Math.pow(10,digitsNumber);return Math.round(number*digits)/digits;};")
        self.element_is_visible(clpro.SAVE).click()

    def edit_sample_cell(self):  # 21 редактирование ячейки шаблона
        self.Iframe()
        self.element_is_visible(clpro.SAMPLE_CELL).click()
        self.element_is_visible(clpro.EDIT).click()
        code = self.element_is_visible(clpro.INPUT_HTML_CELL)
        self.clear_text(code)
        code.send_keys("<span>{{round(value.DisplayValue,4)}}</span>")
        self.element_is_visible(clpro.SAVE).click()

    def delete_sample_cell(self):  # 23 удаление ячейки шаблона
        self.Iframe()
        self.element_is_visible(clpro.SAMPLE_CELL).click()
        self.delete_first_row_client_programming()

    def table_reports(self):  # 25. создания отчета
        self.element_is_visible(dev.DEVELOPMENT).click()
        self.element_is_visible(dev.REPORTS).click()
        self.element_is_visible(dev.ADD_REPORTS).click()
        names = self.RandomName("Test1")
        print(names)
        self.element_is_visible(dev.NAMES_REPORTS).send_keys(names)
        self.element_is_visible(dev.THEME_REPORTS).send_keys("Просмотр данных из таблицы справочник")
        self.element_is_visible(dev.CHOICE_DATA).click()
        self.element_is_visible(dev.INPUT_DATA).send_keys("31.03.2023")
        self.element_is_visible(dev.FIRST_DATA).click()
        self.element_is_visible(dev.CHOICE_ROLE).click()
        self.element_is_visible(dev.INPUT_ROLE).send_keys("admin")
        self.element_is_visible(dev.FIRST_ROLE).click()
        self.element_is_visible(dev.CHOICE_ROLE).click()
        self.element_is_visible(dev.ADD_FIELD).click()
        self.element_is_visible(dev.FIRST_ROW).click()
        name=self.element_is_visible(dev.NAMES_FIELD)
        name.clear()
        name.send_keys("Строка")
        base = self.element_is_visible(dev.NAME_IN_BASE)
        base.clear()
        base.send_keys("Строка")
        self.element_is_visible(dev.ADD_FIELD).click()
        self.element_is_visible(dev.SECOND_ROW).click()
        name = self.element_is_visible(dev.NAMES_FIELD)
        name.clear()
        name.send_keys("Многострочная строка")
        base = self.element_is_visible(dev.NAME_IN_BASE)
        base.clear()
        base.send_keys("Многострочная строка")
        self.element_is_visible(dev.TYPE).click()
        self.element_is_visible(dev.MANY_STRING).click()
        self.element_is_visible(dev.ADD_FIELD).click()
        self.element_is_visible(dev.THIRD_ROW).click()
        name = self.element_is_visible(dev.NAMES_FIELD)
        name.clear()
        name.send_keys("Дата")
        base = self.element_is_visible(dev.NAME_IN_BASE)
        base.clear()
        base.send_keys("Дата")
        self.element_is_visible(dev.TYPE).click()
        self.element_is_visible(dev.DATE).click()
        self.element_is_visible(dev.REQUEST).click()
        self.element_is_visible(dev.SQL).click()
        self.element_is_visible(dev.INPUT_SQL).send_keys("select tbl.[Строка] as [Строка]tbl.[Многострочная строка] as [Многострочная строка],tbl.[Дата] as [Дата],from nsi_view.[Справочник 31.03.2023] tbl")
        self.element_is_visible(dev.SAVE_REPORTS).click()

    def check_reports(self):  # 26 проверка просмотра и скачивания
        self.element_is_visible(dev.DEVELOPMENT).click()
        self.element_is_visible(dev.REPORTS).click()
        self.element_is_visible(dev.FIRST_REPORT).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.element_is_visible(dev.EXPORT_EXCEL).click()


    def Iframe(self):
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))

    def Iframe_Server(self):
        self.element_is_visible(serpro.DEVELOPMENT).click()
        self.element_is_visible(serpro.SERVER_PROGRAMMING).click()
        self.driver.switch_to.frame(self.element_is_visible(serpro.IFRAME))
        self.driver.switch_to.frame(self.element_is_visible(serpro.IFRAME))

    def delete_first_row_client_programming(self):
        self.element_is_visible(clpro.DELETE).click()
        self.element_is_visible(clpro.YES_DELETE).click()
