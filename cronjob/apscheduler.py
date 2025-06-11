from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

def my_task():
    print("Task executed")

scheduler = BackgroundScheduler()
scheduler.add_job(my_task, CronTrigger(hour=3, minute=0))
scheduler.start()


