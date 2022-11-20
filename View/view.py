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

class WindowManager(ScreenManager):
    pass

class TooltipButton(Button, MDTooltip):
    pass
# class WelcomeScreenView(Popup, Widget):
#     def __init__(self, system, **kwargs):
#         super().__init__(**kwargs)
#         self.system = system
#
#     def return_system(self):
#         return self.system
#
#
class MainScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        # self.table = MDDataTable(pos_hint={'center_y': 0.58, 'center_x': 0.5},
        #                          use_pagination=True,
        #                          check=True,
        #                          column_data=[
        #                              ("Имя питомца", dp(40)),
        #                              ("Вид животного", dp(30)),
        #                              ("Дата рождения", dp(30)),
        #                              ("Дата последнего приема", dp(30)),
        #                              ("ФИО ветеринара", dp(30)),
        #                              ("Диагноз", dp(30))], size_hint=(1, 0.7))
        # #                          # row_data=self.add_table_data())
        # # self.table.bind(on_row_press=self.pet_info_window)
        # # self.table.bind(on_check_press=self.check_info)
        #
        # self.add_widget(self.table)


class RegistrationScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ФИО
        self.fio = ''
        # пароль
        self.password = ''
        # логин
        self.login = ''

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


# class StringInput(TextInput):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def insert_text(self, string, from_undo=False):
#         alphabet = '+*/-=[]{}'
#         if string not in alphabet:
#             new_text = self.text + string
#             print(new_text)
#             if len(new_text) != 0:
#                 StringInput.insert_text(self, string, from_undo=from_undo)


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
        # self.table = MDDataTable(pos_hint={'center_y': 0.58, 'center_x': 0.6},
        #                          use_pagination=True,
        #                          check=True,
        #                          column_data=[
        #                              ("Имя питомца", dp(40)),
        #                              ("Вид животного", dp(30)),
        #                              ("Дата рождения", dp(30)),
        #                              ("Дата последнего приема", dp(30)),
        #                              ("ФИО ветеринара", dp(30)),
        #                              ("Диагноз", dp(30))], size_hint=(0.75, 0.7))
        #
        # self.add_widget(self.table)

    # сохранить()
    def save(self):
        pass


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

