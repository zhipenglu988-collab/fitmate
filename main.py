"""FitMate - 移动健身助手
Python + KivyMD 打造，全本地 SQLite 存储，无需服务端
"""

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from database import init_db
from services.notification import start_scheduler


class FitMateApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"

        self.sm = MDScreenManager()

        # 7 个功能页面
        from screens.home import HomeScreen
        from screens.profile import ProfileScreen
        from screens.bmi import BMIScreen
        from screens.plan import PlanScreen
        from screens.diet import DietScreen
        from screens.settings import SettingsScreen
        from screens.achievements import AchievementsScreen

        screens = [
            HomeScreen(name="home"),
            ProfileScreen(name="profile"),
            BMIScreen(name="bmi"),
            PlanScreen(name="plan"),
            DietScreen(name="diet"),
            SettingsScreen(name="settings"),
            AchievementsScreen(name="achievements"),
        ]
        for s in screens:
            self.sm.add_widget(s)

        return self.sm

    def on_start(self):
        init_db()
        from database import DBHelper
        DBHelper.init_achievements()
        start_scheduler()


if __name__ == "__main__":
    FitMateApp().run()
