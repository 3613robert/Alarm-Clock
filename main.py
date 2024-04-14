import datetime as dt
import tkinter as tk
from tkinter import messagebox, simpledialog
import time

def valid_input_time(alarm_date, alarm_hours):
    valid_input = ['012345678914-:']
    for _ in alarm_date:
        if _ not in valid_input:
            return False
    for _ in alarm_hours:
        if _ not in valid_input:
            return False
    return True

def set_alarm():
    while True:
        alarm_date = simpledialog.askstring("Set Alarm", "Enter date (dd-mm-yyyy):")
        alarm_time = simpledialog.askstring("Set Alarm", f"Enter time for {alarm_date} (hh:mm):")
        try:
            if valid_input_time(alarm_date, alarm_hours=alarm_time):
                message = simpledialog.askstring("Set Alarm", "Enter message:")
                setting = f"{alarm_date} {alarm_time}"
                return setting, message
            else:
                tk.messagebox.showinfo(message="Please enter a valid date and time")
        except TypeError:
            tk.messagebox.showinfo(message="Please enter a valid date and time")


def alarm(alarm_time, message):
    try:
        alarm_time = dt.datetime.strptime(alarm_time, '%d-%m-%Y %H:%M')
    except (ValueError, TypeError):
        tk.messagebox.showinfo(message='Please enter a valid date and time.')
        alarm_time, message = set_alarm()
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