from View.view import *

class System:
    """
    Система
    """
    def __init__(self):
        pass

    #
    def authorization(self):
        pass
    #
    def open_menu(self):
        pass
    #
    def add_new_user(self, name : str):
        pass
    #
    def add_new_record(self):
        pass
    #
    def remove_record(self):
        pass
    #
    def edit_record(self, date: str, time:str,name:str):
        pass
    #
    def update_record(self):
        pass


class User:
    """
    Пользователь
    """
    def __init__(self):
        # имя
        self.name = ''
        # фотография
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


class Registration:
    """
    Регистрация
    """
    def __init__(self):
        # ФИО
        self.fio = ''
        # пароль
        self.password = ''
        # логин
        self.login = ''
        # фотография
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
        self.login_list = Validate()

    # проверка(string логин, string пароль)
    def validate(self, login:str, password:str)-> bool:
        pass