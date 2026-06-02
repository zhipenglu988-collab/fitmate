from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from database import DBHelper
from services.bmi_service import calculate_bmi, bmi_category
import datetime


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 10

        # 欢迎与BMI摘要
        self.status_label = MDLabel(
            text="加载中...",
            font_style="H6",
            halign="center"
        )
        self.add_widget(self.status_label)

        self.bmi_label = MDLabel(
            text="",
            halign="center"
        )
        self.add_widget(self.bmi_label)

        # 快捷按钮
        btn_layout = MDBoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)
        btn1 = MDRaisedButton(text="体重记录", on_release=lambda x: self.set_screen("bmi"))
        btn2 = MDRaisedButton(text="饮食记录", on_release=lambda x: self.set_screen("diet"))
        btn3 = MDRaisedButton(text="训练计划", on_release=lambda x: self.set_screen("plan"))
        btn_layout.add_widget(btn1)
        btn_layout.add_widget(btn2)
        btn_layout.add_widget(btn3)
        self.add_widget(btn_layout)

        # 本周训练概览
        self.workout_summary = MDLabel(
            text="本周训练: 0 次",
            halign="center"
        )
        self.add_widget(self.workout_summary)

    def set_screen(self, name):
        if self.manager:
            self.manager.current = name

    def on_pre_enter(self, *args):
        self.refresh()

    def refresh(self):
        profile = DBHelper.get_profile()
        if profile:
            # profile: (id, name, gender, birth, height, weight, target, activity, goal)
            name = profile[1] or "用户"
            weight = profile[5] or 0
            height = profile[4] or 170
            target = profile[6] or 0
            self.status_label.text = f"Hi, {name}!"
            if weight > 0 and height > 0:
                bmi = calculate_bmi(weight, height)
                cat = bmi_category(bmi)
                target_str = f"| 目标: {target} kg" if target > 0 else ""
                self.bmi_label.text = f"当前 BMI: {bmi} ({cat}) {target_str}"
            else:
                self.bmi_label.text = "请先完善个人信息"
        else:
            self.status_label.text = "请先完善个人信息"
            self.bmi_label.text = ""

        # 本周训练次数
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        workouts = DBHelper.get_workout_log()
        week_count = 0
        for w in workouts:
            try:
                w_date = datetime.date.fromisoformat(w[0])
                if w_date >= monday:
                    week_count += 1
            except (ValueError, IndexError):
                pass
        self.workout_summary.text = f"本周训练: {week_count} 次"
