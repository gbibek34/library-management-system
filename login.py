from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import Register
import Home
from Query import librarian


class loginPage:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Login")
        self.wn.geometry("500x500+500+100")
        self.exe = librarian()
        # Strings
        self.username_val = StringVar()
        self.password_val = StringVar()
        # Frame
        self.frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.frame.place(x=10, y=10, height=480, width=480)
        # =======================================================Labels==================================================
        self.header = Label(self.frame, text='Login Page',
                            font=('poppins', 15, 'bold')).place(x=180, y=120)
        self.username_lbl = Label(self.frame, text='Username:',
                                  font=('arial', 11)).place(x=80, y=200)
        self.password_lbl = Label(self.frame, text='Password:',
                                  font=('arial', 11)).place(x=80, y=240)
        # =======================================================Entries=================================================
        self.username_ent = Entry(self.frame, font=(
            'arial', 12), width=22, textvariable=self.username_val)
        self.username_ent.place(x=180, y=200)
        self.password_ent = Entry(self.frame, font=('arial', 12),
                                  width=22, show='*', textvariable=self.password_val)
        self.password_ent.place(x=180, y=240)
        # =======================================================Button=================================================
        self.delete_btn = Button(
            self.frame, text='Delete User', height=2, width=12, command=self.delete_librarian)
        self.delete_btn.place(x=10, y=10)
        self.login_btn = Button(self.frame, text='Login',
                                height=2, width=12, command=self.check_login)
        self.login_btn.place(x=120, y=340)
        self.register_btn = Button(
            self.frame, text='Register', height=2, width=12, command=self.register)
        self.register_btn.place(x=280, y=340)
    # =======================================================Methods=================================================

    def check_login(self):
        data = self.exe.fetch_librarian()
        for i, j in data:
            if i == self.username_ent.get() and j == self.password_ent.get():
                tkinter.messagebox.showinfo(
                    'Success', 'Welcome to Library Management System')
                self.home()
                return
        else:
            tkinter.messagebox.showerror(
                'Login Failed', 'Invalid Username or Password')

    def delete_librarian(self):
        data = self.exe.fetch_librarian()
        for i, j in data:
            if i == self.username_ent.get() and j == self.password_ent.get():
                self.exe.delete_librarian(self.username_ent.get())
                tkinter.messagebox.showinfo(
                    'Success', 'User removed successfully')
                self.reset()
                return
        else:
            tkinter.messagebox.showerror('Failed', 'Check your credentials')
            return

    def reset(self):
        self.username_val.set('')
        self.password_val.set('')

    def register(self):
        self.register = Toplevel(self.wn)
        Register.registerPage(self.register)
        self.wn.withdraw()

    def home(self):
        self.home = Toplevel(self.wn)
        Home.home(self.home)
        self.wn.withdraw()


def main():
    '''Sets the class to work in tkinter'''
    window = Tk()
    loginPage(window)
    window.mainloop()


if __name__ == '__main__':
    main()
