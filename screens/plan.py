from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from database import DBHelper
from services.plan_generator import generate_plan

class PlanScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        top_bar = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=50, spacing=10)
        top_bar.add_widget(MDRaisedButton(text="重新生成计划", on_release=self.regenerate))
        top_bar.add_widget(MDRaisedButton(text="标记完成训练", on_release=self.mark_done))
        self.add_widget(top_bar)

        self.plan_label = MDLabel(text="尚无计划", valign="top")
        scroll = ScrollView()
        scroll.add_widget(self.plan_label)
        self.add_widget(scroll)

    def on_pre_enter(self, *args):
        self.load_plan()

    def load_plan(self):
        plan = DBHelper.get_plan()
        if plan:
            days_map = {0: "周一", 1: "周二", 2: "周三", 3: "周四", 4: "周五", 5: "周六", 6: "周日"}
            text = ""
            current_day = None
            for day, name, sets, reps, duration, rest in plan:
                if day != current_day:
                    current_day = day
                    text += f"\n【{days_map.get(day, '')}】\n"
                if sets == 1 and duration > 0:
                    text += f"  {name} : {duration} 分钟\n"
                else:
                    text += f"  {name} : {sets} 组 x {reps} 次\n"
            self.plan_label.text = text.strip() or "尚无计划"
        else:
            self.plan_label.text = "请先生成计划"

    def regenerate(self, instance):
        profile = DBHelper.get_profile()
        if profile:
            goal = profile[8]
            activity = profile[7]
            plan_data = generate_plan(goal, activity)
            DBHelper.clear_plan()
            for day, exercises in plan_data:
                for name, sets, reps, rest in exercises:
                    DBHelper.insert_plan(day, name, sets, reps, reps if sets==1 else 0, rest)
            self.load_plan()
            self.plan_label.text += "\n计划已更新"

    def mark_done(self, instance):
        # 记录一次完成训练
        DBHelper.insert_workout("跑步", 30, 200, 1)
        from kivymd.uix.snackbar import Snackbar
        Snackbar(text="✅ 已记录一次训练！").open()