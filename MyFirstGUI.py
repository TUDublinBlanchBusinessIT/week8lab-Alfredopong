# Alfred Ukpong
# 24/03/25
# Week 9 

from tkinter import *
from tkinter import messagebox
import sqlite3

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

        self.print_button = Button(master, text="Print All Members", command=self.print_members)  # Ensure function exists
        self.print_button.pack(pady=5)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(pady=5)

    def insert_member(self):
        """Collects input, validates, and inserts a new member into the database."""
        firstname = self.entry_firstname.get().strip()
        surname = self.entry_surname.get().strip()
        dob = self.entry_dob.get().strip()
        member_type = self.entry_membertype.get().strip()

        if not firstname or not surname or not dob or not member_type:
            messagebox.showerror("Input Error", "All fields must be filled out!")
            return

        valid_types = ['Junior', 'Intermediate', 'Senior']
        if member_type not in valid_types:
            messagebox.showerror("Input Error", "Member Type must be Junior, Intermediate, or Senior!")
            return

        try:
            conn = sqlite3.connect("tennisclub.db")
            cursor = conn.cursor()

            sql = "INSERT INTO member (Firstname, Surname, DateOfBirth, MemberType) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (firstname, surname, dob, member_type))

            print(f"SQL Executed: INSERT INTO member (Firstname, Surname, DateOfBirth, MemberType) VALUES ('{firstname}', '{surname}', '{dob}', '{member_type}')")

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Member inserted successfully!")

            self.entry_firstname.delete(0, END)
            self.entry_surname.delete(0, END)
            self.entry_dob.delete(0, END)
            self.entry_membertype.delete(0, END)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def print_members(self):
        """Fetches all members from the database and displays them."""
        try:
            conn = sqlite3.connect("tennisclub.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM member")
            records = cursor.fetchall()

            conn.close()

            if not records:
                messagebox.showinfo("No Records", "No members found in the database.")
                return

            result_text = "ID | Firstname | Surname | DOB | Member Type\n"
            result_text += "-" * 50 + "\n"
            for record in records:
                result_text += f"{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}\n"

            messagebox.showinfo("Member Records", result_text)

            print(result_text)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

