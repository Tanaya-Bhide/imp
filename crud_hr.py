from tkinter import *
import tkinter as tk
from tkinter import messagebox
import cx_Oracle

base = tk.Tk()
base.geometry("550x450")
base.title('CRUD Operations')

# Connect to the Oracle database
conn = cx_Oracle.connect("remote_2020BTECS00011/2020BTECS00011@10.10.16.23:1521/XEPDB1")
cursor = conn.cursor()

# Function to create a record
def create_record():
    id = enter_1.get()
    name = enter_2.get()
    branch = enter_3.get()
    cursor.execute("INSERT INTO student(id, name, branch) VALUES(:id, :name, :branch)", (id, name, branch))
    conn.commit()
    messagebox.showinfo("Information", "Record created successfully.")

# Function to read a record
def read_record():
    id = enter_1.get()
    cursor.execute("SELECT * FROM student WHERE id=:id", (id,))
    result = cursor.fetchone()
    if result:
        id = result[0]
        nm = result[1]
        pz = result[2]
        clear()
        enter_4.insert(0, id)
        enter_5.insert(0, nm)
        enter_6.insert(0, pz)
        messagebox.showinfo("Information", "Id: {0}, Name: {1}, Branch: {2}".format(id, nm, pz))
    else:
        messagebox.showinfo("Information", "Record not found.")

# Function to update a record
def update_record():
    id = enter_1.get()
    name = enter_2.get()
    branch = enter_3.get()
    cursor.execute("UPDATE student SET name=:name, branch=:branch WHERE id=:id", {"name": name, "branch": branch, "id": id})
    conn.commit()
    messagebox.showinfo("Information", "Record updated successfully.")

# Function to delete a record
def delete_record():
    id = enter_1.get()
    cursor.execute("DELETE FROM student WHERE id=:id", (id,))
    conn.commit()
    messagebox.showinfo("Information", "Record deleted successfully.")

# Function to clear the input fields
def clear():
    enter_4.delete(0, END)
    enter_5.delete(0, END)
    enter_6.delete(0, END)

# Create the labels and entry fields
lbl_0 = Label(base, text="Student Information", width=20, font=("bold", 20))
lbl_0.place(x=90, y=60)

lbl_1 = Label(base, text="Student Id", width=20, font=("bold", 10))
lbl_1.place(x=80, y=130)
enter_1 = Entry(base)
enter_1.place(x=240, y=130)

lbl_2 = Label(base, text="Student Name", width=20, font=("bold", 10))
lbl_2.place(x=80, y=180)
enter_2 = Entry(base)
enter_2.place(x=240, y=180)

lbl_3 = Label(base, text="Student Branch", width=20, font=("bold", 10))
lbl_3.place(x=80, y=230)
enter_3 = Entry(base)
enter_3.place(x=240, y=230)

enter_4 = Entry(base)
enter_4.place(x=70, y=280)
enter_5 = Entry(base)
enter_5.place(x=190, y=280)
enter_6 = Entry(base)
enter_6.place(x=310, y=280)

Button(base, text='Read', width=10, bg="black", fg='white', command=read_record).place(x=50, y=330)
Button(base, text='Insert', width=10, bg="black", fg='white', command=create_record).place(x=150, y=330)
Button(base, text='Update', width=10, bg="black", fg='white', command=update_record).place(x=250, y=330)
Button(base, text='Delete', width=10, bg="black", fg='white', command=delete_record).place(x=350, y=330)
Button(base, text='Exit', width=10, bg="black", fg='white', command=base.destroy).place(x=450, y=330)

base.mainloop()

