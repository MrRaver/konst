# konst

Для запуска тестироваия нужно иметь установленное ПО:
1) PyCharm https://www.jetbrains.com/pycharm/download/#section=windows
2) Python https://www.python.org/

После установки, нужно отрыть данный проект в Pycharm.
Уставновить необходимые библиотеки (selenium,pytest, webdriver-manager из  Python Packages). 
Дальше нужно добавть Virtualenv Environment, для работы с selenium.
Нужно перейти File>Settings>Add Interpreter>Add local Interpreter>Virtualenv Environment>ok

![image](https://user-images.githubusercontent.com/114143145/235587502-cbf78159-46f9-45ea-8eb5-a57d5b9a8a3a.png)

![image](https://user-images.githubusercontent.com/114143145/235593283-1c5bbb07-1ddd-421d-99de-c7b59a8cc31e.png)

![image](https://user-images.githubusercontent.com/114143145/235593459-1397cfcd-5e9b-4200-bad0-df20a564bb0b.png)


После файл venv появиться среди файлов проекта.
Проект состоит из трех папок и файла conftest.py

![image](https://user-images.githubusercontent.com/114143145/235593578-0a1e09de-a771-439a-b44d-434400dca7f7.png)


Файл создает функцию driver, в ней происходит инициализация и установка webdriver.
yield возвращает генератор, не занимая место в памяти а создавается по ходу выполнения.
pytest.fixture вызывает функцию только один раз за тестовый сценарий, quit заверщает сессию.

В папке locators хранятся локаторы (путь к элементу в интерфейсе, с помощью которого автоматизированный тест (автотест) сможет его найти)
В папке pages хранятся страницы веб сайта в виде классов и их тестовые сценарии в виде функций.
В папке tests вызываются тестовые сценарии из pages. Для запуска тестового сценария надо перейти в папку tests, выбрать раздел. Затем среди списка тестов выбрать нужный и запустить.
Для запуска нужно нажать на зеленый треугольник перед функцией.
![image](https://user-images.githubusercontent.com/114143145/235600353-1f0ccfb8-aeef-4dc8-a199-286447278167.png)

Дальше начнется тестирование. Не нажимайте никуда по открытому браузера чтобы не сломать тест, дождитесь его окончания. Программа отобразит результат выполнения.

Успешное выполнение тестирования выглядит так ![image](https://user-images.githubusercontent.com/114143145/235600066-d5e63927-b410-4ae0-af81-0a7797d85cdd.png)

Вывод ошибки при тестирование выглядит так ![image](https://user-images.githubusercontent.com/114143145/235601040-e7f2af0c-c76e-4e78-9db5-ed4970edf2f9.png)

