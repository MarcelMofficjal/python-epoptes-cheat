# imports
from tkinter import *
import time

# Control Panel
panel = Tk()
panel.title("Control Panel")
panel.geometry("500x500")

# Funcs
def switch():
    if grinder_switch["text"] == "ENABLED":
        grinder_switch["text"] = "DISABLED"
        grinder_switch["bg"] = "#f00"
    elif grinder_switch["text"] == "DISABLED":
        grinder_switch["text"] = "ENABLED"
        grinder_switch["bg"] = "#0f0"
        enable_grinder()

def kill(window):
    window.forget(window)
    if grinder_switch["text"] == "DISABLED":
        output.insert(END, "[INFO]  | SW GRINDER: Grinder succesfully disabled.\n")
    else:
        grind()

def grind():
    window = Toplevel(panel)
    window.geometry("0x0")
    window.title("Grinder")
    try:
        window.after(int(interval.get()), lambda: kill(window=window))
    except:
        output.insert(END, "[ERROR] | SW GRINDER: Interval value must be INT!\n")
        grinder_switch["text"] = "DISABLED"
        grinder_switch["bg"] = "#f00"
        output.insert(END, "[INFO]  | SW GRINDER: Grinder succesfully disabled.\n")

def enable_grinder():
    output.insert(END, "[INFO]  | SW GRINDER: Grinder succesfully enabled.\n")
    grind()

grinder_title = Label(panel, text="Windows Grinder", fg="#f00", font=("Arial", 13))
grinder_switch = Button(panel, text="DISABLED", bg="#f00", command=switch)
label_interval = Label(panel, text="Interval:")
interval = Entry(panel, width=10)
output = Text(panel, width=60, height=22, bg="#000", fg="#fff")

grinder_title.pack()
grinder_switch.pack()
label_interval.pack()
interval.pack()
interval.insert(END, "300")
output.pack(pady=20) 

panel.mainloop()
