from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel


class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        self.add_widget(MDLabel(text="提醒设置", font_style="H5", halign="center"))

        self.add_widget(MDLabel(text="晨练提醒", halign="left", theme_text_color="Secondary"))
        self.morning_hour = MDTextField(hint_text="时 (0-23)", text="8", input_filter="int")
        self.morning_min = MDTextField(hint_text="分 (0-59)", text="0", input_filter="int")
        self.add_widget(self.morning_hour)
        self.add_widget(self.morning_min)

        self.add_widget(MDLabel(text="晚间提醒", halign="left", theme_text_color="Secondary"))
        self.evening_hour = MDTextField(hint_text="时 (0-23)", text="19", input_filter="int")
        self.evening_min = MDTextField(hint_text="分 (0-59)", text="0", input_filter="int")
        self.add_widget(self.evening_hour)
        self.add_widget(self.evening_min)

        self.add_widget(MDRaisedButton(text="保存并应用", on_release=self.apply))
        self.status = MDLabel(text="", halign="center")
        self.add_widget(self.status)

    def apply(self, instance):
        try:
            from services.notification import scheduler

            h1 = max(0, min(23, int(self.morning_hour.text or "8")))
            m1 = max(0, min(59, int(self.morning_min.text or "0")))
            h2 = max(0, min(23, int(self.evening_hour.text or "19")))
            m2 = max(0, min(59, int(self.evening_min.text or "0")))

            try:
                scheduler.reschedule_job('morning_workout', trigger='cron', hour=h1, minute=m1)
            except Exception:
                from services.notification import send_notification
                from apscheduler.triggers.cron import CronTrigger
                scheduler.add_job(
                    lambda: send_notification("🏋️ 晨练时间", "新的一天，完成今天的训练目标吧！"),
                    CronTrigger(hour=h1, minute=m1),
                    id='morning_workout',
                    replace_existing=True
                )

            try:
                scheduler.reschedule_job('evening_reminder', trigger='cron', hour=h2, minute=m2)
            except Exception:
                from services.notification import send_notification
                from apscheduler.triggers.cron import CronTrigger
                scheduler.add_job(
                    lambda: send_notification("🥗 饮食记录", "别忘了记录你的晚餐哦~"),
                    CronTrigger(hour=h2, minute=m2),
                    id='evening_reminder',
                    replace_existing=True
                )

            self.status.text = f"✅ 提醒已更新: {h1:02d}:{m1:02d} / {h2:02d}:{m2:02d}"
            Snackbar(text="提醒设置已保存").open()

        except Exception as e:
            self.status.text = f"❌ 错误: {e}"
