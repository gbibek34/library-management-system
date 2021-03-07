from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import login
from query import librarian


class registerPage:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Register")
        self.wn.geometry("500x500+500+100")
        self.exe = librarian()
        # =======================================================Text Variables==========================================
        self.firstname_val = StringVar()
        self.lastname_val = StringVar()
        self.email_val = StringVar()
        self.username_val = StringVar()
        self.password_val = StringVar()
        self.contact_val = StringVar()
        # =======================================================Labels==================================================
        self.firstname_lbl = Label(self.wn, text='Firstname :',
                                   font=('arial', 11)).place(x=80, y=140)
        self.lastname_lbl = Label(self.wn, text='Lastname :',
                                  font=('arial', 11)).place(x=80, y=180)
        self.email_lbl = Label(self.wn, text='E-mail :',
                               font=('arial', 11)).place(x=80, y=220)
        self.username_lbl = Label(self.wn, text='Username :',
                                  font=('arial', 11)).place(x=80, y=260)
        self.password_lbl = Label(self.wn, text='Password :',
                                  font=('arial', 11)).place(x=80, y=300)
        self.contact_lbl = Label(self.wn, text='Contact :',
                                 font=('arial', 11)).place(x=80, y=340)
        # =======================================================Entries=================================================
        self.firstname_ent = Entry(self.wn, text='Firstname :',
                                   font=('arial', 11), width=22, textvariable=self.firstname_val)
        self.firstname_ent.place(x=180, y=140)
        self.lastname_ent = Entry(self.wn, text='Lastname :',
                                  font=('arial', 11), width=22, textvariable=self.lastname_val)
        self.lastname_ent.place(x=180, y=180)
        self.email_ent = Entry(self.wn, text='E-mail :',
                               font=('arial', 11), width=22, textvariable=self.email_val)
        self.email_ent.place(x=180, y=220)
        self.username_ent = Entry(self.wn, text='Username:',
                                  font=('arial', 11), width=22, textvariable=self.username_val)
        self.username_ent.place(x=180, y=260)
        self.password_ent = Entry(self.wn, text='Password :',
                                  font=('arial', 11), width=22, show='*', textvariable=self.password_val)
        self.password_ent.place(x=180, y=300)
        self.contact_ent = Entry(self.wn, text='Contact :',
                                 font=('arial', 11), width=22, textvariable=self.contact_val)
        self.contact_ent.place(x=180, y=340)
        # =======================================================Buttons=================================================
        self.reg_btn = Button(self.wn, text='Sign Up',
                              height=2, width=12, command=self.addlibrarian)
        self.reg_btn.place(x=120, y=380)
        self.reset_btn = Button(self.wn, text='Reset',
                                height=2, width=12, command=self.reset)
        self.reset_btn.place(x=250, y=380)
        self.login_btn = Button(self.wn, text='Login',
                                height=2, width=12, command=self.login)
        self.login_btn.place(x=180, y=450)

    def addlibrarian(self):
        '''Takes in the credentials to add a user after checking existing username'''
        data = self.exe.fetch_username()
        username = self.username_ent.get()
        result = self.binary_search(data, username)
        if result != -1:
            tkinter.messagebox.showerror('Error', 'Username already exists')
        else:
            if self.firstname_val.get() == '' or self.lastname_ent.get() == '' or self.email_ent.get() == '' or \
                    self.username_val.get() == '' or self.password_val.get() == '' or self.contact_ent.get() == '':
                tkinter.messagebox.showerror(
                    'Error', 'Dont leave the fields empty.')
            else:
                self.exe.addlibrarian(self.firstname_ent.get(), self.lastname_ent.get(), self.email_ent.get(), self.username_ent.get(),
                                      self.password_ent.get(), self.contact_ent.get())
                tkinter.messagebox.showinfo(
                    'Success', 'User registered sucessfully')
                self.reset()

    def binary_search(self, list, key):
        '''Binary Search Algorithm'''
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][0] == key:
                return mid
            elif list[mid][0] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def reset(self):
        '''Clears data in the entry and combo boxes'''
        self.firstname_val.set('')
        self.lastname_val.set('')
        self.email_val.set('')
        self.username_val.set('')
        self.password_val.set('')
        self.contact_val.set('')

    def login(self):
        self.login = Toplevel(self.wn)
        login.loginPage(self.login)
        self.wn.withdraw()
