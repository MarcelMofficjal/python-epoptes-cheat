"""
This code blocks blocking your screen by pushing windows and changing piority
"""

# imports
from tkinter import END, Tk, Toplevel, Label, Button, Text, Entry 

# window
panel = Tk()
panel.title("Control Panel")
panel.geometry("500x500")
panel.maxsize(500, 500)
panel.minsize(500, 500)

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
        window.geometry("0x0+0+0")
        window.title("Grinder")
        window.attributes("-topmost", True)

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
output = Text(panel, width=60, height=18, bg="#000", fg="#fff") # 22 → 18
terminal_title = Label(panel, text="Terminal:")
terminal = Entry(panel, width=80, bg="#000", fg="#fff")
terminal.config(insertbackground="white")

def terminal_enter(event):
    event_value = terminal.get()

    args = event_value.split()

    if args[0] == "help":
        if len(args) == 1:
            output.insert(END, 
"""[CMD]   | TERMINAL: Command list:
        |           help    list of all commands
        |           help -> <command>     help of given command
        |           enable    enable grinder
        |           enable -> <interval>    enable grinder with given interval
        |           disable     disable grinder
        |           interval -> <value>   sets interval to given value
        |           incognito     enable incognito mode
""")
        else:
            if args[1] == "->":
            #elif event_value.startswith("help -> "):
                if event_value[8:] == "help":
                    output.insert(END, "[CMD]   | TERMINAL: help     list of all commands\n        |           help -> <command> help for given command\n")
                elif event_value[8:] == "enable":
                    output.insert(END, "[CMD]   | TERMINAL: enable     enable grinder\n        |           enable -> <interval> enable grinder with given interval\n")
                elif event_value[8:] == "disable":
                    output.insert(END, "[CMD]   | TERMINAL: disable     disable grinder\n")
                elif event_value[8:] == "interval":
                    output.insert(END, "[CMD]   | TERMINAL: interval -> <value>     sets interval to given value\n")
                elif event_value[8:] == "incognito":
                    output.insert(END, "[CMD]   | TERMINAL: incognito     enable incognito mode\n")
                else:
                    output.insert(END, f"[ERROR] | TERMINAL: Invalid command value >>> {event_value[8:]}\n")
            else:
                output.insert(END, f"[ERROR] | TERMINAL: Invalid parameter >>> {args[1]}")
    elif args[0] == "enable":
        if len(args) == 1:
            grinder_switch["text"] = "ENABLED"
            grinder_switch["bg"] = "#0f0"
            grinder.enable_grinder()
        else:
            if args[1] == "->":
                interval.delete(0, END)
                interval.insert(END, f"{event_value[10:]}")
                grinder_switch["text"] = "ENABLED"
                grinder_switch["bg"] = "#0f0"
                grinder.enable_grinder()  
            else:
                output.insert(END, f"[ERROR] | TERMINAL: Invalid parameter >>> {args[1]}")
    elif args[0] == "disable":
        if len(args) == 1:
            grinder_switch["text"] = "DISABLED"
            grinder_switch["bg"] = "#f00"
        else:
            output.insert(END, f"[ERROR] | TERMINAL: Invalid parameter >>> {args[1]}")
    elif args[0] == "interval":
        if len(args) == 1:
            output.insert(END, "[CMD]   | TERMINAL: interval -> <value>     sets interval to given value\n")
        else:
            if args[1] == "->":
                interval.delete(0, END)
                interval.insert(END, f"{event_value[12:]}")
                output.insert(END, "[CMD]   | TERMINAL: Succesfully changed interval value.\n")
            else:
                output.insert(END, f"[ERROR] | TERMINAL: Invalid parameter >>> {args[1]}")
    elif args[0] == "incognito":
        if len(args) == 1:
            panel.minsize(0, 0)
            panel.geometry("0x0+0+0")
            panel.wm_state('iconic')
            output.insert(END, "[CMD]   | TERMINAL: Succesfully changed mode to incognito.\n")
        else:
            output.insert(END, f"[ERROR] | TERMINAL: Invalid parameter >>> {args[1]}")
    else:
        output.insert(END, f"[ERROR] | TERMINAL: Cannot find command \"{event_value}\"\n")
    terminal.delete(0, END)
terminal.bind("<Return>", terminal_enter)

# ui showing
grinder_title.pack()
grinder_switch.pack()
label_interval.pack()
interval.pack()
interval.insert(END, "300")
output.pack(pady=20) 
terminal_title.pack()
terminal.pack()

# mainloop
panel.mainloop()
