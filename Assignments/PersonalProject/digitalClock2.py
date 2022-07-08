from tkinter import Label

from Assignments.PersonalProject.digitalClock1 import root


def digitalclock():
    import time
    import datetime
    while True:
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"))
        time.sleep(1)
        digitalclock()
        lbl = Label(root, font=('Segoe Script', 12, 'bold'),
                    background='black',
                    foreground='yellow')

        # Placing clock at the centre
        # of the tkinter window
        lbl.pack(anchor='center')
        time()