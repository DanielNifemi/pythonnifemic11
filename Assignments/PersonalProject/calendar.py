# create a function that print out a whole calendar
# the function should take a year and a month as arguments
# if the year and month are not given, the current year and month should be used
import datetime

import calendar


def print_calendar(year=None, month=None):
    if year is None:
        year = calendar.now().year
    if month is None:
        month = datetime.now().month
    print(calendar.month(year, month))
    return calendar.month(year, month)


print(print_calendar())