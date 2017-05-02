#!/usr/bin/python3

import tkinter as tk
import os,os.path

class ChipsManagerUI(tk.Frame):
    def __init__(self, savefilelocation, master=None):
        with open(savefilelocation,"rb") as f:
            self.save_data = f.read()
        super().__init__(master)
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()

    def populate(self):
        pass

    
    
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__=="__main__":
    user_folder = os.getenv("USERPROFILE")
    nier_automata_folder = os.path.join(user_folder, "Documents", "My Games", "NieR_Automata")
    if not os.path.isdir(nier_automata_folder):
        raise Exception("Could not find NieR;Automata's save folder location")

    gamedata_path = os.path.join(nier_automata_folder, "GameData.dat")
    if not os.path.isfile(gamedata_path):
        raise Exception("Could not find NieR_Automata/GameData.dat. Please run Nier;Automata at least once before using this tool.")

    # read the gamedata header.
    with open(gamedata_path, "rb") as f:
        gamedata_header = f.read(12)

    locations = ("SlotData_0.dat", "SlotData_1.dat", "SlotData_2.dat")
    import collections
    saves = collections.OrderedDict()


    interface = ChipsManagerUI(os.path.join(nier_automata_folder, locations[2]))
    interface.master.title("NieR;Automata Save Editor")
    interface.mainloop()