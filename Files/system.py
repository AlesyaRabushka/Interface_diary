import datetime
from kivy.properties import ObjectProperty
from Files.view import *

class Application:
    def __init__(self):
        self.system = System()

        user = User()
        self.system.set_user(user)
        self.system.add_new_user(user.name)

        record = Records()
        self.system.set_current_record(record)
        self.system.add_new_record(record.name, record.date, record.time, record.id)

        validation = Validate()





class System:
    """
    Система
    """
    def __init__(self):
        self.registration = Registration()

    def set_user(self, user):
        self.user = user
    def set_current_record(self, record):
        self.current_record = record



    # авторизация()
    def authorization(self):
        pass
    # открыть_меню()
    def open_menu(self):
        pass
    # добавитьНовогоПользователя(string Имя)
    def add_new_user(self, name : str):
        pass
    # добасвитьНовуюЗапись()
    def add_new_record(self, name: str, date: datetime, time : str, id : str):
        pass
    # удалитьЗапись()
    def remove_record(self):
        pass
    #редактироватьЗапись(string дата, string время, string название)
    def edit_record(self, date: str, time:str,name:str):
        pass
    # обновитьЗапись()
    def update_record(self):
        pass
    # Выход()
    def exit(self):
        pass


class Records:
    """
    Задачи
    """
    def __init__(self):
        # string название
        self.name = ''
        # date дата
        self.date = datetime.date.today()
        # string время
        self.time = ''
        # string идентификатор
        self.id = ''

    # сохранить()
    def save(self):
        pass
    # показать()
    def show(self):
        pass


class User:
    """
    Пользователь
    """
    def __init__(self):
        # string имя
        self.name = ''
        # string фотография
        self.photo_path = ''

    # ДобавитьЗапись(Запись запись)
    def add_record(self, record):
        pass
    # УдалитьЗапись(Запись запись)
    def remove_record(self, record):
        pass
    # РедактироватьЗапись(Запись запись)
    def edit_record(self, record):
        pass
    # ПросмотретьЗапись(Запись запись)
    def read_record(self, record):
        pass
    # Выйти()
    def exit(self):
        pass


class Registration:
    """
    Регистрация
    """
    def __init__(self):
        # string ФИО
        self.fio = ''
        # string пароль
        self.password = ''
        # string логин
        self.login = ''
        # string фотография
        self.photo_path = ''

    # регистрация()
    def registration(self):
        pass


class Validate:
    """
    Проверка
    """
    def __init__(self):
        # списокЛогинов
        self.login_list = []


    # bool проверка(string логин, string пароль)
    def validate(self, login:str, password:str)-> bool:
        pass