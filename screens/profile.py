from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from database import DBHelper

class ProfileScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        self.add_widget(MDLabel(text="个人信息", font_style="H5", halign="center"))

        self.name_field = MDTextField(hint_text="姓名")
        self.gender_field = MDTextField(hint_text="性别 (男/女)")
        self.birth_field = MDTextField(hint_text="出生日期 (YYYY-MM-DD)")
        self.height_field = MDTextField(hint_text="身高 cm", input_filter="float")
        self.weight_field = MDTextField(hint_text="体重 kg", input_filter="float")
        self.target_field = MDTextField(hint_text="目标体重 kg", input_filter="float")
        self.activity_field = MDTextField(hint_text="活动水平 (sedentary/light/moderate/active/extreme)")
        self.goal_field = MDTextField(hint_text="目标 (lose_fat/build_muscle/maintain)")

        for field in [self.name_field, self.gender_field, self.birth_field,
                      self.height_field, self.weight_field, self.target_field,
                      self.activity_field, self.goal_field]:
            self.add_widget(field)

        self.add_widget(MDRaisedButton(text="保存", on_release=self.save_profile))
        self.status = MDLabel(text="", halign="center")
        self.add_widget(self.status)

    def on_pre_enter(self, *args):
        self.load()

    def load(self):
        profile = DBHelper.get_profile()
        if profile:
            self.name_field.text = str(profile[1] or "")
            self.gender_field.text = str(profile[2] or "")
            self.birth_field.text = str(profile[3] or "")
            self.height_field.text = str(profile[4] or "")
            self.weight_field.text = str(profile[5] or "")
            self.target_field.text = str(profile[6] or "")
            self.activity_field.text = str(profile[7] or "")
            self.goal_field.text = str(profile[8] or "")

    def save_profile(self, instance):
        try:
            data = {
                "name": self.name_field.text,
                "gender": self.gender_field.text,
                "birth_date": self.birth_field.text,
                "height_cm": float(self.height_field.text or 0),
                "weight_kg": float(self.weight_field.text or 0),
                "target_weight_kg": float(self.target_field.text or 0),
                "activity_level": self.activity_field.text,
                "goal": self.goal_field.text
            }
            DBHelper.update_profile(data)
            self.status.text = "保存成功"
        except Exception as e:
            self.status.text = f"错误: {e}"