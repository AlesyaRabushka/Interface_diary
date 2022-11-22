from kivymd.uix.screen import MDScreen
#from Model.system import User, Registration, Validate
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput
from kivymd.uix.tooltip import MDTooltip
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(transition = NoTransition(),**kwargs)

class TooltipButton(Button, MDTooltip):
    pass

class MainScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RegistrationScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # string ФИО
        self.fio = ''
        # string пароль
        self.password = ''
        # string логин
        self.login = ''

        # адрес почты пользователя
        self.email = ''

        # новыйПользователь
        # self.registration = Registration()

    def set_full_name(self, full_name):
        self.fio = full_name
    def set_login(self, login):
        self.login = login
    def set_password(self, password):
        self.password = password
    def set_email(self, email):
        self.email = email

    # для безопасности ввода пароля
    def hide_password(self):
        if self.ids.password.password == True:
            self.ids.password.password = False
        elif self.ids.password.password == False:
            self.ids.password.password = True

    # сохранить(ФИО)
    def save(self, fio):
        pass
    # регистрация()
    def registration(self):
        pass


#
class AuthentificationScreenView(MDScreen):
    """
    ОкноВход
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # пароль
        self.password = ''
        # логин
        self.login = ''

    def set_login(self, login):
        self.login = login
    def set_password(self, password):
        self.password = password


    def hide_password(self):
        if self.ids.password.password == True:
            self.ids.password.password = False
        elif self.ids.password.password == False:
            self.ids.password.password = True




class ForgetPasswordScreenView(MDScreen, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.system = system

    def set_login(self, login):
        pass
    def set_email(self, email):
        pass

class AccountScreenView(MDScreen, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ФИО
        self.fio = ''
        # фотография
        self.photo_path = ''
        # почта
        self.email =''

        # проверкаПользователя
        # self.validation = Validate()
        # модель
        # self.model = User()


class EditAccountScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.system = system
    def set_name(self, name):
        pass

class RecordsScreenView(MDScreen):
    """
    ОкноЗадачи
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # запись
        #self.record = ??????

    # сохранить()
    def save(self):
        pass

    def add_record(self):
        Factory.AddRecordScreenView().open()



class SettingsScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ProgressScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class NotificationsScreenView(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


class AddRecordScreenView(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_time(self, time):
        pass
    def set_record_name(self, name):
        pass
    def set_record_description(self, description):
        pass


class RemoveRecordScreenView(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    def remove_record(self):
        pass

class RemoveAccountScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class EditRecordScreenView(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    def set_name(self, name):
        pass
    def set_time(self, time):
        pass
    def set_description(self, description):
        pass


class ExitScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ErrorScreenView(Popup, Widget):
    """
    Ошибка
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # НаименованиеОшибки
        self.error_name = ''


class RecordMenuScreenView(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

