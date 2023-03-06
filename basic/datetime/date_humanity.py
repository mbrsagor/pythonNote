def format_timedelta(td):
    hours, remainder = divmod(td.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    if hours < 10:
        hours = '0%s' % int(hours)
    if minutes < 10:
        minutes = '0%s' % minutes
    if seconds < 10:
        seconds = '0%s' % seconds
    return '%s:%s:%s' % (hours, minutes, seconds)


millis = input("Enter time in milliseconds: ")
millis = int(millis)
seconds = (millis / 1000) % 60
seconds = int(seconds)
minutes = (millis / (1000 * 60)) % 60
minutes = int(minutes)
hours = (millis / (1000 * 60 * 60)) % 24

print("%d:%d:%d" % (hours, minutes, seconds))
