from datetime import datetime
from tkinter import Label

#
# def clock(time):
#     return time.strftime("%H:%M:%S")
#
#
# print(clock(datetime.now()))


from Assignments.PersonalProject.digitalClock1 import root, time

lbl = Label(root, font=('Segoe Script', 0, 'bold'),
            background='black',
            foreground='green')


# Placing clock at the centre
# of the tkinter window
def date(time):
    return time.strftime("%d/%m/%Y")


lbl.pack(anchor='center')

print(date(datetime.now()))

time()
