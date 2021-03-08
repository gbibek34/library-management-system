from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time


class home:

    def __init__(self, window):
        self.wn = window
        self.wn.title("Homepage")
        self.wn.geometry("500x500+500+100")
        self.Time = time.strftime('%H:%M%p')

        self.frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.frame.place(x=10, y=10, width=480, height=480)

        self.header = Label(self.frame, text='LIBRARY MANAGEMENT SYSTEM',
                            font=('Poppins', 20)).place(x=30, y=10)

        self.username = Label(self.frame, text='Username',
                              font=('Poppins', 10)).place(x=30, y=60)

        self.time = Entry(self.frame, font=('Poppins', 10), width=8)
        self.time.place(x=380, y=60)
        self.time.insert(0, self.Time)

        self.register_book = Button(self.frame).place()
        self.register_borrower = Button(self.frame).place()
        self.lend_book = Button(self.frame).place()
        self.exit = Button(self.frame).place()
        self.logout = Button(self.frame).place()


def main():
    window = Tk()
    home(window)
    window.mainloop()


if __name__ == '__main__':
    main()
