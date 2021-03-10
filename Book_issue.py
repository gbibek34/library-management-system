from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from Query import issue
import Home


class bookIssue:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Product Entry')
        self.wn.geometry("1055x545+200+100")
        self.exe = issue()
        # ==================================================Entry Data===================================================
        self.iid_val = StringVar()
        self.bid_val = StringVar()
        self.brname_val = StringVar()
        self.contact_val = StringVar()
        # ==================================================Frames=======================================================
        self.entry_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.entry_frame.place(x=10, y=10, width=430, height=530)
        self.table_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.table_frame.place(x=450, y=40, width=600, height=500)
        self.option_frame = Frame(self.entry_frame, relief=GROOVE, bd=5)
        self.option_frame.place(x=0, y=470, width=420, height=50)
        self.search_ent = Entry(self.wn, font=(
            'arial', 12), width=49,)
        self.search_ent.place(x=450, y=10)
        self.search_btn = Button(
            self.wn, text='Search', command=self.fetch_data)
        self.search_btn.place(x=920, y=8)
        self.searchall_btn = Button(
            self.wn, text='Search all', command=self.fetch)
        self.searchall_btn.place(x=980, y=8)
        # ==================================================Labels=======================================================
        self.iid_lbl = Label(
            self.entry_frame, text='Issue ID :', font=('arial', 11))
        self.iid_lbl.place(x=20, y=20)
        self.bid_lbl = Label(
            self.entry_frame, text='Book ID :', font=('arial', 11))
        self.bid_lbl.place(x=20, y=70)
        self.bname_lbl = Label(
            self.entry_frame, text='Book Name :', font=('arial', 11))
        self.bname_lbl.place(x=20, y=120)
        self.brname_lbl = Label(
            self.entry_frame, text='Borrower Name :', font=('arial', 11))
        self.brname_lbl.place(x=20, y=170)
        self.contact_lbl = Label(
            self.entry_frame, text='Contact :', font=('arial', 11))
        self.contact_lbl.place(x=20, y=220)
        # ==================================================Entry========================================================
        self.iid_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.iid_val, state='readonly')
        self.iid_ent.place(x=190, y=25)
        self.bid_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.bid_val, state='readonly')
        self.bid_ent.place(x=190, y=75)
        self.bname_ent = ttk.Combobox(
            self.entry_frame, font=('arial', 12), width=20, state='readonly')
        self.bname_ent['values'] = ()
        self.bname_ent.place(x=190, y=125)
        self.brname_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.brname_val)
        self.brname_ent.place(x=190, y=175)
        self.contact_ent = Entry(self.entry_frame, font=(
            'arial', 12), width=22, textvariable=self.contact_val)
        self.contact_ent.place(x=190, y=225)
        self.bname_fetch()
        # ==================================================Buttons======================================================
        self.issue_btn = Button(self.entry_frame, text='ISSUE',
                                height=2, width=12, command=self.issuebook)
        self.issue_btn.place(x=80, y=320)
        self.return_btn = Button(
            self.entry_frame, text='RETURN', height=2, width=12, command=self.returnbook)
        self.return_btn.place(x=210, y=320)
        self.back_btn = Button(
            self.option_frame, text='BACK', height=2, width=58, command=self.home)
        self.back_btn.pack(side=LEFT)
        # ==================================================Tree View====================================================
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.issue_tbl = ttk.Treeview(self.table_frame,
                                      columns=("id", "bname", "brname",
                                               "contact"),
                                      xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.issue_tbl.yview, bg='#9BC01C')
        self.issue_tbl.heading("id", text="Issue ID")
        self.issue_tbl.heading("bname", text="Book Name")
        self.issue_tbl.heading("brname", text="Borrower Name")
        self.issue_tbl.heading("contact", text="Contact")
        self.issue_tbl['show'] = 'headings'
        self.issue_tbl.column("id", width=5)
        self.issue_tbl.column("bname", width=80)
        self.issue_tbl.column("brname", width=100)
        self.issue_tbl.column("contact", width=20)
        self.issue_tbl.pack(fill=BOTH, expand='1')
        self.fetch()
    # ==================================================Methods==========================================================

    def issuebook(self):
        if self.bname_ent.get() == '' or self.brname_val.get() == '' or self.contact_val.get() == '':
            tkinter.messagebox.showerror(
                'Error', 'Dont leave the fields empty.')
        else:
            self.exe.add_issue(self.bid_val.get(), self.bname_ent.get(),
                               self.brname_val.get(), self.contact_val.get())
            self.exe.update_book_issue(self.bid_val.get())
            tkinter.messagebox.showinfo('Success', 'Issue Made')
            self.bname_fetch()
            self.fetch()
            self.reset()

    def returnbook(self):
        if self.iid_val.get() == '' or self.bid_val.get() == '' or self.bname_ent.get() == '' or \
                self.brname_val.get() == '' or self.contact_val.get() == '':
            tkinter.messagebox.showerror(
                'Error', 'Dont leave the fields empty.')
        else:
            self.exe.return_issue(self.iid_val.get())
            self.exe.update_book_return(self.bid_val.get())
            self.bname_fetch()
            self.fetch()
            self.reset()
            return True

    def reset(self):
        '''Clears the data in the entry and combo boxes'''
        self.iid_val.set('')
        self.bid_val.set('')
        self.bname_ent.set('')
        self.brname_val.set('')
        self.contact_val.set('')

    def bname_fetch(self):
        data = []
        for i in self.exe.fetch_book():
            data.append(i[0])
        self.bname_ent['values'] = data
        self.bname_ent.bind("<<ComboboxSelected>>", self.bookid_fetch)

    def bookid_fetch(self, event):
        data = self.exe.fetch_book_id(self.bname_ent.get())
        self.bid_val.set(data[0][0])

    def fetch_data(self):
        data = self.exe.search_data(self.search_ent.get())
        print(data)
        if len(data) != 0:
            self.issue_tbl.delete(*self.issue_tbl.get_children())
            for i in data:
                self.issue_tbl.insert(
                    "", "end", value=(i[0], i[2], i[3], i[4]))

    def fetch(self):
        '''Takes in the data from database and inserts in treeview'''
        data = self.exe.fetch_issue()
        self.issue_tbl.delete(*self.issue_tbl.get_children())
        for i in data:
            self.issue_tbl.insert("", "end", value=(
                i[0], i[2], i[3], i[4], i[1]))
        self.issue_tbl.bind('<Double-1>', self.select)

    def select(self, event):
        '''Selects the data clicked in treeview'''
        self.row = self.issue_tbl.item(
            self.issue_tbl.selection(), "values")
        self.id = self.row[0]
        self.fill()

    def fill(self):
        '''Fills in the selected data from treeview'''
        self.reset()
        self.iid_val.set(self.row[0])
        self.bid_val.set(self.row[4])
        self.bname_ent.set(self.row[1])
        self.brname_val.set(self.row[2])
        self.contact_val.set(self.row[3])

    def home(self):
        self.home = Toplevel(self.wn)
        Home.home(self.home)
        self.wn.withdraw()


def main():
    '''Sets the class to work in tkinter'''
    window = Tk()
    bookIssue(window)
    window.mainloop()


if __name__ == '__main__':
    main()
