from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from kivymd.uix.screen import MDScreen

from mod.pop_ai import PopAIScreen
from mod.pop_gem import PopGemScreen


KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<HomeScreen>:
    name: "home"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: get_color_from_hex("#0D4037")

        MDTopAppBar:
            title: "Demon"
            elevation: 4
            md_bg_color: app.theme_cls.primary_color

        MDLabel:
            text: "Головний екран"
            halign: "center"

    # 🤖 AI кнопка
    MDFloatingActionButton:
        icon: "robot"
        md_bg_color: get_color_from_hex("#FF9800")
        pos_hint: {"center_x": .9, "center_y": .1}
        on_release: root.open_ai()

    # 💎 GEM кнопка
    MDFloatingActionButton:
        icon: "star-four-points"
        md_bg_color: get_color_from_hex("#03A9F4")
        pos_hint: {"center_x": .9, "center_y": .2}
        on_release: root.open_gem()
'''

Builder.load_string(KV)


class HomeScreen(MDScreen):

    def on_enter(self):
        # додаємо екрани тільки один раз
        if not self.manager.has_screen("ai"):
            self.manager.add_widget(PopAIScreen(name="ai"))

        if not self.manager.has_screen("gem"):
            self.manager.add_widget(PopGemScreen(name="gem"))

    def open_ai(self):
        self.manager.current = "ai"

    def open_gem(self):
        self.manager.current = "gem"