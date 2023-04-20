from datetime import datetime, timedelta


def time_conversion(sec):
    sec_value = sec % (24 * 3600)
    hours = sec_value // 3600
    sec_value %= 3600
    minutes = sec_value // 60
    sec_value %= 60
    print("Converted sec value in hour:", hours)
    print("Converted sec value in minutes:", minutes)


time_conversion(1667663255)

print()


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


c = convert(1667663255)
print(c)

sec = int(input("Enter time in Seconds: "))

time = []
days, sec = divmod(sec, 86400)  # sec will get seconds in partial day
if days:
    time.append(f"{days} day" + "s" * (days > 1))

hours, sec = divmod(sec, 3600)  # sec will get seconds in partial hour
if hours:
    time.append(f"{hours} hour" + "s" * (hours > 1))

minutes, sec = divmod(sec, 60)  # sec will get seconds in partial minute
if minutes:
    time.append(f"{minutes} minute" + "s" * (minutes > 1))

if sec:
    time.append(f"{sec} second" + "s" * (sec > 1))
print(time)

last_hour_date_time = datetime.now() - timedelta(hours=1)
print(last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S'))
