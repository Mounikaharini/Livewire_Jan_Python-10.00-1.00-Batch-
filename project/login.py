import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import *
a=tk.Tk()
a.geometry("1550x900")
a.config(bg="#EDF4F4")

bg = Image.open(r"bg.jpg")
bg = ImageTk.PhotoImage(bg.resize((1550,900)))
photo = Label(a, image=bg)
photo.pack()

a.title("Login")

title = Label(a,text="Login",font=("Palatino Linotype", 40),bg="#EDF4F4",fg="black")
title.place(x=700,y=0)

L1 = Label(a,text="Username",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L1.place(x=500,y=150)

L1Entry = Entry(a,font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L1Entry.place(x=800,y=150)

L2 = Label(a,text="Password",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L2.place(x=500,y=250)

L2Entry = Entry(a,font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black",show="+")
L2Entry.place(x=800,y=250)

def login():
    username = L1Entry.get()
    password = L2Entry.get()
    if username=="" and password=="":
        messagebox.showwarning("LOGIN", "Fill All The Details")
    elif username=="admin" and password=="1234":
        messagebox.showinfo("LOGIN", "Logged In Successfully")
    else:
        messagebox.showerror("LOGIN", "Logged In Failed")
        
def register():
    a.destroy()
    import register
    
login = Button(a,text="login",width=12,font=("Palatino Linotype", 20),bg="white",fg="black",command=login)
login.place(x=680,y=350)


L3 = Label(a,text="Don't have an account ? click to register",font=("Palatino Linotype", 20),bg="#EDF4F4",fg="black")
L3.place(x=550,y=450)

register = Button(a,text="Register",width=20,font=("Palatino Linotype", 20),bg="white",fg="black",command=register)
register.place(x=600,y=550)

a.mainloop()
