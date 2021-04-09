#!/usr/bin/env python3

'''
15 Puzzle game
'''

import tkinter as tk
from random import shuffle

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.timeButton = tk.Button(self, text="Time", command=self.settime)
        self.timeLabel = tk.Label(self)
        self.quitButton.grid()
        self.timeButton.grid(row=0, column=1)
        self.timeLabel.grid(columnspan=2)
        self.settime()
        '''
        self.exitButton = tk.Button(self, text="Exit", command=self.quit)
        self.refreshButton = tk.Button(self, text="New", command=self.refresh)
        self.gameButtons = []
        for i in range(1, 16):
            self.gameButtons.append(
                tk.Button(self, text=str(i), command=self.action)
            )
        self.exitButton.grid(row=0, column=0)
        self.refreshButton.grid(row=0, column=1)
        shuffle(self.gameButtons)
        for i in range(15):
            self.gameButtons[i].grid(row=1+i//4, column=i%4)

    def refresh(self):
        shuffle(self.gameButtons)
        for i in range(15):
            self.gameButtons[i].grid(row=1+i//4, column=i%4)

    def action(self):
        pass

app = Application()
app.master.title('Игра в 15')
app.mainloop()
