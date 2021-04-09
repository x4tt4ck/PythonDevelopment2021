#!/usr/bin/env python3

'''
15 Puzzle game
'''

import tkinter as tk
from random import shuffle

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):

        # Making the root window resizeable
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for i in range(1, 4):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)

        # Control buttons
        self.exitButton = tk.Button(self, text="Exit", command=self.quit)
        self.refreshButton = tk.Button(self, text="New", command=self.refresh)

        # Game buttons
        self.gameButtons = []
        for i in range(1, 16):
            self.gameButtons.append(
                tk.Button(self, text=str(i), command=self.action)
            )

        # Control buttons placement
        self.exitButton.grid(row=0, column=0, columnspan=2, sticky="WE")
        self.refreshButton.grid(row=0, column=2, columnspan=2, sticky="WE")

        # Game buttons placement
        shuffle(self.gameButtons)
        for i in range(15):
            self.gameButtons[i].grid(row=1+i//4, column=i%4, sticky="NEWS")

    def refresh(self):
        shuffle(self.gameButtons)
        for i in range(15):
            self.gameButtons[i].grid(row=1+i//4, column=i%4)

    def action(self):
        pass

app = Application()
app.master.title('Игра в 15')
app.mainloop()
