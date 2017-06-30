# NieR;Automata save game editor by CensoredUsername (https://github.com/CensoredUsername)
# Note: I am not responsible for you fucking your save game up with this.

import tkinter as tk
from tkinter import messagebox, filedialog
import struct
import os
from os import path
import shutil
import binascii
import chips_UI

class SaveGame:
    def __init__(self, path):
        self.path = path
        with open(path, "rb") as f:
            self.original = f.read()

        # these bytes are always the first 12 bytes of GameData.dat
        self.gamedata_header = self.original[0x4:0x10]

        self.time_played,        = struct.unpack_from("<L", self.original, 0x00024)
        self.last_saved_chapter, = struct.unpack_from("<L", self.original, 0x0002C)

        # name is stored in a zero-padded utf-16 (or maybe UCS-2) buffer at the start of the file
        self.name = self.original[0x34:0x7A].decode("utf-16-le").rstrip("\0")

        # most interesting things to edit
        self.money,              = struct.unpack_from("<L", self.original, 0x3056C)
        self.experience,         = struct.unpack_from("<L", self.original, 0x3871C)

    def save(self):
        new = bytearray(self.original)

        new[0x4:0x10] = self.gamedata_header

        struct.pack_into("<L", new, 0x00024, self.time_played)
        struct.pack_into("<L", new, 0x0002C, self.last_saved_chapter)

        namebuf = self.name.encode("utf-16-le")
        # limit length
        if len(namebuf) > 68:
            namebuf = namebuf[:68]
        # pad with zeroes
        namebuf = namebuf + b"\0" * (70 - len(namebuf))
        new[0x34:0x7A] = namebuf

        struct.pack_into("<L", new, 0x3056C, self.money)
        struct.pack_into("<L", new, 0x3871C, self.experience)

        # back up the file
        shutil.move(self.path, self.path + ".bak")

        # write the new one
        with open(self.path, "wb") as f:
            f.write(new)

FILL = tk.N+tk.S+tk.E+tk.W
def curry(f, *args):
    def curried():
        f(*args)
    return curried


