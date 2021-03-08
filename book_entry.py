from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import Home
from Query import book


class bookEntry:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Book Entry')
        self.wn.geometry("1055x545+200+100")
        self.exe = book()
        # ==================================================Entry Data===================================================
        self.bid_val = StringVar()
        self.bname_val = StringVar()
        self.bgenre_val = StringVar()
        self.bauthor_val = StringVar()
        # ==================================================Frames=======================================================
        self.entry_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.entry_frame.place(x=10, y=10, width=430, height=530)
        self.table_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.table_frame.place(x=450, y=10, width=600, height=530)
        self.option_frame = Frame(self.entry_frame, relief=GROOVE, bd=5)
        self.option_frame.place(x=0, y=470, width=420, height=50)
        # ==================================================Labels=======================================================
        self.bid_lbl = Label(
            self.entry_frame, text='Book ID :', font=('arial', 11))
        self.bid_lbl.place(x=20, y=20)
        self.bname_lbl = Label(
            self.entry_frame, text='Book Name :', font=('arial', 11))
        self.bname_lbl.place(x=20, y=70)
        self.bgenre_lbl = Label(
            self.entry_frame, text='Genre :', font=('arial', 11))
        self.bgenre_lbl.place(x=20, y=120)
        self.bauthor_lbl = Label(
            self.entry_frame, text='Author :', font=('arial', 11))
        self.bauthor_lbl.place(x=20, y=170)
        # ==================================================Entry========================================================
        self.bid_ent = Entry(self.entry_frame, font=('arial', 12), width=22, textvariable=self.bid_val,
                             state="readonly")
        self.bid_ent.place(x=190, y=25)
        self.bname_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.bname_val)
        self.bname_ent.place(x=190, y=75)
        self.bgenre_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.bgenre_val)
        self.bgenre_ent.place(x=190, y=125)
        self.bauthor_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.bauthor_val)
        self.bauthor_ent.place(x=190, y=175)
        # ==================================================Buttons======================================================
        self.add_btn = Button(self.entry_frame, text='ADD',
                              height=2, width=12, command=self.add)
        self.add_btn.place(x=30, y=280)
        self.update_btn = Button(
            self.entry_frame, text='UPDATE', height=2, width=12, command=self.update)
        self.update_btn.place(x=160, y=280)
        self.delete_btn = Button(
            self.entry_frame, text='DELETE', height=2, width=12, command=self.delete)
        self.delete_btn.place(x=290, y=280)
        self.reset_btn = Button(
            self.entry_frame, text='RESET', height=2, width=24, command=self.reset)
        self.reset_btn.place(x=120, y=340)
        self.back_btn = Button(
            self.option_frame, text='BACK', height=2, width=58, command=self.home)
        self.back_btn.pack(side=LEFT)
        # ==================================================Tree View====================================================
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.book_tbl = ttk.Treeview(self.table_frame,
                                     columns=("bid", "bname", "bgenre",
                                              "bauthor", "availability"),
                                     xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.book_tbl.yview, bg='#9BC01C')
        self.book_tbl.heading("bid", text="ID")
        self.book_tbl.heading("bname", text="Book Name")
        self.book_tbl.heading("bgenre", text="Genre")
        self.book_tbl.heading("bauthor", text="Author")
        self.book_tbl.heading("availability", text="Availability")
        self.book_tbl['show'] = 'headings'
        self.book_tbl.column("bid", width=5)
        self.book_tbl.column("bname", width=150)
        self.book_tbl.column("bgenre", width=40)
        self.book_tbl.column("bauthor", width=80)
        self.book_tbl.column("availability", width=10)
        self.book_tbl.pack(fill=BOTH, expand='1')
        self.fetch()

    # ==========================================================Methods=================================================
    def add(self):
        if self.bname_val.get() == '' or self.bgenre_val.get() == '' or self.bauthor_val.get() == '':
            tkinter.messagebox.showerror(
                'Error', 'Dont leave the fields empty.')
        else:
            self.exe.add_book(self.bname_val.get(),
                              self.bgenre_val.get(), self.bauthor_val.get())
            self.fetch()
            self.reset()

    def update(self):
        if self.bid_val.get() == '' or self.bname_ent.get() == '' or self.bgenre_val.get() == '' or \
                self.bauthor_val.get() == '':
            tkinter.messagebox.showerror(
                'Error', 'Dont leave the fields empty.')
        else:
            self.exe.update_book(self.bname_ent.get(), self.bgenre_val.get(
            ), self.bauthor_val.get(), self.bid_val.get())
            self.fetch()
            return True

    def delete(self):
        '''Deletes an added product'''
        self.exe.delete_book(self.bid_val.get())
        self.reset()
        self.fetch()

    def reset(self):
        '''Clears the data in the entry and combo boxes'''
        self.bid_val.set('')
        self.bname_val.set('')
        self.bgenre_val.set('')
        self.bauthor_val.set('')

    def fetch(self):
        '''Takes in the data from database and inserts in treeview'''
        data = self.exe.fetch_book()
        self.book_tbl.delete(*self.book_tbl.get_children())
        for i in data:
            self.book_tbl.insert("", "end", value=i)
        self.book_tbl.bind('<Double-1>', self.select)

    def select(self, event):
        '''Selects the data clicked in treeview'''
        self.row = self.book_tbl.item(
            self.book_tbl.selection(), "values")
        self.id = self.row[0]
        self.fill()

    def fill(self):
        '''Fills in the selected data from treeview'''
        self.reset()
        self.bid_val.set(self.row[0])
        self.bname_val.set(self.row[1])
        self.bgenre_val.set(self.row[2])
        self.bauthor_val.set(self.row[3])

    def home(self):
        self.home = Toplevel(self.wn)
        Home.home(self.login)
        self.wn.withdraw()


def main():
    window = Tk()
    bookEntry(window)
    window.mainloop()


if __name__ == '__main__':
    main()
