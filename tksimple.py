#!/usr/bin/env python3

'''
TkInter example
Launches a window with "Quit" button.
'''

import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.timeButton = tk.Button(self, text="Time", command=self.settime)
        self.timeLabel = tk.Label(self)
        self.quitButton.grid()
        self.timeButton.grid(row=0, column=1)
        self.timeLabel.grid(columnspan=2)
        self.settime()

    def settime(self):
        self.timeLabel["text"] = time.strftime("%c")

app = Application()
app.master.title('Sample application')
app.mainloop()
