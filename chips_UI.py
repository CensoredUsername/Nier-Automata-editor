#!/usr/bin/python3

import tkinter as tk

class ChipsManagerUI(tk.Frame):
    def __init__(self, savefilelocation, master=None):
        with open(savefilelocation,"rb") as f:
            self.save_data = f.read()
        super().__init__(master)
        self.createWidgets()

    def createWidgets(self):
        pass

