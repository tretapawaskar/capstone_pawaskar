from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('TekSystems sales repo')
#root.iconbitmap('c:/Users/treta/userinterface/teksystems.ico')
root.geometry("400x400")

# DB needs to be created
conn = sqlite3.connect('sales.db')

c = conn.cursor()

# Create table
''''
c.execute("""" CREATE TABLE addresses(
        first_name text,
        last_name txt,
        address txt,
        city txt,
        state txt,
        zipcode integer
        )"""")
'''
# Create submit function for DB

def submit():
    conn = sqlite3.connect('address_book_db')
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO address VALUES (:f_name, :l_name , :address, :city, :state, :zipcode)")
    conn.commit()
    conn.close()

def submit():
    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


f_name = Entry(root,width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root,width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root,width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root,width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root,width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root,width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create txt box labels
f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="city")
city_label.grid(row=3, column=0)

state_label = Label(root, text="state")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)

# Create submit button

submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#commit.Changes
conn.commit()

#Close.Connection
conn.close()

root.mainloop()












