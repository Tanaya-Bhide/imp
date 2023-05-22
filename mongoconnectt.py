from tkinter import *
from tkinter import messagebox
import pymongo

def connect_to_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    col = db["customers"]
    return col

def create_record(col, name, address, phone):
    mydict = {"name": name, "address": address, "phone": phone}
    col.insert_one(mydict)
    messagebox.showinfo("Success", "Record created successfully")

def read_record(col, name):
    result = col.find_one({"name": name})
    if result:
        return f"name: {result['name']}\naddress: {result['address']}\nphone: {result['phone']}\n"
    else:
        return "Record not found"

def update_record(col, name, address, phone):
    result = col.update_one({"name": name}, {"$set": {"address": address, "phone": phone}})
    if result.modified_count:
        messagebox.showinfo("Success", "Record updated successfully")
    else:
        messagebox.showerror("Error", "Record not found")

def delete_record(col, name):
    result = col.delete_one({"name": name})
    if result.deleted_count:
        messagebox.showinfo("Success", "Record deleted successfully")
    else:
        messagebox.showerror("Error", "Record not found")

def clear_fields():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    text1.delete(1.0, END)

def create():
    col = connect_to_mongo()
    create_record(col, entry1.get(), entry2.get(), entry3.get())
    clear_fields()

def read():
    col = connect_to_mongo()
    result = read_record(col, entry1.get())
    text1.delete(1.0, END)
    text1.insert(END, result)

def update():
    col = connect_to_mongo()
    update_record(col, entry1.get(), entry2.get(), entry3.get())
    clear_fields()

def delete():
    col = connect_to_mongo()
    delete_record(col, entry1.get())
    clear_fields()

window = Tk()
window.title("MongoDB CRUD Application")

label1 = Label(window, text="Name")
label1.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=1)

label2 = Label(window, text="Address")
label2.grid(row=1, column=0)
entry2 = Entry(window)
entry2.grid(row=1, column=1)

label3 = Label(window, text="Phone")
label3.grid(row=2, column=0)
entry3 = Entry(window)
entry3.grid(row=2, column=1)

button1 = Button(window, text="Create", command=create)
button1.grid(row=3, column=0)
button2 = Button(window, text="Read", command=read)
button2.grid(row=3, column=1)
button3 = Button(window, text="Update", command=update)
button3.grid(row=4, column=0)
button4 = Button(window, text="Delete", command=delete)
button4.grid(row=4, column=1)

text1 = Text(window, height=10, width=40)
text1.grid(row=5, column=0, columnspan=2)

window.mainloop()
