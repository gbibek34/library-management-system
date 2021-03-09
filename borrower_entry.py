from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import Home
from Query import borrower


class borrowerEntry:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Borrower Entry')
        self.wn.geometry("1055x545+200+100")
        self.exe = borrower()
        # ==================================================Entry Data===================================================
        self.id_val = StringVar()
        self.fname_val = StringVar()
        self.lname_val = StringVar()
        self.contact_val = StringVar()
        self.email_val = StringVar()
        # ==================================================Frames=======================================================
        self.entry_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.entry_frame.place(x=10, y=10, width=430, height=530)
        self.table_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.table_frame.place(x=450, y=10, width=600, height=530)
        self.option_frame = Frame(self.entry_frame, relief=GROOVE, bd=5)
        self.option_frame.place(x=0, y=470, width=420, height=50)
        # ==================================================Labels=======================================================
        self.id_lbl = Label(
            self.entry_frame, text='Borrower ID :', font=('arial', 11))
        self.id_lbl.place(x=20, y=20)
        self.fname_lbl = Label(
            self.entry_frame, text='First Name :', font=('arial', 11))
        self.fname_lbl.place(x=20, y=70)
        self.lname_lbl = Label(
            self.entry_frame, text='Last Name :', font=('arial', 11))
        self.lname_lbl.place(x=20, y=120)
        self.contact_lbl = Label(
            self.entry_frame, text='Contact :', font=('arial', 11))
        self.contact_lbl.place(x=20, y=170)
        self.email_lbl = Label(
            self.entry_frame, text='E-mail :', font=('arial', 11))
        self.email_lbl.place(x=20, y=220)
        # ==================================================Entry========================================================
        self.id_ent = Entry(self.entry_frame, font=('arial', 12), width=22, textvariable=self.id_val,
                            state="readonly")
        self.id_ent.place(x=190, y=25)
        self.fname_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.fname_val)
        self.fname_ent.place(x=190, y=75)
        self.lname_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.lname_val)
        self.lname_ent.place(x=190, y=125)
        self.contact_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.contact_val)
        self.contact_ent.place(x=190, y=175)
        self.email_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.email_val)
        self.email_ent.place(x=190, y=225)
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
        self.borrower_tbl = ttk.Treeview(self.table_frame,
                                         columns=("id", "fname", "lname",
                                                  "contact", "email"),
                                         xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.borrower_tbl.yview, bg='#9BC01C')
        self.borrower_tbl.heading("id", text="ID")
        self.borrower_tbl.heading("fname", text="Firstname")
        self.borrower_tbl.heading("lname", text="Lastname")
        self.borrower_tbl.heading("contact", text="Contact")
        self.borrower_tbl.heading("email", text="Email")
        self.borrower_tbl['show'] = 'headings'
        self.borrower_tbl.column("id", width=5)
        self.borrower_tbl.column("fname", width=80)
        self.borrower_tbl.column("lname", width=80)
        self.borrower_tbl.column("contact", width=80)
        self.borrower_tbl.column("email", width=120)
        self.borrower_tbl.pack(fill=BOTH, expand='1')
        self.fetch()

    # ==========================================================methods=================================================
    def add(self):
        if self.fname_val.get() == '' or self.lname_val.get() == '' or self.contact_val.get() == '' or self.email_val.get() == '':
            tkinter.messagebox.showerror(
                'Error', 'Dont leave the fields empty.')
        else:
            self.exe.add_borrower(self.fname_val.get(),
                                  self.lname_val.get(), self.contact_val.get(), self.email_val.get())
            self.fetch()
            self.reset()

    def update(self):
        if self.id_val.get() == '' or self.fname_ent.get() == '' or self.lname_val.get() == '' or \
                self.contact_val.get() == '' or self.email_val.get() == '':
            tkinter.messagebox.showerror(
                'Error', 'Dont leave the fields empty.')
        else:
            self.exe.update_borrower(self.fname_ent.get(), self.lname_val.get(
            ), self.contact_val.get(), self.email_val.get(), self.id_val.get())
            self.fetch()
            return True

    def delete(self):
        self.exe.delete_borrower(self.id_val.get())
        self.reset()
        self.fetch()

    def reset(self):
        self.id_val.set('')
        self.fname_val.set('')
        self.lname_val.set('')
        self.contact_val.set('')
        self.email_val.set('')

    def fetch(self):
        data = self.exe.fetch_borrower()
        self.borrower_tbl.delete(*self.borrower_tbl.get_children())
        for i in data:
            self.borrower_tbl.insert("", "end", value=i)
        self.borrower_tbl.bind('<Double-1>', self.select)

    def select(self, event):
        '''Selects the data clicked in treeview'''
        self.row = self.borrower_tbl.item(
            self.borrower_tbl.selection(), "values")
        self.id = self.row[0]
        self.fill()

    def fill(self):
        '''Fills in the selected data from treeview'''
        self.reset()
        self.id_val.set(self.row[0])
        self.fname_val.set(self.row[1])
        self.lname_val.set(self.row[2])
        self.contact_val.set(self.row[3])
        self.email_val.set(self.row[4])

    def home(self):
        self.home = Toplevel(self.wn)
        Home.home(self.home)
        self.wn.withdraw()


# def main():
#     window = Tk()
#     borrowerEntry(window)
#     window.mainloop()


# if __name__ == '__main__':
#     main()
