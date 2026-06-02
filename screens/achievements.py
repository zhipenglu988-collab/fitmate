from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from database import DBHelper

class AchievementsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10
        self.add_widget(MDLabel(text="成就徽章", font_style="H5", halign="center"))
        self.badges_layout = MDBoxLayout(orientation="vertical", spacing=8, adaptive_height=True)
        self.add_widget(self.badges_layout)

    def on_pre_enter(self, *args):
        self.badges_layout.clear_widgets()
        badges = DBHelper.get_achievements()
        for name, unlocked, date in badges:
            card = MDCard(
                orientation="vertical",
                size_hint_y=None,
                height=80,
                padding=10,
                elevation=2
            )
            status = "✅" if unlocked else "🔒"
            date_str = date if unlocked else ""
            card.add_widget(MDLabel(text=f"{status} {name}  {date_str}"))
            self.badges_layout.add_widget(card)