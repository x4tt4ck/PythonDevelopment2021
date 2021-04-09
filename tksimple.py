#!/usr/bin/env python3

'''
TkInter example
Launches a window with "Quit" button.
'''

import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.timeButton = tk.Button(self, text="Time", command=self.settime)
        self.timeLabel = tk.Label(self, text="<time appears here>")
        self.quitButton.grid()
        self.timeButton.grid()
        self.timeLabel.grid()

    def settime(self):
        self.timeLabel["text"] = time.strftime("%c")

app = Application()
app.master.title('Sample application')
app.mainloop()
