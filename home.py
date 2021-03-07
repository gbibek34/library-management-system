from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class home:

    def __init__(self, window):
        self.wn = window
        self.wn.title("Homepage")
        self.wn.geometry("500x500+500+100")

        self.header = Label(self.wn, text='LIBRARY MANAGEMENT SYSTEM',
                            font=('Poppins', 20)).place(x=10, y=10)

        self.username = Label(self.wn, text='Username',
                              font=('Poppins', 10)).place(x=10, y=60)

        self.time = Label(self.wn, text='Time', font=(
            'Poppins', 10)).place(x=100, y=60)

        self.register_book = Button(self.wn).place()
        self.register_borrower = Button(self.wn).place()
        self.lend_book = Button(self.wn).place()
        self.exit = Button(self.wn).place()
        self.logout = Button(self.wn).place()


# def main():
#     '''Sets the class to work in tkinter'''
#     window = Tk()
#     home(window)
#     window.mainloop()


# if __name__ == '__main__':
#     main()
