import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk
from PIL import *
a=tk.Tk()
a.geometry("1550x900")
a.geometry("1550x900")
a.config(bg="#EDF4F4")

bg = Image.open(r"bg.jpg")
bg = ImageTk.PhotoImage(bg.resize((1550,900)))
photo = Label(a, image=bg)
photo.pack()

a.config(bg="#EDF4F4")
a.title("Login")

title = Label(a,text="Register",font=("Palatino Linotype", 40),bg="#EDF4F4",fg="black")
title.place(x=700,y=0)

L1 = Label(a,text="Username",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L1.place(x=500,y=150)

L1Entry = Entry(a,font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L1Entry.place(x=800,y=150)

L2 = Label(a,text="Password",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L2.place(x=500,y=250)

L2Entry = Entry(a,font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black",show="+")
L2Entry.place(x=800,y=250)

L3 = Label(a,text="Email",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L3.place(x=500,y=350)

L3Entry = Entry(a,font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L3Entry.place(x=800,y=350)

L4 = Label(a,text="Phone Number",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L4.place(x=500,y=450)

L4Entry = Entry(a,font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L4Entry.place(x=800,y=450)

L5 = Label(a,text="Degree",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L5.place(x=500,y=550)

L5Entry=Combobox(a,width=20,font=("Palatino Linotype", 20))
L5Entry["values"]=("Select Degree","B.E","B.Tech","B.Sc","MBA","M.Sc")
L5Entry.current(0)
L5Entry.place(x=800,y=550)

def register():
    username = L1Entry.get()
    password = L2Entry.get()
    email = L3Entry.get()
    phone = L4Entry.get()
    degree = L5Entry.get()
    
    if username=="" or password=="" or email=="" or phone=="" or degree=="":
        messagebox.showwarning("REGISTER", "Fill All The Details")
    elif (not email.endswith("@gmail.com")):
        messagebox.showwarning("REGISTER", "Enter Valid Email ID")
    elif len(phone)!=10:
        messagebox.showwarning("REGISTER", "Enter Valid Mobile Number")
    else:
        messagebox.showinfo("REGISTER", " ✌ Registered Successfully ✅ ")
        
        import pymysql as p
        #CONNECT A DATABASE
        db = p.connect(
            host="localhost",
            user="root",
            password="1234",
            database="mounika")
        c = db.cursor()
        query = "INSERT INTO REGISTER VALUES('%s','%s','%s','%s','%s')"%(username,password,email,phone,degree)
        try:
            c.execute(query)
            db.commit()
            db.close()
            messagebox.showinfo("REGISTER", " ✌ Stored Successfully ✅ ")
        except:
            db.rollback()
            db.close()
            messagebox.showinfo("REGISTER", " ✌ Not Stored ❌ ")
        import time
        time.sleep(2)
        a.destroy()
        import login

register = Button(a,text="Register",width=20,font=("Palatino Linotype", 20),bg="#ffffff",fg="black",command=register)
register.place(x=600,y=650)

a.mainloop()
