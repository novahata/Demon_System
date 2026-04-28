from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from home import HomeScreen

Window.softinput_mode = "below_target"

KV = '''
MDScreenManager:

    # Прелоадер
    MDScreen:
        name: "preloader"
        md_bg_color: app.theme_cls.primary_color

        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"

            Widget:

            MDLabel:
                text: "Demon System"
                halign: "center"
                font_style: "H4"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                text: "Loading..."
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0.9, 0.9, 0.9, 1

            Widget:

            MDRaisedButton:
                md_bg_color: get_color_from_hex("#FF9800")
                text: "Start"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.6
                on_release: app.go_home()
'''

class MainApp(MDApp):

    def build(self):
        # ЄДИНЕ місце, де задається стиль
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"

        self.sm = Builder.load_string(KV)

        # додаємо home екран
        self.sm.add_widget(HomeScreen(name="home"))

        return self.sm

    def go_home(self):
        self.sm.current = "home"


if __name__ == '__main__':
    MainApp().run()