from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import Home


class bookEntry:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Book Entry')
        self.wn.geometry("1055x545+200+100")
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
                              height=2, width=12)
        self.add_btn.place(x=30, y=280)
        self.update_btn = Button(
            self.entry_frame, text='UPDATE', height=2, width=12)
        self.update_btn.place(x=160, y=280)
        self.delete_btn = Button(
            self.entry_frame, text='DELETE', height=2, width=12)
        self.delete_btn.place(x=290, y=280)
        self.reset_btn = Button(
            self.entry_frame, text='RESET', height=2, width=24)
        self.reset_btn.place(x=120, y=340)
        self.logout_btn = Button(
            self.option_frame, text='LOGOUT', height=2, width=28)
        self.logout_btn.pack(side=LEFT)
        self.back_btn = Button(
            self.option_frame, text='BACK', height=2, width=28)
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
        # self.fetch()


def main():
    window = Tk()
    bookEntry(window)
    window.mainloop()


if __name__ == '__main__':
    main()
