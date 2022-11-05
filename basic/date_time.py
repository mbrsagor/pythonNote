def time_conversion(sec):
    sec_value = sec % (24 * 3600)
    hours = sec_value // 3600
    sec_value %= 3600
    minutes = sec_value // 60
    sec_value %= 60
    print("Converted sec value in hour:", hours)
    print("Converted sec value in minutes:", minutes)


time_conversion(1667663255)
