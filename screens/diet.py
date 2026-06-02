from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from database import DBHelper
import datetime

class DietScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 10

        self.add_widget(MDLabel(text="饮食记录", font_style="H5", halign="center"))

        self.meal_type = "早餐"
        self.meal_button = MDRaisedButton(text="餐类: 早餐", on_release=self.open_menu)
        self.add_widget(self.meal_button)

        self.food_input = MDTextField(hint_text="食物名称")
        self.cal_input = MDTextField(hint_text="卡路里 (kcal)", input_filter="float")
        self.protein_input = MDTextField(hint_text="蛋白质 g (可选)", input_filter="float")
        for w in [self.food_input, self.cal_input, self.protein_input]:
            self.add_widget(w)

        self.add_widget(MDRaisedButton(text="添加", on_release=self.add_food))

        self.history_label = MDLabel(text="今日饮食", valign="top")
        self.add_widget(self.history_label)

        self.menu_items = [
            {"text": "早餐", "viewclass": "OneLineListItem", "on_release": lambda x="早餐": self.set_meal(x)},
            {"text": "午餐", "viewclass": "OneLineListItem", "on_release": lambda x="午餐": self.set_meal(x)},
            {"text": "晚餐", "viewclass": "OneLineListItem", "on_release": lambda x="晚餐": self.set_meal(x)},
            {"text": "加餐", "viewclass": "OneLineListItem", "on_release": lambda x="加餐": self.set_meal(x)},
        ]
        self.menu = MDDropdownMenu(
            caller=self.meal_button,
            items=self.menu_items,
            width_mult=3,
        )

    def set_meal(self, meal):
        self.meal_type = meal
        self.meal_button.text = f"餐类: {meal}"
        self.menu.dismiss()

    def open_menu(self, instance):
        self.menu.open()

    def add_food(self, instance):
        try:
            food = self.food_input.text
            cal = float(self.cal_input.text or 0)
            protein = float(self.protein_input.text or 0)
            DBHelper.insert_diet(self.meal_type, food, cal, protein)
            self.food_input.text = ""
            self.cal_input.text = ""
            self.protein_input.text = ""
            self.load_today()
        except Exception as e:
            self.history_label.text = f"错误: {e}"

    def on_pre_enter(self, *args):
        self.load_today()

    def load_today(self):
        today = datetime.date.today().isoformat()
        entries = DBHelper.get_diet_log(today)
        text = f"今日 ({today}) 饮食:\n"
        total_cal = 0
        for meal, food, cal in entries:
            text += f"  {meal}: {food} ({cal} kcal)\n"
            total_cal += cal
        text += f"总摄入: {total_cal} kcal"
        self.history_label.text = text