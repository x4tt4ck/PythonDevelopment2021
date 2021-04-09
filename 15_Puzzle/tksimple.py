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
            B = tk.Button(self, text=str(i))
            B["command"] = lambda g=B.grid_info: self.action(g)
            self.gameButtons.append(B)
        self.emptyspace = {'row': 4, 'col': 3}

        # Control buttons placement
        self.exitButton.grid(row=0, column=0, columnspan=2, sticky="WE")
        self.refreshButton.grid(row=0, column=2, columnspan=2, sticky="WE")

        # Game buttons placement
        shuffle(self.gameButtons)
        self.gameButtons.append("Empty")
        for i in range(16):
            if self.gameButtons[i] != "Empty":
                self.gameButtons[i].grid(row=1+i//4, column=i%4, sticky="NEWS")

    def refresh(self):
        self.emptyspace = {'row': 4, 'col': 3}
        self.gameButtons.remove("Empty")
        shuffle(self.gameButtons)
        for i in range(15):
            self.gameButtons[i].grid(row=1+i//4, column=i%4)
        self.gameButtons.append("Empty")

    def check(self):
        win = True
        prev = -1
        for button in self.gameButtons:
            if button != "Empty":
                print(button["text"], prev)
                if int(button["text"]) < prev:
                    print("Not yet!")
                    win = False
                    break
                prev = int(button["text"])

        if win == True:
            self.win()
            print("Refreshing...")
            self.refresh()

    def win(self):
        print("Win!")
        W = tk.Tk()
        W.title("Поздравляем!")
        L = tk.Label(W, text="Вы победили!")
        L.grid()
        B = tk.Button(W, text="Еще разок!", command=W.destroy)
        B.grid()

    def action(self, g):

        col = g()['column']
        row = g()['row']
        ecol = self.emptyspace['col']
        erow = self.emptyspace['row']
        eind = (erow-1)*4 + ecol
        ind = (row-1)*4 + col

        print(f"Button pressed! Empty:{eind}({erow},{ecol}), Button:{ind}({row},{col})")

        if col == ecol and abs(row - erow) == 1:
            self.gameButtons[ind].grid(row=erow)
            self.emptyspace['row'] = row
            self.gameButtons[ind], self.gameButtons[eind] = self.gameButtons[eind], self.gameButtons[ind]
            self.check()

        elif row == erow and abs(col - ecol) == 1:
            self.gameButtons[ind].grid(column=ecol)
            self.emptyspace['col'] = col
            self.gameButtons[ind], self.gameButtons[eind] = self.gameButtons[eind], self.gameButtons[ind]
            self.check()

app = Application()
app.master.title('Игра в 15')
app.mainloop()
