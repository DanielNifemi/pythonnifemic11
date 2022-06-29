from datetime import datetime


def clock(time):
    return time.strftime("%H:%M:%S")


print(clock(datetime.now()))