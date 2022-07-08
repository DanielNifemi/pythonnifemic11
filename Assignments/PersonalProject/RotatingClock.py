from datetime import datetime


def rotatingclock(hour, minute):
    hour = hour % 12
    minute = minute % 60
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6
    return hour_angle, minute_angle


print(rotatingclock(datetime.now().hour, datetime.now().minute))
