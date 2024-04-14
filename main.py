import datetime as dt
import tkinter as tk
from tkinter import messagebox, simpledialog
import time

def set_alarm():
    alarm_date = simpledialog.askstring("Set Alarm", "Enter date (dd-mm-yyyy):")
    alarm_time = simpledialog.askstring("Set Alarm", f"Enter time for {alarm_date} (hh:mm):")
    message = simpledialog.askstring("Set Alarm", "Enter message:")
    setting = f"{alarm_date} {alarm_time}"
    return setting, message


def alarm(alarm_time, message):
    alarm_time = dt.datetime.strptime(alarm_time, '%d-%m-%Y %H:%M')
    while dt.datetime.now() < alarm_time:
        time.sleep(1)
    response = tk.messagebox.askyesno(title='Alarm', message=f"{message}, Would you like to cancel the alarm? "
                                                      f"Press no to snooze", type="yesno")
    if not response:
        time_snooze = simpledialog.askfloat("Set snooze", "For how many minutes would you like to snooze?:")
        tk.messagebox.showinfo(message=f"Alarm has been snoozed for {time_snooze} minute")
        alarm_time += dt.timedelta(minutes=time_snooze)
        alarm(alarm_time.strftime('%d-%m-%Y %H:%M'), message)

alarm_time, message = set_alarm()
alarm(alarm_time, message)