class Interface(tk.Frame):
    def __init__(self, saves, gamedata_header, master=None):
        self.saves = saves
        self.gamedata_header = gamedata_header

        tk.Frame.__init__(self, master)
        self.grid(sticky=FILL)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        gamedata = tk.Frame(self, borderwidth=10)
        gamedata.grid(sticky=FILL)
        tk.Label(gamedata, text="GameData.dat header: ").grid(row=0, column=0, sticky=tk.E)
        tk.Label(gamedata, text=binascii.hexlify(self.gamedata_header)).grid(row=0, column=1)

        for i, (name, data) in enumerate(self.saves.items()):
            self.rowconfigure(i + 1, weight=1)

            saveframe = tk.Frame(self, borderwidth=10)
            saveframe.grid(sticky=FILL)
            # header
            def command(save_button, data):
                data.save()
                save_button.config(state=tk.DISABLED)

            tk.Label(saveframe, text="Save slot {}:".format(i)).grid(row=0, column=0, sticky=tk.E)
            tk.Label(saveframe, text=name).grid(row=0, column=1, sticky=tk.W)
            save_button = tk.Button(saveframe, text="Save", state=tk.DISABLED)
            save_button.config(command=curry(command, save_button, data))
            save_button.grid(row=0, column=2, sticky=FILL)

            # gamedata header
            def command(self, save_button, header_var, data):
                data.gamedata_header = self.gamedata_header
                header_var.set(binascii.hexlify(data.gamedata_header))
                save_button.config(state=tk.NORMAL)

            tk.Label(saveframe, text="GameData.dat header: ").grid(row=1, column=0, sticky=tk.E)
            header_var = tk.StringVar()
            header_var.set(binascii.hexlify(data.gamedata_header))
            tk.Label(saveframe, textvariable=header_var).grid(row=1, column=1, sticky=tk.W)
            tk.Button(saveframe, text="Import", command=curry(command, self, save_button, header_var, data)).grid(row=1, column=2, sticky=FILL)

            # character name
            def command(save_button, name_var, data):
                data.name = name_var.get()
                save_button.config(state=tk.NORMAL)

            tk.Label(saveframe, text="Character name: ").grid(row=2, column=0, sticky=tk.E)
            name_var = tk.StringVar()
            name_var.set(data.name)
            tk.Entry(saveframe, textvariable=name_var).grid(row=2, column=1, sticky=FILL)
            tk.Button(saveframe, text="Set", command=curry(command, save_button, name_var, data)).grid(row=2, column=2, sticky=FILL)

            # xp
            def command(save_button, xp_var, data):
                try:
                    experience = int(xp_var.get())
                except ValueError:
                    messagebox.showerror("Error", "Please specify a number")
                    return

                if experience >= 2**32:
                    messagebox.showerror("Error", "Number too large")
                    return

                data.experience = experience
                save_button.config(state=tk.NORMAL)

            tk.Label(saveframe, text="Experience: ").grid(row=3, column=0, sticky=tk.E)
            xp_var = tk.StringVar()
            xp_var.set(str(data.experience))
            tk.Entry(saveframe, textvariable=xp_var).grid(row=3, column=1, sticky=FILL)
            tk.Button(saveframe, text="Set", command=curry(command, save_button, xp_var, data)).grid(row=3, column=2, sticky=FILL)

            # money
            def command(save_button, money_var, data):
                try:
                    money = int(money_var.get())
                except ValueError:
                    messagebox.showerror("Error", "Please specify a number")
                    return

                if money >= 2**32:
                    messagebox.showerror("Error", "Number too large")
                    return

                data.money = money
                save_button.config(state=tk.NORMAL)

            tk.Label(saveframe, text="Money: ").grid(row=4, column=0, sticky=tk.E)
            money_var = tk.StringVar()
            money_var.set(str(data.money))
            tk.Entry(saveframe, textvariable=money_var).grid(row=4, column=1, sticky=FILL)
            tk.Button(saveframe, text="Set", command=curry(command, save_button, money_var, data)).grid(row=4, column=2, sticky=FILL)

            # chips

            def on_inventory_clicked(save_button, original_data):
                def replace_data(new_data):
                    original_data.original = new_data
                chips_UI.ChipsManagerUI(original_data.original, replace_data)
                save_button.config(state=tk.NORMAL)
            tk.Button(saveframe, text="Edit Chips", command=curry(on_inventory_clicked, save_button, data)).grid(row=5, column=1, sticky=FILL)


def main():
    user_folder = os.getenv("USERPROFILE")
    nier_automata_folder = path.join(user_folder, "Documents", "My Games", "NieR_Automata")
    if not path.isdir(nier_automata_folder):
        messagebox.showerror("Error", "Could not find Nier;Automata's save folder location. Please select the save folder location")
        nier_automata_folder = filedialog.askdirectory()

    gamedata_path = path.join(nier_automata_folder, "GameData.dat")
    if not path.isfile(gamedata_path):
        raise Exception("Could not find NieR_Automata/GameData.dat. Please run Nier;Automata at least once before using this tool.")

    # read the gamedata header.
    with open(gamedata_path, "rb") as f:
        gamedata_header = f.read(12)

    locations = ("SlotData_0.dat", "SlotData_1.dat", "SlotData_2.dat")
    import collections
    saves = collections.OrderedDict()

    for location in locations:
        savedata_path = path.join(nier_automata_folder, location)
        if path.isfile(savedata_path):
            saves[location] = SaveGame(savedata_path)

    interface = Interface(saves, gamedata_header)
    interface.master.title("NieR;Automata Save Editor")
    interface.mainloop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        messagebox.showerror("Whoops", "\n".join(e.args))
