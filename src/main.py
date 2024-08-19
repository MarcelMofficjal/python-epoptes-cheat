"""
This code blocks blocking your screen by pushing windows and changing piority
"""

# imports
from tkinter import END, Tk, Toplevel, Label, Button, Text, Entry 

# window
panel = Tk()
panel.title("Control Panel")
panel.geometry("500x500")

# main class (all funcs)
class Grinder:
    # changes interval input and grinder output foreground colors to normal
    def interval_to_normal(self):
        interval["fg"] = "#000"
        output["fg"] = "#fff"

    # switches button (enabled, disabled)
    def switch(self):
        if grinder_switch["text"] == "ENABLED":
            grinder_switch["text"] = "DISABLED"
            grinder_switch["bg"] = "#f00"
        elif grinder_switch["text"] == "DISABLED":
            grinder_switch["text"] = "ENABLED"
            grinder_switch["bg"] = "#0f0"
            self.enable_grinder()

    # kills grinder and if it's not disabled - runs it again
    def kill(self, window):
        window.forget(window)
        if grinder_switch["text"] == "DISABLED":
            output.insert(END, "[INFO]  | SW GRINDER: Grinder succesfully disabled.\n")
        else:
            self.grind()

    # main grinder function
    def grind(self):
        window = Toplevel(panel)
        window.geometry("0x0")
        window.title("Grinder")

        if interval.get() == "0":
            window.forget(window)
            output.insert(END, "[ERROR] | SW GRINDER: Disabled Grinder for security reasons!\n")
            output.insert(END, "        | SW GRINDER: Interval cannot be set for 0!\n")
            grinder_switch["text"] = "DISABLED"
            grinder_switch["bg"] = "#f00"       
            output.insert(END, "[INFO]  | SW GRINDER: Grinder succesfully disabled.\n")
            interval["fg"] = "#f00"
            output["fg"] = "#f00"
            interval.after(3000, self.interval_to_normal)
        else:
            try:
                window.after(int(interval.get()), lambda: self.kill(window=window))
            except:
                window.forget(window)
                output.insert(END, "[ERROR] | SW GRINDER: Interval value must be INT!\n")
                grinder_switch["text"] = "DISABLED"
                grinder_switch["bg"] = "#f00"
                output.insert(END, "[INFO]  | SW GRINDER: Grinder succesfully disabled.\n")
                interval["fg"] = "#f00"
                output["fg"] = "#f00"
                interval.after(3000, self.interval_to_normal)

    # enables grinder
    def enable_grinder(self):
        output.insert(END, "[INFO]  | SW GRINDER: Grinder succesfully enabled.\n")
        self.grind()

# instance
grinder = Grinder()

# ui
grinder_title = Label(panel, text="Windows Grinder", fg="#f00", font=("Arial", 13))
grinder_switch = Button(panel, text="DISABLED", bg="#f00", command=grinder.switch)
label_interval = Label(panel, text="Interval:")
interval = Entry(panel, width=10)
output = Text(panel, width=60, height=22, bg="#000", fg="#fff")

# ui showing
grinder_title.pack()
grinder_switch.pack()
label_interval.pack()
interval.pack()
interval.insert(END, "300")
output.pack(pady=20) 

# mainloop
panel.mainloop()
