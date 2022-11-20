from kivymd.uix.screen import MDScreen
#from Model.system import User, Registration, Validate
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.popup import Popup
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

        # новыйПользователь
        # self.registration = Registration()

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


    def return_system(self):
        return self.system

#
class ForgetPasswordScreenView(MDScreen, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.system = system

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


class RemoveRecordScreenView(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class RemoveAccountScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class EditRecordScreenView(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

