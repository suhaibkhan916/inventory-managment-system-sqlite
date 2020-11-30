from tkinter.filedialog import asksaveasfile
from tkinter import *
from tkinter import messagebox,filedialog
import time
import random
from tkinter import Toplevel
from tkinter.ttk import Treeview
from tkinter import ttk
import sqlite3
import pandas
import csv
import os
import tempfile
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont, pdfmetrics
from reportlab.lib import colors
def Userwindow():
    # os.system('python backup.py')
    import backup
def Adminwindow():
    # sys.path.append(os.path.abspath(scriptpath))
    # sys.path.append(os.path.abspath('admin.py'))
    # os.system('python admin.py')
    # time.sleep(5)

    # os.system('python admin.py')
    # im=__import__('admin.py')
    # a=Admin()
    import admin
def destory():
    root.quit()
def clearadminvalues():
    adminnamevalue.set('')
    adminpasswordvalue.set('')
def userlogin():
    storeusername = StringVar()
    storepass = StringVar()
    userid = IntVar()
    uid = userid.get()
    usernamevalue.get()
    userpasswordvalue.get()
    conn = sqlite3.connect('japan.db')
    cursor = conn.cursor()
    finduser = ("SELECT u_id, u_name, password FROM user_table WHERE u_name=? AND password=?")
    cursor.execute(finduser, (usernamevalue.get(), userpasswordvalue.get(),))
    results = cursor.fetchall()
    if results:
        messagebox.showinfo("Welcome...", "login successfull ")
        clearuservalues()
        for i in results:
            uid = i[0]
            storeusername = i[1]
            storepass = i[2]
        print(uid)
        print(storeusername)
        print(storepass)
        root.destroy()
        Userwindow()
        # root.deiconify()
    else:
        messagebox.showerror("Login failed", "login failed please try again")
        clearuservalues()
def adminlogin():
    adminnamevalue.get()
    adminpasswordvalue.get()
    conn = sqlite3.connect('japan.db')
    cursor = conn.cursor()
    finduser = ("SELECT  admin_name, password FROM admin WHERE admin_name=? AND password=?")
    cursor.execute(finduser, (adminnamevalue.get(), adminpasswordvalue.get(),))
    results = cursor.fetchall()
    if results:
        messagebox.showinfo("Welcome...", "login successfull ")
        clearadminvalues()
        # root.withdraw()
        root.destroy()
        Adminwindow()
        # root.deiconify()

    else:
        messagebox.showerror("Login failed", "login failed please try again")
        clearadminvalues()
def clearuservalues():
    usernamevalue.set('')
    userpasswordvalue.set('')
root = Tk()
root.title("User And Admin Login | Japan Medical Company")
root.config(bg="white")
root.geometry("1000x700+200+50")
root.iconbitmap('pic.ico')
sliderLabel = Label(root, text="Japan Medical Company", relief=RIDGE, bd=5, font=("times", 30, "bold"), width=40,
                    bg="light cyan")
sliderLabel.pack(side=TOP, fill=X)
# -------------------------------------------admin data entry frame----------------------------------------------
admindataframe = Frame(root, bg="dark blue", relief=RIDGE, bd=10)
admindataframe.place(x=10, y=70, width=480, height=600)
admin_toplabel = Label(admindataframe, text="Admin Login", relief=RIDGE, bd=3, font=("times", 30, "bold"), width=40,
                       bg="dark blue",fg="white")
admin_toplabel.pack(side=TOP, fill=X)
# -------------------------------------------wegits for admin entry frame
adminnamelabel = Label(admindataframe, text="Admin Name", font=("times", 20, "bold"), bg="dark blue",fg="white")
adminnamelabel.place(x=160, y=90)
adminpasswordlbl = Label(admindataframe, text="Admin Password", font=("times", 20, "bold"), bg="dark blue" ,fg="white")
adminpasswordlbl.place(x=160, y=200)
adminnamevalue = StringVar()
adminpasswordvalue = StringVar()
adminnameentry = Entry(admindataframe, textvariable=adminnamevalue, font=("times", 20,), bd=5)
adminnameentry.place(x=90, y=140)
adminpasswordentry = Entry(admindataframe, textvariable=adminpasswordvalue, show="*", font=("times", 20,), bd=5)
adminpasswordentry.place(x=90, y=250)
adminloginbtn = Button(admindataframe, text='Login ', width=10, bg='sky blue', font=("times", 15, " bold"), bd=5,
                       activebackground='blue', activeforeground='white', relief=RIDGE, command=adminlogin)
adminloginbtn.place(x=260, y=340)
adminclearbtn = Button(admindataframe, text='Clear ', width=10, bg='sky blue', font=("times", 15, " bold"), bd=5,
                       activebackground='blue', activeforeground='white', relief=RIDGE, command=clearadminvalues)
adminclearbtn.place(x=90, y=340)
# -------------------------------------------user data entry frame-----------------------------------------------
userdataframe = Frame(root, bg="dark blue", relief=GROOVE, bd=10)
userdataframe.place(x=510, y=70, width=480, height=600)
user_toplabel = Label(userdataframe, text="User Login", relief=RIDGE, bd=3, font=("times", 30, "bold"), width=40,
                      bg="dark blue",fg="white")
user_toplabel.pack(side=TOP, fill=X)
usernamelabel = Label(userdataframe, text="User Name", font=("times", 20, "bold"), bg="dark blue",fg="white")
usernamelabel.place(x=160, y=90)
userpasswordlbl = Label(userdataframe, text="Password", font=("times", 20, "bold"), bg="dark blue",fg="white")
userpasswordlbl.place(x=165, y=200)
usernamevalue = StringVar()
userpasswordvalue = StringVar()
usernameentry = Entry(userdataframe, textvariable=usernamevalue, font=("times", 20,), bd=5)
usernameentry.place(x=90, y=140)
userpasswordentry = Entry(userdataframe, textvariable=userpasswordvalue, show="*", font=("times", 20,), bd=5)
userpasswordentry.place(x=90, y=250)
userloginbtn = Button(userdataframe, text='Login ', width=10, bg='sky blue', font=("times", 15, " bold"), bd=5,
                      activebackground='blue', activeforeground='white', relief=RIDGE, command=userlogin)
userloginbtn.place(x=260, y=340)
userclearbtn = Button(userdataframe, text='Clear ', width=10, bg='sky blue', font=("times", 15, " bold"), bd=5,
                      activebackground='blue', activeforeground='white', relief=RIDGE, command=clearuservalues)
userclearbtn.place(x=90, y=340)
root.mainloop()




