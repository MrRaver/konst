import time
import random
from datetime import date

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.development_locator import Reports as dev
from locators.development_locator import CLIENTPROGRAMMING as clpro


class Test_Development(BasePage):

    def create_DHTML(self):  # 1.Создание DHTML страниц
        self.autorization()
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))
        self.element_is_present(clpro.ADD_DHTML).click()
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
        self.autorization()
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))
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
        self.autorization()
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))
        self.element_is_visible(clpro.DELETE).click()
        self.element_is_visible(clpro.YES_DELETE).click()

    def create_actions_string(self):  # 4 Действия над строками
        self.autorization()
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))
        self.element_is_visible(clpro.ACTIONS_STRING).click()
        self.element_is_visible(clpro.ADD_ACTIONS_STRING).click()
        names = self.RandomName("Тестовая действие")
        print(names)
        self.element_is_visible(clpro.NAMES_ACTION).send_keys(names)
        self.element_is_visible(clpro.BUTTON_NAMES_ACTION).send_keys("TestAction")
        self.element_is_visible(clpro.CHECKBOX_SHOW_GRID).click()
        self.element_is_visible(clpro.INPUT_ACTION).send_keys("alert('hello world'); ")
        self.element_is_visible(clpro.SAVE).click()

    def create_right_on_string(self):  # 5.Создание команд над строками
        self.autorization()
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))
        self.element_is_visible(clpro.RIGHT_ON_STRING).click()
        self.element_is_visible(clpro.ROLE).click()
        self.element_is_visible(clpro.INPUT_ROLE).send_keys("admin")
        self.element_is_visible(clpro.FIRST_ROVE_VARIANT).click()
        self.element_is_visible(clpro.ACTION).click()
        self.element_is_visible(clpro.ACTION).click()
        self.element_is_visible(clpro.FIRST_ACTION_VARIANT).click()

    def edit_actions_string(self):  # 6 Редактировнаие действия над строками
        self.autorization()
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))
        self.element_is_visible(clpro.ACTIONS_STRING).click()
        self.element_is_visible(clpro.EDIT).click()
        html = self.element_is_visible(clpro.INPUT_ACTION)
        html.send_keys(Keys.CONTROL + "a")
        html.send_keys(Keys.DELETE)
        html.send_keys("alert('bye bye'); ")
        self.element_is_visible(clpro.SAVE).click()

    def delete_actions_string(self):  # 7 удаление действия над строками
        self.autorization()
        self.element_is_visible(clpro.DEVELOPMENT).click()
        self.driver.switch_to.frame(self.element_is_visible(clpro.IFRAME))
        self.element_is_visible(clpro.ACTIONS_STRING).click()
        self.element_is_visible(clpro.DELETE).click()
        self.element_is_visible(clpro.YES_DELETE).click()

    def table_reports(self):
        self.autorization()
        self.element_is_visible(dev.DEVELOPMENT).click()
        self.element_is_visible(dev.REPORTS).click()
        self.element_is_visible(dev.REPORTS_FIRST).click()
