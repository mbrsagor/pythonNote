import schedule
import time

def job():
    print("Running task...")

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

