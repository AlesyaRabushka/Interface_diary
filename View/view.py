
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
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
        #                          # row_data=self.add_table_data())
        # self.table.bind(on_row_press=self.pet_info_window)
        # self.table.bind(on_check_press=self.check_info)

        # self.add_widget(self.table)


class RegistrationScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.system = system

    def return_system(self):
        return self.system
#
class AuthentificationScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.system = system

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
        # self.system = system


class EditAccountScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.system = system

class RecordsScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


class ProgressScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class NotificationsScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class AddRecordScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class RemoveRecordScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class RemoveAccountScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class EditRecordScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


class ExitScreenView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



