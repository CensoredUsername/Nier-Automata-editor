#!/usr/bin/python3

import tkinter as tk
import tkinter.ttk
import chips

class ChipsManagerUI(tk.Frame):

    def __init__(self, save_data, on_close=None):

        self._save_data = bytearray(save_data)
        self._chips_manager = chips.ChipsRecordManager(self._save_data)
        self.updated_chips = {}

        root = tk.Toplevel()
        root.geometry('320x400')
        root.title("NieR;Automata Chips Editor")

        super().__init__(root)
        self.pack(side="top", fill="both", expand=True)
        self.create_widgets()

        if callable(on_close):
            self.bind("<Destroy>", lambda _: on_close(self._save_data))


    def create_widgets(self):
        right_frame = tk.Frame(self, background="#eeeeee", width=20)
        tk.Label(right_frame, text="Equipped chips are not editable, un-equip them first", width=10, wraplength=70).grid(row=0, column=0)
        tk.Button(right_frame, text="Save",width=8, height=3, command=self.on_save_clicked).grid(row=1, column=0)
        tk.Button(right_frame, text="Close", width=8, height=3, command=self.on_close_clicked).grid(row=2, column=0)
        canvas = tk.Canvas(self, borderwidth=0, background="#ccffff", width=30)
        frame = tk.Frame(canvas, background="#ffffff")
        vsb = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        right_frame.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4, 4), window=frame, anchor="nw", tags="self.frame")
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        self.populate(frame)

    def populate(self, parent):
        available_chips = ("(Empty)",) + chips.ChipsRecord.AVAILABLE_CHIPS
        available_sizes = [i for i in range(31)]
        for row in range(300):
            chip_name = tk.StringVar()
            chip_size = tk.StringVar()
            tk.Label(parent, text=str(row), width=3, borderwidth="1", relief="solid").grid(row=row, column=0)
            chip_cb = tk.ttk.Combobox(parent, values=available_chips, state="readonly", textvariable=chip_name)
            chip_cb.grid(row=row, column=1)
            size_cb = tk.ttk.Combobox(parent, values=available_sizes, state="readonly", width=5, textvariable=chip_size)
            size_cb.grid(row=row, column=2)
            current = self._chips_manager.get_chip_at(row)
            if current != chips.ChipsRecord.EMPTY_RECORD:
                chip_cb.current(available_chips.index(current.name))
                size_cb.current(current.size)

                if current.offset_a != -1 or current.offset_b != -1 or current.offset_c != -1:
                    chip_cb['state'] = "disabled"
                    size_cb['state'] = "disabled"
            else:
                chip_cb.current(0)
                size_cb.current(0)
            data = (row, chip_name, chip_size)
            chip_cb.bind("<<ComboboxSelected>>", lambda e, args=data: self.on_chip_cb_selected(e, args))
            size_cb.bind("<<ComboboxSelected>>", lambda e, args=data: self.on_size_cb_selected(e, args))

    def on_chip_cb_selected(self, event, args):
        # print("index:{0} name:{1} size:{2}".format(args[0], args[1].get(), args[2].get()))
        if args[1].get() != "(Empty)":
            record = chips.ChipsRecord.from_name(args[1].get())
            args[2].set(str(record.size))
        else:
            record = chips.ChipsRecord.EMPTY_RECORD
            args[2].set("0")
        self.updated_chips[args[0]] = record

    def on_size_cb_selected(self, event, args):
        if args[0] in self.updated_chips.keys():
            self.updated_chips[args[0]].size = int(args[2].get())
        else:
            record = chips.ChipsRecord.from_name(args[1].get())
            record.size = int(args[2].get())
            self.updated_chips[args[0]] = record

    def on_save_clicked(self):
        for index, record in self.updated_chips.items():
            self._chips_manager.set_chip_at(index, record)
        self._save_data[chips.ChipsRecordManager.SAVE_DATA_CHIPS_OFFSET: chips.ChipsRecordManager.SAVE_DATA_CHIPS_OFFSET_END] = self._chips_manager.blocks
        self.master.destroy()

    def on_close_clicked(self):
        self.master.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    def open_ui():
        with open("./SlotData_0.dat", "rb") as f:
            data = f.read()
        ChipsManagerUI(data, lambda out: print(len(out)))

    tk.Button(root, text="Open", command=open_ui).pack(fill="both")

    root.mainloop()
