from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time
import Login
import Book_entry
import Book_issue


class home:

    def __init__(self, window):
        self.wn = window
        self.wn.title("Homepage")
        self.wn.geometry("500x400+500+100")
        self.Time = time.strftime('%H:%M%p')
        # Frames
        self.frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.frame.place(x=10, y=10, width=480, height=380)
        # Labels
        self.header = Label(self.frame, text='LIBRARY MANAGEMENT SYSTEM',
                            font=('Poppins', 20, 'bold'))
        self.header.place(x=20, y=10)
        # Buttons
        self.register_book = Button(
            self.frame, text='Register \nBook', height=2, width=10, font=('Poppins', 10, 'bold'), command=self.register_book)
        self.register_book.place(x=100, y=150)
        self.lend_book = Button(
            self.frame, text='Lend \nBook', height=2, width=10, font=('Poppins', 10, 'bold'), command=self.book_issue)
        self.lend_book.place(x=300, y=150)
        self.logout = Button(self.frame, text='Logout',
                             height=2, width=10, font=('Poppins', 10, 'bold'), command=self.logout)
        self.logout.place(x=100, y=250)
        self.exit = Button(
            self.frame, text='Exit', height=2, width=10, font=('Poppins', 10, 'bold'), command=self.exit)
        self.exit.place(x=300, y=250)
    # Methods

    def register_book(self):
        self.register_book = Toplevel(self.wn)
        Book_entry.bookEntry(self.register_book)
        self.wn.withdraw()

    def book_issue(self):
        self.book_issue = Toplevel(self.wn)
        Book_issue.bookIssue(self.book_issue)
        self.wn.withdraw()

    def logout(self):
        self.login = Toplevel(self.wn)
        Login.loginPage(self.login)
        self.wn.withdraw()

    def exit(self):
        self.wn.withdraw()


def main():
    window = Tk()
    home(window)
    window.mainloop()


if __name__ == '__main__':
    main()
