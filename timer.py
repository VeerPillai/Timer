import tkinter as tk
import datetime
import math
#datetime.datetime.now() ----It will show you device time
#datetime.timedelta(seconds) --- The time we have given
#after == almost like sleep in multithreading
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.done_time=datetime.datetime.now() + datetime.timedelta(seconds=1200) # half hour
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clk()
        self.root.mainloop()

    def update_clk(self):
        elapsed = self.done_time - datetime.datetime.now()
        h,m,s = elapsed.seconds/3600,elapsed.seconds/60,elapsed.seconds%60
        fractional = math.floor(elapsed.microseconds/1000000.0*100)
        self.label.configure(text="%02d:%02d:%02d.%02d"%(h,m,s,fractional),fg='red')
        self.root.after(10, self.update_clk)
app=App()
