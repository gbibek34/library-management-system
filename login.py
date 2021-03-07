from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import register
import home
from query import librarian


class loginPage:

    def __init__(self, window):
        self.wn = window
        self.wn.title("Login")
        self.wn.geometry("500x500+500+100")
        self.exe = librarian()

        # =======================================================Labels==================================================
        self.username_lbl = Label(self.wn, text='Username:',
                                  font=('arial', 11)).place(x=80, y=200)
        self.password_lbl = Label(self.wn, text='Password:',
                                  font=('arial', 11)).place(x=80, y=240)
        # =======================================================Entries=================================================
        self.username_ent = Entry(self.wn, font=(
            'arial', 12), width=22)
        self.username_ent.place(x=180, y=200)
        self.password_ent = Entry(self.wn, font=('arial', 12),
                                  width=22, show='*')
        self.password_ent.place(x=180, y=240)
        # ==========================================================================================================
        self.delete_btn = Button(
            self.wn, text='Delete User', height=2, width=12, command=self.delete_librarian)
        self.delete_btn.place(x=10, y=10)
        self.login_btn = Button(self.wn, text='Login',
                                height=2, width=12, command=self.check_login)
        self.login_btn.place(x=120, y=340)
        self.register_btn = Button(
            self.wn, text='Register', height=2, width=12, command=self.register)
        self.register_btn.place(x=280, y=340)

    def check_login(self):
        '''Checks username password and user type to open the product and order entry windows'''
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
        '''Deletes the user account and details if credentials are correct'''
        data = self.exe.fetch_librarian()
        for i, j in data:
            if i == self.username_ent.get() and j == self.password_ent.get():
                self.exe.delete_librarian(self.username_ent.get())
                tkinter.messagebox.showinfo(
                    'Success', 'User removed successfully')
                return
        else:
            tkinter.messagebox.showerror('Failed', 'Check your credentials')
            return

    def register(self):
        self.register = Toplevel(self.wn)
        register.registerPage(self.register)
        self.wn.withdraw()

    def home(self):
        self.home = Toplevel(self.wn)
        home.home(self.home)
        self.wn.withdraw()


def main():
    '''Sets the class to work in tkinter'''
    window = Tk()
    loginPage(window)
    window.mainloop()


if __name__ == '__main__':
    main()
