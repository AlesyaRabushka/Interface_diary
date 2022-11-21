from kivymd.app import MDApp
import os
from kivy.lang import Builder
from Files.system import System


class DiaryApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system = System()

    def build(self):
        return Builder.load_file(os.path.join(os.path.dirname(__file__), "Files/view.kv"))

if __name__ == '__main__':
    DiaryApp().run()
