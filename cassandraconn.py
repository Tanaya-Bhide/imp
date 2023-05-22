from tkinter import *
from tkinter import messagebox
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

def connect_to_cassandra():
    cluster = Cluster(['localhost'])
    session = cluster.connect()
    session.set_keyspace('mykeyspace')
    return session

def create_record(session, name, address, phone):
    query = "INSERT INTO customers (name, address, phone) VALUES (%s, %s, %s)"
    session.execute(query, (name, address, phone))
    messagebox.showinfo("Success", "Record created successfully")

def read_record(session, name):
    query = "SELECT * FROM customers WHERE name = %s"
    result = session.execute(query, [name])
    for row in result:
        return f"name: {row.name}\naddress: {row.address}\nphone: {row.phone}\n"
    return "Record not found"

def update_record(session, name, address, phone):
    query = "UPDATE customers SET address = %s, phone = %s WHERE name = %s"
    session.execute(query, (address, phone, name))
    messagebox.showinfo("Success", "Record updated successfully")

def delete_record(session, name):
    query = "DELETE FROM customers WHERE name = %s"
    session.execute(query, [name])
    messagebox.showinfo("Success", "Record deleted successfully")

def clear_fields():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    text1.delete(1.0, END)

def create():
    session = connect_to_cassandra()
    create_record(session, entry1.get(), entry2.get(), entry3.get())
    clear_fields()

def read():
    session = connect_to_cassandra()
    result = read_record(session, entry1.get())
    text1.delete(1.0, END)
    text1.insert(END, result)

def update():
    session = connect_to_cassandra()
    update_record(session, entry1.get(), entry2.get(), entry3.get())
    clear_fields()

def delete():
    session = connect_to_cassandra()
    delete_record(session, entry1.get())
    clear_fields()

window = Tk()
window.title("Cassandra CRUD Application")

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
