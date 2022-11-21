from Files.view import *

class System:
    """
    Система
    """
    def __init__(self):
        pass

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
    def add_new_record(self):
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
        self.login_list = Validate()

    # bool проверка(string логин, string пароль)
    def validate(self, login:str, password:str)-> bool:
        pass