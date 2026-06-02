from plyer import notification
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

scheduler = BackgroundScheduler()

def send_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="FitMate",
            timeout=5
        )
    except Exception as e:
        print("通知失败:", e)

def start_scheduler():
    # 默认早晨8:00和晚上19:00
    scheduler.add_job(
        lambda: send_notification("🏋️ 晨练时间", "新的一天，完成今天的训练目标吧！"),
        'cron', hour=8, minute=0, id='morning_workout'
    )
    scheduler.add_job(
        lambda: send_notification("🥗 饮食记录", "别忘了记录你的晚餐哦~"),
        'cron', hour=19, minute=0, id='evening_reminder'
    )
    scheduler.start()