# Alfred Ukpong
# 24/03/25
# Week 9 

from tkinter import *
from tkinter import messagebox

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tennis Club Member Form")

        Label(master, text="Enter your Firstname").pack()
        self.entry_firstname = Entry(master)
        self.entry_firstname.pack()

        Label(master, text="Enter your Surname").pack()
        self.entry_surname = Entry(master)
        self.entry_surname.pack()

        Label(master, text="Enter your Date of Birth (YYYY-MM-DD)").pack()
        self.entry_dob = Entry(master)
        self.entry_dob.pack()

        Label(master, text="Enter your Member Type (Junior/Intermediate/Senior)").pack()
        self.entry_membertype = Entry(master)
        self.entry_membertype.pack()

        self.insert_button = Button(master, text="Insert Into DB", command=self.insert_member)
        self.insert_button.pack(pady=5)

        self.print_button = Button(master, text="Print All Members", command=self.print_members)
        self.print_button.pack(pady=5)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(pady=5)

    def insert_member(self):
        messagebox.showinfo("Insert", "Successful.")

    def print_members(self):
        messagebox.showinfo("Print", "Successful")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

