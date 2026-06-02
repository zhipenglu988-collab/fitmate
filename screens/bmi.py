from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from services.bmi_service import calculate_bmi, bmi_category
from database import DBHelper
import datetime

class BMIScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        self.add_widget(MDLabel(text="体重与 BMI", font_style="H5", halign="center"))

        self.height_input = MDTextField(hint_text="身高 (cm)", text="170", input_filter="float")
        self.weight_input = MDTextField(hint_text="今日体重 (kg)", input_filter="float")
        self.fat_input = MDTextField(hint_text="体脂率 % (可选)", input_filter="float")
        for w in [self.height_input, self.weight_input, self.fat_input]:
            self.add_widget(w)

        self.add_widget(MDRaisedButton(text="计算并保存", on_release=self.calc_and_save))
        self.result_label = MDLabel(text="", halign="center")
        self.add_widget(self.result_label)

        # 历史记录简述
        self.history_label = MDLabel(text="", size_hint_y=None, height=200)
        self.add_widget(self.history_label)

    def calc_and_save(self, instance):
        try:
            h = float(self.height_input.text)
            w = float(self.weight_input.text)
            fat = float(self.fat_input.text or 0)
            bmi = calculate_bmi(w, h)
            cat = bmi_category(bmi)
            DBHelper.insert_weight(w, bmi, fat)
            self.result_label.text = f"BMI: {bmi} ({cat}) 已保存"
            self.update_history()
        except Exception as e:
            self.result_label.text = f"输入错误: {e}"

    def on_pre_enter(self, *args):
        profile = DBHelper.get_profile()
        if profile:
            self.height_input.text = str(profile[4])
        self.update_history()

    def update_history(self):
        rows = DBHelper.get_weight_history()
        text = "历史记录 (最近10条)\n" + "\n".join([f"{r[0]}: {r[1]}kg BMI{r[2]}" for r in rows[-10:]])
        self.history_label.text = text