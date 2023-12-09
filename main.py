import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import webbrowser
from PIL import Image, ImageTk
from tkinter import scrolledtext
import datetime
import re
import PyPDF2
from tkinter import simpledialog
import time

n1=datetime.datetime.now()
x1=n1.strftime("%x")
fx2=n1.strftime("%X")

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tkcalendar import Calendar
from tkcalendar import DateEntry

root = tk.Tk()
root.configure(bg='skyblue')
window_width = 1200
window_height = 700

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#root.geometry('1200x750')
root.title('Fast Food Management Sysytem')
root.resizable(False,False)
    
def open_link():
    url = "https://www.goole.com"  # Replace this with your desired link
    webbrowser.open(url)

def del_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def init(page):
    del_pages()
    page()

options_frame = tk.Frame(root, bg='#c3c3c3')

Emp_btn = ttk.Button(options_frame,text='Employee',
                     command=lambda: init(Emp)).grid(row=0,column=1)#place(x=90,y=10)
Cus_btn = ttk.Button(options_frame,text='Customer',
                     command=lambda: init(Cus)).grid(row=0,column=2)#place(x=210,y=10)
Menu_btn = ttk.Button(options_frame,text='Menu',
                     command=lambda: init(Mu)).grid(row=0,column=4)#place(x=410,y=10)
Raw_btn = ttk.Button(options_frame,text='Inventory',
                     command=lambda: init(Ra)).grid(row=0,column=5)#place(x=410,y=10)
Sup_btn = ttk.Button(options_frame,text='Supplier',
                     command=lambda: init(Sup)).grid(row=0,column=3)#place(x=320,y=10)
CusB_btn = ttk.Button(options_frame,text='Customer Bill',
                     command=lambda: init(CusB)).grid(row=0,column=7)#place(x=810,y=10)
SupB_btn = ttk.Button(options_frame,text='Supplier Bill',
                     command=lambda: init(SupB)).grid(row=0,column=8)#place(x=960,y=10)
options_frame.pack()
options_frame.pack_propagate(False)
options_frame.configure(width=1200,height=100)

main_frame = tk.Frame(root,highlightbackground="black"
                      ,highlightthickness=2)

d=tk.Label(options_frame,text="Date :"+x1,font=('Bold',25),padx=50,bg='light green').grid(row=0,column=0)

image_path = "cafe.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
image_label = tk.Label(main_frame, image=photo)
image_label.pack(pady=100)

main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(height=700,width=1200)

def verify():
    
    p=tkinter.simpledialog.askstring("Verification","Enter Password",show='*')

    if(p!="Admin"):
        tkinter.messagebox.askretrycancel('Alert !!','Wrong Password')
        verify()
    else:
        tkinter.messagebox.showinfo('Congratulations !!','Login Successful')

verify()
    
Id = StringVar()
name = StringVar()
email = StringVar()
gen = StringVar()
doj = StringVar()
dob = StringVar()
phone = StringVar()
des = StringVar()
add= StringVar()
date = StringVar()
OBId = StringVar()
Mid1 = StringVar()
Mname1 = StringVar()
Mqty1 = StringVar()
Mmrp1 = StringVar()
Mtot1 = StringVar()
Mid2 = StringVar()
Mname2 = StringVar()
Mqty2 = StringVar()
Mmrp2 = StringVar()
Mtot2 = StringVar()
Mid3 = StringVar()
Mname3 = StringVar()
Mqty3 = StringVar()
Mmrp3 = StringVar()
Mtot3 = StringVar()
Mid4 = StringVar()
Mname4 = StringVar()
Mqty4 = StringVar()
Mmrp4 = StringVar()
Mtot4 = StringVar()
Mid5 = StringVar()
Mname5 = StringVar()
Mqty5 = StringVar()
Mmrp5 = StringVar()
Mtot5 = StringVar()
BAmt = StringVar()

a=b=c=d=""
    
def Emp():   ### EMPLOYEE TABLE
    E_head=tk.Frame(main_frame)
    lb = tk.Label(E_head,text="Employee Page",
                  font=('Bold',40)).grid(row=0,columnspan=4)
    E_head.pack()
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Employee(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name text,Email text, gender text,Date_Of_Joining text,
        Date_Of_Birth text,Phone text,Designation text,Address text)''')
    con.commit

    cur.execute('''select ID from Employee''')
    for record in cur:
        print(str(record[0]))
    
    def show_data():
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        doj1=doj.get()
        dob1=dob.get()
        phone1=phone.get()
        des1=des.get()
        add1=add.get()
        E_frame=tk.Frame(main_frame)
        print("RECORDS")
        cur.execute('''select * from Employee''')
        #data = cur.fetchall()
        for record in cur:
            print('ID :',str(record[0])+'\n')
            print('Name:',str(record[1])+'\n')
            print('Email:',str(record[2])+'\n')
            print('gender:',str(record[3])+'\n')
            print('Date_Of_Joining:',str(record[4])+'\n')
            print('Date_Of_Birth:',str(record[5])+'\n')
            print('Phone:',str(record[6])+'\n')
            print('Designation:',str(record[7])+'\n')
            print('Address:',str(record[8])+'\n')
        con.commit()
        #Id.set("")
        name.set("")
        email.set("")
        gen.set("")
        doj.set("")
        dob.set("")
        phone.set("")
        des.set("")
        add.set("")

        try:
            a=str(record[0])
            a=int(a)+1
            Id.set(a)
        except:
            Id.set("1")
        E_frame.pack()
        
    show_data()
    

    def adde():        #ADDING DATA
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        doj1=doj.get()
        dob1=dob.get()
        phone1=phone.get()
        des1=des.get()
        add1=add.get()
        
        cur.execute('''Insert into Employee(Name,Email,gender,
                        Date_Of_Joining,Date_Of_Birth,Phone,Designation,Address)
                        values(?,?,?,?,?,?,?,?)''',(name1,email1,gen1,doj1,dob1,phone1,des1,add1))
        tkinter.messagebox.showinfo('Congratulations !!','Employee successfully Added')
            
        
        con.commit()
        show_data()

    def check():
        Id1=Id.get()
        if(Id1==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Id1))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        name1=name.get()
        if(name1==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', name1))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
                
        email1=email.get()
        
        phone1=phone.get()
        if(phone1==""):
            tkinter.messagebox.showerror('Error !!','Phone Number Cannot be Empty')
        else:
            c=bool(re.search(r'\d', phone1))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in Phone')
                
        des1=des.get()
        if(des1==""):
            tkinter.messagebox.showerror('Error !!','Destination Cannot be Empty')
        else:
            d=bool(re.search(r'\d', des1))
            if(d==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Destination')
        try:        
            if(a==True and b==False and c==True and d==False):
                adde()
        except:
            print("Error")

            
    def upe():  #UPDATING DATA
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        doj1=doj.get()
        dob1=dob.get()
        phone1=phone.get()
        des1=des.get()
        add1=add.get()
        if(a and b == False ):
            cur.execute('''Update Employee
                    SET Name=?,Email=?,gender=?, Date_Of_Joining=?,
                    Date_Of_Birth=?,Phone=?,Designation=?,Address=?
                    WHERE ID=?''',(name1,email1,gen1,doj1,dob1,phone1,des1,add1,Id1,))
            con.commit()
            show_data()
            tkinter.messagebox.showinfo('Congratulations !!','Employee successfully updated')
            

    def checkU():
        Id1=Id.get()
        if(Id1==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Id1))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        name1=name.get()
        if(name1==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', name1))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
                
        email1=email.get()
        
        phone1=phone.get()
        if(phone1==""):
            tkinter.messagebox.showerror('Error !!','Phone Number Cannot be Empty')
        else:
            c=bool(re.search(r'\d', phone1))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in Phone')
                
        des1=des.get()
        if(des1==""):
            tkinter.messagebox.showerror('Error !!','Destination Cannot be Empty')
        else:
            d=bool(re.search(r'\d', des1))
            if(d==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Destination')
                
        try:        
            if(a==True and b==False and c==True and d==False):
                upe()
        except:
            print("Error")

    def dele():
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    Id1=Id.get()
                    cur.execute('''Delete from Employee where ID=?''',(Id1,))
                    con.commit()
                    tkinter.messagebox.showinfo('Congratulations !!','Employee successfully Deleted')
                    show_data()
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')

    def toggle_entry_state():
        current_state = Emp_id['state']
        if current_state == 'normal':
            Emp_id.config(state='readonly')
            toggle_button['text'] = 'Enable Entry'
        else:
            Emp_id.config(state='normal')
            toggle_button['text'] = 'Disable Entry'

    def ad():
        lambda:init(Emp)
        add_Emp=ttk.Button(Emp_frame,text="ADD NEW",command=check).grid(row=6,column=0)
        up_Emp=ttk.Button(Emp_frame,text="      ",command=checkU,state='disabled').grid(row=6,column=1)

    def up():
        lambda:init(Emp)
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    up_Emp=ttk.Button(Emp_frame,text="Update",command=checkU).grid(row=6,column=1)
                    add_Emp=ttk.Button(Emp_frame,text="               ",command=check,state='disabled').grid(row=6,column=0)
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')
                
    Emp_frame=tk.Frame(main_frame)
    Emp_frame.pack()
    add1_Emp=ttk.Button(Emp_frame,text="New Entry",command=ad).grid(row=0,column=0)
    up1_Emp=ttk.Button(Emp_frame,text="Update Form",command=up).grid(row=0,column=1)
    Emp_ID=tk.Label(Emp_frame,text="Employee ID",font=('Bold',25),padx=15,pady=15).grid(row=1,column=0)
    Emp_id=tk.Entry(Emp_frame,textvariable=Id,font=('Bold',25), state='readonly').grid(row=1,column=1)

    Emp_Name=tk.Label(Emp_frame,text="Employee Name",font=('Bold',25),padx=15,pady=15).grid(row=1,column=2)
    Emp_name=tk.Entry(Emp_frame,textvariable=name,font=('Bold',25)).grid(row=1,column=3)
    
    Emp_Email=tk.Label(Emp_frame,text="Email Id",font=('Bold',25),padx=15,pady=15).grid(row=2,column=0)
    Emp_email=tk.Entry(Emp_frame,textvariable=email,font=('Bold',25)).grid(row=2,column=1)
    
    Emp_Gen=tk.Label(Emp_frame,text="Gender",font=('Bold',25),padx=15,pady=15).grid(row=2,column=2)
    Emp_gen = ttk.Combobox(Emp_frame,textvariable=gen)
    Emp_gen['values'] = ["Male","Female","Others"]
    Emp_gen.set(" Select Gender ")
    def on_combo_select(event):
        selected_item = Emp_gen.get()

    Emp_gen.bind("<<ComboboxSelected>>", on_combo_select)
    Emp_gen.grid(row=2,column=3)
    
    EDOJ=tk.Label(Emp_frame,text="Date Of joining",font=('Bold',25),padx=15,pady=15).grid(row=3,column=0)
    edoj = DateEntry(Emp_frame, selectmode="day",textvariable=doj).grid(row=3,column=1)
    
    EDOB=tk.Label(Emp_frame,text="Date Of Birth",font=('Bold',25),padx=15,pady=15).grid(row=3,column=2)
    edob= DateEntry(Emp_frame, selectmode="day",year=20,textvariable=dob).grid(row=3,column=3)
    
    Ephone=tk.Label(Emp_frame,text="Phone no:",font=('Bold',25),padx=15,pady=15).grid(row=4,column=0)
    ephone=tk.Entry(Emp_frame,textvariable=phone,font=('Bold',25)).grid(row=4,column=1)
    
    EDesignation=tk.Label(Emp_frame,text="Designation",font=('Bold',25),padx=15,pady=15).grid(row=4,column=2)
    edes=tk.Entry(Emp_frame,textvariable=des,font=('Bold',25)).grid(row=4,column=3)
    
    Address=tk.Label(Emp_frame,text="Address",font=('Bold',25),padx=15,pady=15).grid(row=5,column=0)
    Add=tk.Entry(Emp_frame,width=50,textvariable=add).grid(row=5,column=1,columnspan=3)
    del_Emp=ttk.Button(Emp_frame,text="Delete",command=dele).grid(row=6,column=2)
    re_Emp=ttk.Button(Emp_frame,text="Clear",command=show_data).grid(row=6,column=3)


Emp()

def Cus():   #Customer TABLE
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Customer(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name text,Email text, gender text,Date_Of_Birth text,Phone text,Address text)''')
    def show_data():
        print("RECORDS")
        con= sqlite3.connect('FFMS.db')
        cur= con.cursor()
        cur.execute('''select * from Customer''')
        for record in cur:
            print('ID :',str(record[0])+'\n')
            print('Name:',str(record[1])+'\n')
            print('Email:',str(record[2])+'\n')
            print('gender:',str(record[3])+'\n')
            print('Date_Of_Birth:',str(record[4])+'\n')
            print('Phone:',str(record[5])+'\n')
            print('Address:',str(record[6])+'\n')
        #Id.set("")
        name.set("")
        email.set("")
        gen.set("")
        doj.set("")
        dob.set("")
        phone.set("")
        des.set("")
        add.set("")

        try:
            a=str(record[0])
            a=int(a)+1
            Id.set(a)
        except:
            Id.set("1")
    show_data()
    
    def adde():           #ADDING DATA
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        dob1=dob.get()
        phone1=phone.get()
        add1=add.get()
        
        cur.execute('''Insert into Customer(Name,Email,gender,
            Date_Of_Birth,Phone,Address)values(?,?,?,?,?,?)''',(name1,email1,gen1,dob1,phone1,add1))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer successfully Added')

    def check():
        Id1=Id.get()
        if(Id1==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Id1))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        name1=name.get()
        if(name1==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', name1))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
                
        email1=email.get()
        
        phone1=phone.get()
        if(phone1==""):
            tkinter.messagebox.showerror('Error !!','Phone Number Cannot be Empty')
        else:
            c=bool(re.search(r'\d', phone1))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in Phone')
                
        try:        
            if(a==True and b==False and c==True):
                adde()
        except:
            print("Error")

    def upe():         #UPDATING DATA
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        dob1=dob.get()
        phone1=phone.get()
        add1=add.get()
    
        cur.execute('''Update Customer SET Name=?,Email=?,gender=?,
                    Date_Of_Birth=?,Phone=?,Address=?
                    WHERE ID=?''',(name1,email1,gen1,dob1,phone1,add1,Id1,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer successfully updated')

    def checkU():
        Id1=Id.get()
        if(Id1==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Id1))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        name1=name.get()
        if(name1==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', name1))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
                
        email1=email.get()
        
        phone1=phone.get()
        if(phone1==""):
            tkinter.messagebox.showerror('Error !!','Phone Number Cannot be Empty')
        else:
            c=bool(re.search(r'\d', phone1))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in Phone')
                
        try:        
            if(a==True and b==False and c==True):
                upe()
        except:
            print("Error")

    def ad():
        lambda:init(Emp)
        add_Emp=ttk.Button(Cus_frame,text="ADD NEW",command=check).grid(row=6,column=0)
        up_Emp=ttk.Button(Cus_frame,text="      ",command=checkU,state='disabled').grid(row=6,column=1)

    def up():
        lambda:init(Emp)
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    up_Emp=ttk.Button(Cus_frame,text="Update",command=checkU).grid(row=6,column=1)
                    add_Emp=ttk.Button(Cus_frame,text="                ",command=check,state='disabled').grid(row=6,column=0)
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')
    
    def dele():
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    Id1=Id.get()
                    cur.execute('''Delete from Customer where ID=?''',(Id1,))
                    con.commit()
                    tkinter.messagebox.showinfo('Congratulations !!','Customer successfully Deleted')
                    show_data()
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')
    
    Cus_frame=tk.Frame(main_frame)
    add1_Emp=ttk.Button(Cus_frame,text="New Entry",command=ad).grid(row=0,column=0)
    up1_Emp=ttk.Button(Cus_frame,text="Update Form",command=up).grid(row=0,column=1)
    
    lb = tk.Label(Cus_frame,text="Customer Page",
                  font=('Bold',40)).grid(row=0,column=2,columnspan=4)#place(x=200,y=450)
    Cus_ID=tk.Label(Cus_frame,text="Customer ID",font=('Bold',25),padx=15,pady=15).grid(row=1,column=0)
    Cus_id=tk.Entry(Cus_frame,textvariable=Id,font=('Bold',25),state='readonly').grid(row=1,column=1)
    
    Cus_Name=tk.Label(Cus_frame,text="Customer Name",font=('Bold',25),padx=15,pady=15).grid(row=1,column=2)
    Cus_name=tk.Entry(Cus_frame,textvariable=name,font=('Bold',25)).grid(row=1,column=3)
    
    Cus_Email=tk.Label(Cus_frame,text="Email Id",font=('Bold',25),padx=15,pady=15).grid(row=2,column=0)
    Cus_email=tk.Entry(Cus_frame,textvariable=email,font=('Bold',25)).grid(row=2,column=1)
    
    Cus_Gen=tk.Label(Cus_frame,text="Gender",font=('Bold',25),padx=15,pady=15).grid(row=2,column=2)
    Emp_gen = ttk.Combobox(Cus_frame,textvariable=gen)
    Emp_gen['values'] = ["Male","Female","Others"]
    Emp_gen.set(" Select Gender ")
    def on_combo_select(event):
        selected_item = Emp_gen.get()

    Emp_gen.bind("<<ComboboxSelected>>", on_combo_select)
    Emp_gen.grid(row=2,column=3)
    
    CDOB=tk.Label(Cus_frame,text="Date Of Birth",font=('Bold',25),padx=15,pady=15).grid(row=3,column=2)
    cdob= DateEntry(Cus_frame, selectmode="day",year=20,textvariable=dob).grid(row=3,column=3)
    
    Cphone=tk.Label(Cus_frame,text="Phone no:",font=('Bold',25),padx=15,pady=15).grid(row=3,column=0)
    cphone=tk.Entry(Cus_frame,textvariable=phone,font=('Bold',25)).grid(row=3,column=1)
    
    Address=tk.Label(Cus_frame,text="Address",font=('Bold',25),padx=15,pady=15).grid(row=5,column=0)
    Add=tk.Entry(Cus_frame,width=50,textvariable=add,font=('Bold',25)).grid(row=5,column=1,columnspan=3)
    del_Emp=ttk.Button(Cus_frame,text="Delete",command=dele).grid(row=6,column=2)
    re_Emp=ttk.Button(Cus_frame,text="clear",command=show_data).grid(row=6,column=3)
    Cus_frame.pack()

Cus()
    
def Sup():   # SUPPLIER TABLE
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Supplier(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name text,Email text, gender text,
        Date_Of_Birth text,Phone text,Address text)''')
    def show_data():
        print("RECORDS")
        con= sqlite3.connect('FFMS.db')
        cur= con.cursor()
        cur.execute('''select * from Supplier''')
        for record in cur:
            print('ID :',str(record[0])+'\n')
            print('Name:',str(record[1])+'\n')
            print('Email:',str(record[2])+'\n')
            print('gender:',str(record[3])+'\n')
            print('Date_Of_Birth:',str(record[4])+'\n')
            print('Phone:',str(record[5])+'\n')
            print('Address:',str(record[6])+'\n')
        #Id.set("")
        name.set("")
        email.set("")
        gen.set("")
        doj.set("")
        dob.set("")
        phone.set("")
        des.set("")
        add.set("")

        try:
            a=str(record[0])
            a=int(a)+1
            Id.set(a)
        except:
            Id.set("1")
        
    show_data()
    
    def adde():     #ADDING DATA
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        dob1=dob.get()
        phone1=phone.get()
        add1=add.get()
        cur.execute('''Insert into Supplier(Name,Email,gender,
            Date_Of_Birth,Phone,Address)values(?,?,?,?,?,?)''',(name1,email1,gen1,dob1,phone1,add1))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier successfully Added')

    def check():
        Id1=Id.get()
        if(Id1==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Id1))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        name1=name.get()
        if(name1==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', name1))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
                
        email1=email.get()
        
        phone1=phone.get()
        if(phone1==""):
            tkinter.messagebox.showerror('Error !!','Phone Number Cannot be Empty')
        else:
            c=bool(re.search(r'\d', phone1))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in Phone')
                
        try:        
            if(a==True and b==False and c==True):
                adde()
        except:
            print("Error")

    def upe():       #UPDATING DATA 
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        dob1=dob.get()
        phone1=phone.get()
        add1=add.get()
        cur.execute('''Update Supplier SET Name=?,Email=?,gender=?,
                    Date_Of_Birth=?,Phone=?,Address=?
                    WHERE ID=?''',(name1,email1,gen1,dob1,phone1,add1,Id1,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier successfully updated')

    def checkU():
        Id1=Id.get()
        if(Id1==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Id1))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        name1=name.get()
        if(name1==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', name1))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
                
        email1=email.get()
        
        phone1=phone.get()
        if(phone1==""):
            tkinter.messagebox.showerror('Error !!','Phone Number Cannot be Empty')
        else:
            c=bool(re.search(r'\d', phone1))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in Phone')
                
        try:        
            if(a==True and b==False and c==True):
                upe()
        except:
            print("Error")

    def ad():
        lambda:init(Emp)
        add_Emp=ttk.Button(Sup_frame,text="ADD NEW",command=check).grid(row=6,column=0)
        up_Emp=ttk.Button(Sup_frame,text="      ",command=checkU,state='disabled').grid(row=6,column=1)

    def up():
        lambda:init(Emp)
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    up_Emp=ttk.Button(Sup_frame,text="Update",command=checkU).grid(row=6,column=1)
                    add_Emp=ttk.Button(Sup_frame,text="              ",command=check,state='disabled').grid(row=6,column=0)
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')

    def dele():
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    Id1=Id.get()
                    cur.execute('''Delete from Supplier where ID=?''',(Id1,))
                    con.commit()
                    tkinter.messagebox.showinfo('Congratulations !!','Supplier successfully Deleted')
                    show_data()
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')

    
    Sup_frame=tk.Frame(main_frame)
    add1_Emp=ttk.Button(Sup_frame,text="New Entry",command=ad).grid(row=0,column=0)
    up1_Emp=ttk.Button(Sup_frame,text="Update Form",command=up).grid(row=0,column=1)
    
    lb = tk.Label(Sup_frame,text="Supplier Page",
                  font=('Bold',40)).grid(row=0,column=2,columnspan=4)
    Sup_ID=tk.Label(Sup_frame,text="Supplier ID",font=('Bold',25),padx=15,pady=15).grid(row=1,column=0)
    Sup_id=tk.Entry(Sup_frame,textvariable=Id,font=('Bold',25),state='readonly').grid(row=1,column=1)
    
    Sup_Name=tk.Label(Sup_frame,text="Supplier Name",font=('Bold',25),padx=15,pady=15).grid(row=1,column=2)
    Sup_name=tk.Entry(Sup_frame,textvariable=name,font=('Bold',25)).grid(row=1,column=3)
    
    Sup_Email=tk.Label(Sup_frame,text="Email Id",font=('Bold',25),padx=15,pady=15).grid(row=2,column=0)
    Sup_email=tk.Entry(Sup_frame,textvariable=email,font=('Bold',25)).grid(row=2,column=1)
    
    Sup_Gen=tk.Label(Sup_frame,text="Gender",font=('Bold',25),padx=15,pady=15).grid(row=2,column=2)
    Emp_gen = ttk.Combobox(Sup_frame,textvariable=gen)
    Emp_gen['values'] = ["Male","Female","Others"]
    Emp_gen.set(" Select Gender ")
    def on_combo_select(event):
        selected_item = Emp_gen.get()

    Emp_gen.bind("<<ComboboxSelected>>", on_combo_select)
    Emp_gen.grid(row=2,column=3)
    
    SDOB=tk.Label(Sup_frame,text="Date Of Birth",font=('Bold',25),padx=15,pady=15).grid(row=3,column=2)
    sdob= DateEntry(Sup_frame, selectmode="day",year=20,textvariable=dob).grid(row=3,column=3)
    
    Sphone=tk.Label(Sup_frame,text="Phone no:",font=('Bold',25),padx=15,pady=15).grid(row=3,column=0)
    sphone=tk.Entry(Sup_frame,textvariable=phone,font=('Bold',25)).grid(row=3,column=1)
    
    Address=tk.Label(Sup_frame,text="Address",font=('Bold',25),padx=15,pady=15).grid(row=5,column=0)
    Add=tk.Entry(Sup_frame,width=50,textvariable=add,font=('Bold',15)).grid(row=5,column=1,columnspan=3)
    del_Emp=ttk.Button(Sup_frame,text="Delete",
                      command=dele).grid(row=6,column=2)
    re_Emp=ttk.Button(Sup_frame,text="Clear",
                     command=show_data).grid(row=6,column=3)
    Sup_frame.pack()

Sup()

def Mu():
    Mid11 =Mid1.get()
    Mname11 = Mname1.get()
    Mqty11 = Mqty1.get()
    Mmrp11 = Mmrp1.get()

    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Menu(Menu_id INTEGER PRIMARY KEY AUTOINCREMENT,Menu_name text,
    Menu_Qty text,Menu_MRP text)''')


    def show_data():
        print("RECORDS")
        cur.execute('''select * from Menu''')
        for record in cur:
            print('Menu_id:',str(record[0])+'\n')
            print('Menu_name:',str(record[1])+'\n')
            print('Menu_Qty:',str(record[2])+'\n')
            print('Menu_MRP:',str(record[3]+'\n'))
        Mid1.set("")
        Mname1.set("")
        Mqty1.set("")
        Mmrp1.set("")
        Mtot1.set("")

        try:
            a=str(record[0])
            a=int(a)+1
            Mid1.set(a)
        except:
            Mid1.set("1")
    show_data()

    def adde():        #ADDING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        cur.execute('''Insert into Menu(Menu_name,Menu_Qty,Menu_MRP)values(?,?,?)''',(Mname11,Mqty11,Mmrp11))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully Added')

    def check():
        Mid11=Mid1.get()
        if(Mid11==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Mid11))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        Mname11=Mname1.get()
        if(Mname11==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', Mname11))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
        
        Mmrp11=Mmrp1.get()
        if(Mmrp11==""):
            tkinter.messagebox.showerror('Error !!','MRP Cannot be Empty')
        else:
            c=bool(re.search(r'\d', Mmrp11))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in MRP')

        try:        
            if(a==True and b==False and c==True):
                adde()
        except:
            print("Error")
            
    def upe():  #UPDATING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        cur.execute('''Update Menu SET Menu_name=?,
                Menu_Qty=?,Menu_MRP=?
                where Menu_id=?''',(Mname11,Mqty11,Mmrp11,Mid11,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully updated')

    def checku():
        Mid11=Mid1.get()
        if(Mid11==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Mid11))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        Mname11=Mname1.get()
        if(Mname11==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', Mname11))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
        
        Mmrp11=Mmrp1.get()
        if(Mmrp11==""):
            tkinter.messagebox.showerror('Error !!','MRP Cannot be Empty')
        else:
            c=bool(re.search(r'\d', Mmrp11))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in MRP')

        try:        
            if(a==True and b==False and c==True):
                upe()
        except:
            print("Error")

    def ad():
        add_Emp=ttk.Button(mu_frame,text="ADD NEW",command=check).grid(row=6,column=0)
        up_Emp=ttk.Button(mu_frame,text="      ",command=checku,state='disabled').grid(row=6,column=1)

    def up():
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    up_Emp=ttk.Button(mu_frame,text="Update",command=checku).grid(row=6,column=1)
                    add_Emp=ttk.Button(mu_frame,text="             ",command=check,state='disabled').grid(row=6,column=0)
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')

    def dele():
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Mid1.set(p)
                    Mid11=Mid1.get()
                    cur.execute('''Delete from Supplier where ID=?''',(Mid11,))
                    con.commit()
                    tkinter.messagebox.showinfo('Congratulations !!','Supplier successfully Deleted')
                    show_data()
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')
        
    mu_frame=tk.Frame(main_frame)
    add1_Emp=ttk.Button(mu_frame,text="New Entry",command=ad).grid(row=0,column=0)
    up1_Emp=ttk.Button(mu_frame,text="Update Form",command=up).grid(row=0,column=1)
    lb = tk.Label(mu_frame,text="Menu Page",
                  font=('Bold',40)).grid(row=0,column=2,columnspan=5)#place(x=200,y=450)
    MU_ID=tk.Label(mu_frame,text="Menu ID",font=('Bold',25),pady=15).grid(row=3,column=0)
    MU_Name=tk.Label(mu_frame,text="Name",font=('Bold',25)).grid(row=3,column=1)
    MU_QTY=tk.Label(mu_frame,text="Serving Size",font=('Bold',25)).grid(row=3,column=2)
    MU_MRP=tk.Label(mu_frame,text="MRP",font=('Bold',25)).grid(row=3,column=3)

### Menu item 1
    MU_id1=tk.Entry(mu_frame,textvariable=Mid1,font=('Bold',15),state='readonly').grid(row=4,column=0)

    MU_name1=tk.Entry(mu_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    #MU_qty1=tk.Entry(mu_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)
    
    combo_qty = ttk.Combobox(mu_frame)
    combo_qty['values'] = [1,2,3,4]
    combo_qty.set(" ")
    def on_combo_select(event):
        selected_item = combo_qty.get()

    combo_qty.bind("<<ComboboxSelected>>", on_combo_select)
    combo_qty.grid(row=4,column=2)

    MU_mrp1=tk.Entry(mu_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)
    del_Emp=ttk.Button(mu_frame,text="Delete",
                      command=dele).grid(row=6,column=2)
    re_Emp=ttk.Button(mu_frame,text="show data",
                     command=show_data).grid(row=6,column=3)
    mu_frame.pack()

Mu()

def retrieve_datas():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Name FROM Supplier")
    data = cursor.fetchall()
    connection.close()
    return data

def Ra():
    Mid11 =Mid1.get()
    Mname11 = Mname1.get()
    Mqty11 = Mqty1.get()
    Mmrp11 = Mmrp1.get()

    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Raw_Material(Menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Menu_name text,Supplier_name text,Menu_Qty text,Menu_MRP text)''')


    def show_data():
        print("RECORDS")
        cur.execute('''select * from Raw_Material''')
        for record in cur:
            print('Raw Material id:',str(record[0])+'\n')
            print('Raw Material name:',str(record[1])+'\n')
            print('Supplier Name:',str(record[2])+'\n')
            print('Raw Material Qty:',str(record[3])+'\n')
            print('Raw Material MRP:',str(record[4]+'\n'))
        Mid1.set("")
        Mname1.set("")
        Mqty1.set("")
        Mmrp1.set("")

        try:
            a=str(record[0])
            a=int(a)+1
            Mid1.set(a)
        except:
            Mid1.set("1")
    show_data()

    def adde():        #ADDING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        name1=name.get()
        cur.execute('''Insert into Raw_Material(Menu_name,Supplier_name,Menu_Qty,Menu_MRP)values(?,?,?,?)''',(Mname11,name1,"0",Mmrp11))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully Added')

    def check():
        Mid11=Mid1.get()
        if(Mid11==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Mid11))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        Mname11=Mname1.get()
        if(Mname11==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', Mname11))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
        
        Mmrp11=Mmrp1.get()
        if(Mmrp11==""):
            tkinter.messagebox.showerror('Error !!','MRP Cannot be Empty')
        else:
            c=bool(re.search(r'\d', Mmrp11))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in MRP')

        try:        
            if(a==True and b==False and c==True):
                adde()
        except:
            print("Error")
            
    def upe():  #UPDATING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        cur.execute('''Update Raw_Material SET Menu_name=?,Menu_MRP=?
                where Menu_id=?''',(Mname11,Mmrp11,Mid11,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully updated')

    def checku():
        Mid11=Mid1.get()
        if(Mid11==""):
            tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
        else:
            a=bool(re.search(r'\d', Mid11))
            if(a==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                
        Mname11=Mname1.get()
        if(Mname11==""):
            tkinter.messagebox.showerror('Error !!','Name Cannot be Empty')
        else:
            b=bool(re.search(r'\d', Mname11))
            if(b==True):
                tkinter.messagebox.showerror('Error !!',' Numbers Not Allowed In Name')
        
        Mmrp11=Mmrp1.get()
        if(Mmrp11==""):
            tkinter.messagebox.showerror('Error !!','MRP Cannot be Empty')
        else:
            c=bool(re.search(r'\d', Mmrp11))
            if(c==False):
                tkinter.messagebox.showerror('Error !!',' Numbers Only Accepted in MRP')

        try:        
            if(a==True and b==False and c==True):
                upe()
        except:
            print("Error")

    def ad():
        lambda:init(Emp)
        add_Emp=ttk.Button(mu_frame,text="ADD NEW",command=check).grid(row=6,column=0)
        up_Emp=ttk.Button(mu_frame,text="      ",command=checku,state='disabled').grid(row=6,column=1)

    def up():
        lambda:init(Emp)
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    up_Emp=ttk.Button(mu_frame,text="Update",command=checku).grid(row=6,column=1)
                    add_Emp=ttk.Button(mu_frame,text="                ",command=check,state='disabled').grid(row=6,column=0)
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')

    def dele():
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Mid1.set(p)
                    Mid11=Mid1.get()
                    cur.execute('''Delete from Supplier where ID=?''',(Mid11,))
                    con.commit()
                    tkinter.messagebox.showinfo('Congratulations !!','Supplier successfully Deleted')
                    show_data()
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')
        
    mu_frame=tk.Frame(main_frame)
    add1_Emp=ttk.Button(mu_frame,text="New Entry",command=ad).grid(row=0,column=0)
    up1_Emp=ttk.Button(mu_frame,text="Update Form",command=up).grid(row=0,column=1)
    
    lb = tk.Label(mu_frame,text="Raw Material Page",
                  font=('Bold',40)).grid(row=0,column=2,columnspan=5)#place(x=200,y=450)
    MU_ID=tk.Label(mu_frame,text="Material ID",font=('Bold',25),pady=15).grid(row=3,column=0)
    MU_Name=tk.Label(mu_frame,text="Name",font=('Bold',25)).grid(row=3,column=1)
    MU_QTY=tk.Label(mu_frame,text="Supplier Name",font=('Bold',25)).grid(row=3,column=2)
    MU_MRP=tk.Label(mu_frame,text="MRP",font=('Bold',25)).grid(row=3,column=3)

### Menu item 1
    MU_id1=tk.Entry(mu_frame,textvariable=Mid1,font=('Bold',15),state='readonly').grid(row=4,column=0)

    MU_name1=tk.Entry(mu_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    combo1 = ttk.Combobox(mu_frame,textvariable=name)
    data = retrieve_datas()
    try:
        combo1['values'] = [item[0] for item in data]
        combo1.set(" ")
        def on_combo_select(event):
            selected_item = combo1.get()
    
        combo1.bind("<<ComboboxSelected>>", on_combo_select)
        combo1.grid(row=4,column=2)
    except:
        print('error')

    #MU_qty1=tk.Entry(mu_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)

    MU_mrp1=tk.Entry(mu_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)
    del_Emp=ttk.Button(mu_frame,text="Delete",
                      command=dele).grid(row=6,column=2)
    re_Emp=ttk.Button(mu_frame,text="show data",
                     command=show_data).grid(row=6,column=3)
    mu_frame.pack()

Ra()
'''
def fetch_ids(table_name):
    connection = sqlite3.connect("FFMS.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM {}".format(table_name))
    ids = cursor.fetchall()

    connection.close()
    return ids
d= fetch_ids('Customer')
print(d)
'''

def retrieve_data():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Id FROM Customer")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_data1():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Name FROM Customer")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_dataMI():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Menu_id FROM Menu")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_dataMN():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Menu_name FROM Menu")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_dataMP():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Menu_MRP FROM Menu")
    data = cursor.fetchall()
    connection.close()
    return data

def CusB():

    def prnt():

        Id1=Id.get()
        name1=name.get()
        date1=date.get()
        OBId1 = OBId.get()
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        Mid21 = Mid2.get()
        Mname21 = Mname2.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mtot21=Mtot2.get()
        Mid31 = Mid3.get()
        Mname31 = Mname3.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mtot31=Mtot3.get()
        Mid41 = Mid4.get()
        Mname41 = Mname4.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mtot41=Mtot4.get()
        Mid51 = Mid5.get()
        Mname51 = Mname5.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        Mtot51=Mtot5.get()
        Bamt1 = BAmt.get()
        
        # Create a PDF document
        pdf_doc = SimpleDocTemplate("CustomerBill.pdf", pagesize=letter)

        elements = []

        styles = getSampleStyleSheet()

        elements.append(Paragraph("Bill Report", styles['Title']))

        elements.append(Spacer(1, 12))
        #elements.append(Paragraph("This is a sample report generated using Python and ReportLab.", styles['Normal']))

        data = [[],
            ["Bill ID", OBId1 , "Bill Date",date1],
                ["Customer Id",Id1 , "Customer Name",name1],
                ["Menu Id","Menu Name","Qty","MRP","Total"],
                [Mid11,Mname11,Mqty11,Mmrp11,Mtot11],
                [Mid21,Mname21,Mqty21,Mmrp21,Mtot21],
                [Mid31,Mname31,Mqty31,Mmrp31,Mtot31],
                [Mid41,Mname41,Mqty41,Mmrp41,Mtot41],
                [Mid51,Mname51,Mqty51,Mmrp51,Mtot51],
                [' ',' '," ","Bill Amount",Bamt1],
                ["        THANK YOU"              ]]

        table = Table(data)
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                  ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                  ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                  ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(table)
        
        pdf_doc.build(elements)

        print("Report generated: report.pdf")
    
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Customer_Bill(date text,
        Bill_id INTEGER PRIMARY KEY AUTOINCREMENT,Customer_ID text,Customer_Name text,Menu_id text,Menu_name text,
        Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,Menu_name2 text,
        Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,Menu_id3 text,Menu_name3 text,
        Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,Menu_id4 text,Menu_name4 text,
        Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,Menu_id5 text,Menu_name5 text,
        Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text,Bill_AMT int)''')

    def total():
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        
        try:
            mt1=int(Mqty11)*int(Mmrp11)
            Mtot1.set(mt1)
        except:
            mt1=0
        try:
            mt2=int(Mqty21)*int(Mmrp21)
            Mtot2.set(mt2)
        except:
            mt2=0
        try:
            mt3=int(Mqty31)*int(Mmrp31)
            Mtot3.set(mt3)
        except:
            mt3=0
        try:
            mt4=int(Mqty41)*int(Mmrp41)
            Mtot4.set(mt4)
        except:
            mt4=0
        try:
            mt5=int(Mqty51)*int(Mmrp51)
            Mtot5.set(mt5)
        except:
            mt5=0
        
        global BT
        BT=mt1+mt2+mt3+mt4+mt5
        BAmt.set(BT)
        
    def BillAmt():
        total()

        
    def show_data():
        print("RECORDS")
        cur.execute('''select * from Customer_Bill''')
        for record in cur:
            print('Order ID :',str(record[1])+'\n')
            print('Date:',str(record[0])+'\n')
            print('ID :',str(record[2])+'\n')
            print('Name:',str(record[3])+'\n')
            print('Menu_id:',str(record[4])+'\n')
            print('Menu_name:',str(record[5])+'\n')
            print('Menu_Qty:',str(record[6])+'\n')
            print('Menu_MRP:',str(record[7]+'\n'))
            print('Menu_Total:',str(record[8]+'\n'))
            print('Menu_id2:',str(record[9])+'\n')
            print('Menu_name2:',str(record[10])+'\n')
            print('Menu_Qty2:',str(record[11])+'\n')
            print('Menu_MRP2:',str(record[12]+'\n'))
            print('Menu_Total2:',str(record[13]+'\n'))
            print('Menu_id3:',str(record[14])+'\n')
            print('Menu_name3:',str(record[15])+'\n')
            print('Menu_Qty3:',str(record[16])+'\n')
            print('Menu_MRP3:',str(record[17]+'\n'))
            print('Menu_Total3:',str(record[18]+'\n'))
            print('Menu_id4:',str(record[19])+'\n')
            print('Menu_name4:',str(record[20])+'\n')
            print('Menu_Qty4:',str(record[21])+'\n')
            print('Menu_MRP4:',str(record[22]+'\n'))
            print('Menu_Total4:',str(record[23]+'\n'))
            print('Menu_id5:',str(record[24])+'\n')
            print('Menu_name5:',str(record[25])+'\n')
            print('Menu_Qty5:',str(record[26])+'\n')
            print('Menu_MRP5:',str(record[27]+'\n'))
            print('Menu_Total5:',str(record[28]+'\n'))

        #Id.set("")
        name.set("")
        date.set(x1)
        OBId.set("")
        Mid1.set("")
        Mname1.set("")
        Mqty1.set("")
        Mmrp1.set("")
        Mtot1.set("")
        Mid2.set("")
        Mname2.set("")
        Mqty2.set("")
        Mmrp2.set("")
        Mtot2.set("")
        Mid3.set("")
        Mname3.set("")
        Mqty3.set("")
        Mmrp3.set("")
        Mtot3.set("")
        Mid4.set("")
        Mname4.set("")
        Mqty4.set("")
        Mmrp4.set("")
        Mtot4.set("")
        Mid5.set("")
        Mname5.set("")
        Mqty5.set("")
        Mmrp5.set("")
        Mtot5.set("")
        BAmt.set("")

        try:
            a=str(record[1])
            a=int(a)+1
            OBId.set(a)
        except:
            OBId.set("1")
    show_data()

    def adde():        #ADDING DATA
        add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
        Id1=Id.get()
        name1=name.get()
        date1=date.get()
        OBId1 = OBId.get()
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        Mid21 = Mid2.get()
        Mname21 = Mname2.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mtot21=Mtot2.get()
        Mid31 = Mid3.get()
        Mname31 = Mname3.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mtot31=Mtot3.get()
        Mid41 = Mid4.get()
        Mname41 = Mname4.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mtot41=Mtot4.get()
        Mid51 = Mid5.get()
        Mname51 = Mname5.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        Mtot51=Mtot5.get()
        Bamt1 = BAmt.get()
        cur.execute('''Insert into Customer_Bill(date,Customer_ID,
            Customer_Name,Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
            ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
            Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
            Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
            Menu_MRP5,Menu_Total5,Bill_AMT)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1))

        def switchM11(value):
            if value == "Burger":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Bun"''',(Mqty11))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty11))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Burger Tikki"''',(Mqty11))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty11))
                return "Case Burger"
            elif value == "Pizza":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Pizza Base"''',(Mqty11))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty11))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty11))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Nuggets"''',(Mqty11))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty11))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty11))
                return "Case Nuggets"
            else:
                return "Default Case"
        if Mname11 != (" "):
            result = switchM11(Mname11)
            print(result)
    
        def switchM51(value):
            if value == "Burger":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Bun"''',(Mqty51))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty51))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Burger Tikki"''',(Mqty51))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty51))
                return "Case Burger"
            elif value == "Pizza":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Pizza Base"''',(Mqty51))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty51))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty51))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Nuggets"''',(Mqty51))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty51))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty51))
                return "Case Nuggets"
            else:
                return "Default Case"
        if Mname51 != (" "):
            result = switchM51(Mname51)
            print(result)

        def switchM21(value):
            if value == "Burger":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Bun"''',(Mqty21))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty21))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Burger Tikki"''',(Mqty21))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty21))
                return "Case Burger"
            elif value == "Pizza":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Pizza Base"''',(Mqty21))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty21))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty21))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Nuggets"''',(Mqty21))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty21))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty21))
                return "Case Nuggets"
            else:
                return "Default Case"
        if Mname21 != (" "):
            result = switchM21(Mname21)
            print(result)

        def switchM31(value):
            if value == "Burger":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Bun"''',(Mqty31))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty31))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Burger Tikki"''',(Mqty31))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty31))
                return "Case Burger"
            elif value == "Pizza":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Pizza Base"''',(Mqty31))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty31))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty31))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Nuggets"''',(Mqty31))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty31))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty31))
                return "Case Nuggets"
            else:
                return "Default Case"
        if Mname31 != (" "):
            result = switchM31(Mname31)
            print(result)

        def switchM41(value):
            if value == "Burger":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Bun"''',(Mqty41))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty41))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Burger Tikki"''',(Mqty41))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty41))
                return "Case Burger"
            elif value == "Pizza":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Pizza Base"''',(Mqty41))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty41))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty41))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Nuggets"''',(Mqty41))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "ketchup"''',(Mqty41))
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty-? where Menu_name = "Cheese"''',(Mqty41))
                return "Case Nuggets"
            else:
                return "Default Case"
        if Mname41 != (" "):
            result = switchM41(Mname41)
            print(result)
        
        con.commit()
        #show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Bill successfully Added')

            
    def upe():  #UPDATING DATA
        Id1=Id.get()
        name1=name.get()
        date1=date.get()
        OBId1 = OBId.get()
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        Mid21 = Mid2.get()
        Mname21 = Mname2.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mtot21=Mtot2.get()
        Mid31 = Mid3.get()
        Mname31 = Mname3.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mtot31=Mtot3.get()
        Mid41 = Mid4.get()
        Mname41 = Mname4.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mtot41=Mtot4.get()
        Mid51 = Mid5.get()
        Mname51 = Mname5.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        Mtot51=Mtot5.get()
        Bamt1 = BAmt.get()
        cur.execute('''Update Customer_Bill SET date=?,Customer_ID=?,Customer_Name=?,
            Menu_id=?,Menu_name=?,Menu_Qty=?,Menu_MRP=?,Menu_Total=?
            ,Menu_id2=?,Menu_name2=?,Menu_Qty2=?,Menu_MRP2=?,Menu_Total2=?,Menu_id3=?,
            Menu_name3=?,Menu_Qty3=?,Menu_MRP3=?,Menu_Total3=?,Menu_id4=?,Menu_name4=?,
            Menu_Qty4=?,Menu_MRP4=?,Menu_Total4=?,Menu_id5=?,Menu_name5=?,Menu_Qty5=?,
            Menu_MRP5=?,Menu_Total5=?,Bill_AMT=? where Bill_id=?''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1,OBId1,))
        con.commit()
        #show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Bill successfully updated')
        

    def chIN():
        
        cur.execute('''Select Menu_Qty from Raw_Material where Menu_name = "ketchup" ''')
        for n in cur:
            print(n)
            if(int(n[0])>0):
                pass
            else:
                add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
                tkinter.messagebox.showerror('','ketchup Not Available')
        cur.execute('''Select Menu_Qty from Raw_Material where Menu_name = "Cheese" ''')
        for n in cur:
            print(n)
            if(int(n[0])>0):
                pass
            else:
                add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
                tkinter.messagebox.showerror('','Cheese Not Available')

        def switchM11(value):
                        
            if value == "Burger":
                cur.execute('''Select Menu_Qty from Raw_Material where Menu_name = "Bun" ''')
                for n in cur:
                    print(n)
                    if(n[0]>0):
                        pass
                    else:
                        add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
                        tkinter.messagebox.showerror('','Buns Not Available')
                
                cur.execute('''Select Menu_Qty from Raw_Material where Menu_name = "Burger Tikki" ''')
                for n in cur:
                    print(n)
                    if(n[0]>0):
                        pass
                    else:
                        add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
                        tkinter.messagebox.showerror('','Burger Tikki Not Available')
                
                return "Case Burger"
            elif value == "Pizza":
                cur.execute('''Select Menu_Qty from Raw_Material where Menu_name = "Pizza Base" ''')
                for n in cur:
                    print(n)
                    if(n[0]>0):
                        pass
                    else:
                        add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
                        tkinter.messagebox.showerror('','Pizza Base Not Available')
                        
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Select Menu_Qty from Raw_Material where Menu_name = "Nuggets" ''')
                for n in cur:
                    print(n)
                    if(n[0]>0):
                        pass
                    else:
                        add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
                        tkinter.messagebox.showerror('','Nuggets Not Available')
                return "Case Nuggets"
            else:
                return "Default Case"


    def ad():
        add_Emp=ttk.Button(CusB_frame,text="ADD NEW",command=adde).grid(row=9,column=0)
        up_Emp=ttk.Button(CusB_frame,text="      ",command=upe,state='disabled').grid(row=9,column=1)
        chIN()

    def up():
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    up_Emp=ttk.Button(CusB_frame,text="Update",command=adde).grid(row=9,column=1)
                    add_Emp=ttk.Button(CusB_frame,text="               ",command=upe,state='disabled').grid(row=9,column=0)
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')
    
    def dele():
        OBId1 = OBId.get()
        cur.execute('''Delete from Customer_Bill where Bill_id=?''',(OBId1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Bill successfully Deleted')
        #show_data()

    CusB_frame=tk.Frame(main_frame)
    add1_Emp=ttk.Button(CusB_frame,text="New Entry",command=ad).grid(row=0,column=0)
    up1_Emp=ttk.Button(CusB_frame,text="Update Form",command=up).grid(row=0,column=1)
    
    lb = tk.Label(CusB_frame,text="Customer Bill Page",
                  font=('Bold',40)).grid(row=0,column=2,columnspan=6)
    
    CusB_ID=tk.Label(CusB_frame,text="Bill ID",font=('Bold',15)).grid(row=1,column=0)
    CusB_id=tk.Entry(CusB_frame,textvariable=OBId,font=('Bold',15),state='readonly').grid(row=1,column=1)
    
    CusB_Date=tk.Label(CusB_frame,text="Bill Date",font=('Bold',15)).grid(row=1,column=2)
    CusB_date=tk.Entry(CusB_frame,textvariable=date,font=('Bold',15)).grid(row=1,column=3)

    CusB_CID=tk.Label(CusB_frame,text="Customer ID",font=('Bold',15)).grid(row=2,column=0)
    
    combo = ttk.Combobox(CusB_frame,textvariable=Id)
    data = retrieve_data()
    try:
        combo['values'] = [item[0] for item in data]
        combo.set(" ")
        def on_combo_select(event):
            selected_item = combo.get()
            cur.execute('''select Name FROM Customer where Id=?''',selected_item)
            for record in cur:
                a=record[0]
            name.set(a)
    
        combo.bind("<<ComboboxSelected>>", on_combo_select)
        combo.grid(row=2,column=1)
    except:
        print('error')

    Cus_Name=tk.Label(CusB_frame,text="Customer Name",font=('Bold',15)).grid(row=2,column=2)

    combo1 = ttk.Combobox(CusB_frame,textvariable=name)
    data = retrieve_data1()
    try:
        combo1['values'] = [item[0] for item in data]
        combo1.set(" ")
        def on_combo_select(event):
            selected_item = combo1.get()
            cur.execute('''select Id FROM Customer where Name=?''',(selected_item,))
            for record in cur:
                a=record[0]
            Id.set(a)
    
        combo1.bind("<<ComboboxSelected>>", on_combo_select)
        combo1.grid(row=2,column=3)
    except:
        print('error')

    MU_ID=tk.Label(CusB_frame,text="Menu ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(CusB_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(CusB_frame,text="Quantity",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(CusB_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    
    MU_TOT=tk.Label(CusB_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

### Menu item 1
    #MU_id1=tk.Entry(CusB_frame,textvariable=Mid1,font=('Bold',15)).grid(row=4,column=0)
    comboMI1 = ttk.Combobox(CusB_frame,textvariable=Mid1)
    data = retrieve_dataMI()
    try:
        comboMI1['values'] = [item[0] for item in data]
        comboMI1.set(" ")
        def on_combo_select(event):
            selected_item = comboMI1.get()
            cur.execute('''select * FROM Menu where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[3]
            Mname1.set(a)
            Mmrp1.set(b)
    
        comboMI1.bind("<<ComboboxSelected>>", on_combo_select)
        comboMI1.grid(row=4,column=0)
    except:
        print('error')

    #MU_name1=tk.Entry(CusB_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)
    comboMN1 = ttk.Combobox(CusB_frame,textvariable=Mname1)
    data = retrieve_dataMN()
    try:
        comboMN1['values'] = [item[0] for item in data]
        comboMN1.set(" ")
        def on_combo_select(event):
            selected_item = comboMN1.get()
    
        comboMN1.bind("<<ComboboxSelected>>", on_combo_select)
        comboMN1.grid(row=4,column=1)
    except:
        print('error')

    comboMQ1 = ttk.Combobox(CusB_frame,textvariable=Mqty1)
    comboMQ1['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ1.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ1.get()

    comboMQ1.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ1.grid(row=4,column=2)
    
    comboMP1 = ttk.Combobox(CusB_frame,textvariable=Mmrp1)
    data = retrieve_dataMP()
    try:
        comboMP1['values'] = [item[0] for item in data]
        comboMP1.set(" ")
        def on_combo_select(event):
            selected_item = comboMP1.get()
    
        comboMP1.bind("<<ComboboxSelected>>", on_combo_select)
        comboMP1.grid(row=4,column=3)
    except:
        print('error')
    #MU_mrp1=tk.Entry(CusB_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)

    MU_tot1=tk.Entry(CusB_frame,textvariable=Mtot1,font=('Bold',15),state='readonly').grid(row=4,column=4)

### Menu item  2
    #MU_id2=tk.Entry(CusB_frame,textvariable=Mid2,font=('Bold',15)).grid(row=5,column=0)

    comboMI2 = ttk.Combobox(CusB_frame,textvariable=Mid2)
    data = retrieve_dataMI()
    try:
        comboMI2['values'] = [item[0] for item in data]
        comboMI2.set(" ")
        def on_combo_select(event):
            selected_item = comboMI2.get()
            cur.execute('''select * FROM Menu where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[3]
            Mname2.set(a)
            Mmrp2.set(b)
    
        comboMI2.bind("<<ComboboxSelected>>", on_combo_select)
        comboMI2.grid(row=5,column=0)
    except:
        print('error')

    comboMN2 = ttk.Combobox(CusB_frame,textvariable=Mname2)
    data = retrieve_dataMN()
    try:
        comboMN2['values'] = [item[0] for item in data]
        comboMN2.set(" ")
        def on_combo_select(event):
            selected_item = comboMN2.get()
    
        comboMN2.bind("<<ComboboxSelected>>", on_combo_select)
        comboMN2.grid(row=5,column=1)
    except:
        print('error')

    comboMQ2 = ttk.Combobox(CusB_frame,textvariable=Mqty2)
    comboMQ2['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ2.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ2.get()

    comboMQ2.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ2.grid(row=5,column=2)

    comboMP2 = ttk.Combobox(CusB_frame,textvariable=Mmrp2)
    data = retrieve_dataMP()
    try:
        comboMP2['values'] = [item[0] for item in data]
        comboMP2.set(" ")
        def on_combo_select(event):
            selected_item = comboMP2.get()
    
        comboMP2.bind("<<ComboboxSelected>>", on_combo_select)
        comboMP2.grid(row=5,column=3)
    except:
        print('error')

    MU_tot2=tk.Entry(CusB_frame,textvariable=Mtot2,font=('Bold',15),state='readonly').grid(row=5,column=4)


    ### Menu item 3

    comboMI3 = ttk.Combobox(CusB_frame,textvariable=Mid3)
    data = retrieve_dataMI()
    try:
        comboMI3['values'] = [item[0] for item in data]
        comboMI3.set(" ")
        def on_combo_select(event):
            selected_item = comboMI3.get()
            cur.execute('''select * FROM Menu where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[3]
            Mname3.set(a)
            Mmrp3.set(b)
    
        comboMI3.bind("<<ComboboxSelected>>", on_combo_select)
        comboMI3.grid(row=6,column=0)
    except:
        print('error')

    comboMN3 = ttk.Combobox(CusB_frame,textvariable=Mname3)
    data = retrieve_dataMN()
    try:
        comboMN3['values'] = [item[0] for item in data]
        comboMN3.set(" ")
        def on_combo_select(event):
            selected_item = comboMN3.get()
    
        comboMN3.bind("<<ComboboxSelected>>", on_combo_select)
        comboMN3.grid(row=6,column=1)
    except:
        print('error')

    comboMQ3 = ttk.Combobox(CusB_frame,textvariable=Mqty3)
    comboMQ3['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ3.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ3.get()

    comboMQ3.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ3.grid(row=6,column=2)

    comboMP3 = ttk.Combobox(CusB_frame,textvariable=Mmrp3)
    data = retrieve_dataMP()
    try:
        comboMP3['values'] = [item[0] for item in data]
        comboMP3.set(" ")
        def on_combo_select(event):
            selected_item = comboMP3.get()
    
        comboMP3.bind("<<ComboboxSelected>>", on_combo_select)
        comboMP3.grid(row=6,column=3)
    except:
        print('error')

    MU_tot3=tk.Entry(CusB_frame,textvariable=Mtot3,font=('Bold',15),state='readonly').grid(row=6,column=4)

### Menu item 4

    comboMI4 = ttk.Combobox(CusB_frame,textvariable=Mid4)
    data = retrieve_dataMI()
    try:
        comboMI4['values'] = [item[0] for item in data]
        comboMI4.set(" ")
        def on_combo_select(event):
            selected_item = comboMI4.get()
            cur.execute('''select * FROM Menu where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[3]
            Mname4.set(a)
            Mmrp4.set(b)
    
        comboMI4.bind("<<ComboboxSelected>>", on_combo_select)
        comboMI4.grid(row=7,column=0)
    except:
        print('error')

    comboMN4 = ttk.Combobox(CusB_frame,textvariable=Mname4)
    data = retrieve_dataMN()
    try:
        comboMN4['values'] = [item[0] for item in data]
        comboMN4.set(" ")
        def on_combo_select(event):
            selected_item = comboMN4.get()
    
        comboMN4.bind("<<ComboboxSelected>>", on_combo_select)
        comboMN4.grid(row=7,column=1)
    except:
        print('error')
        
    comboMQ4 = ttk.Combobox(CusB_frame,textvariable=Mqty4)
    comboMQ4['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ4.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ4.get()

    comboMQ4.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ4.grid(row=7,column=2)

    comboMP4 = ttk.Combobox(CusB_frame,textvariable=Mmrp4)
    data = retrieve_dataMP()
    try:
        comboMP4['values'] = [item[0] for item in data]
        comboMP4.set(" ")
        def on_combo_select(event):
            selected_item = comboMP4.get()
    
        comboMP4.bind("<<ComboboxSelected>>", on_combo_select)
        comboMP4.grid(row=7,column=3)
    except:
        print('error')
    MU_tot4=tk.Entry(CusB_frame,textvariable=Mtot4,font=('Bold',15),state='readonly').grid(row=7,column=4)

### Menu item 5
    comboMI5 = ttk.Combobox(CusB_frame,textvariable=Mid5)
    data = retrieve_dataMI()
    try:
        comboMI5['values'] = [item[0] for item in data]
        comboMI5.set(" ")
        def on_combo_select(event):
            selected_item = comboMI5.get()
            cur.execute('''select * FROM Menu where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[3]
            Mname5.set(a)
            Mmrp5.set(b)
    
        comboMI5.bind("<<ComboboxSelected>>", on_combo_select)
        comboMI5.grid(row=8,column=0)
    except:
        print('error')

    comboMN5 = ttk.Combobox(CusB_frame,textvariable=Mname5)
    data = retrieve_dataMN()
    try:
        comboMN5['values'] = [item[0] for item in data]
        comboMN5.set(" ")
        def on_combo_select(event):
            selected_item = comboMN5.get()
    
        comboMN5.bind("<<ComboboxSelected>>", on_combo_select)
        comboMN5.grid(row=8,column=1)
    except:
        print('error')

    comboMQ5 = ttk.Combobox(CusB_frame,textvariable=Mqty5)
    comboMQ5['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ5.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ5.get()

    comboMQ5.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ5.grid(row=8,column=2)

    comboMP5 = ttk.Combobox(CusB_frame,textvariable=Mmrp5)
    data = retrieve_dataMP()
    try:
        comboMP5['values'] = [item[0] for item in data]
        comboMP5.set(" ")
        def on_combo_select(event):
            selected_item = comboMP5.get()
    
        comboMP5.bind("<<ComboboxSelected>>", on_combo_select)
        comboMP5.grid(row=8,column=3)
    except:
        print('error')

    MU_tot5=tk.Entry(CusB_frame,textvariable=Mtot5,font=('Bold',15),state='readonly').grid(row=8,column=4)

    Bamt=ttk.Button(CusB_frame,text="Bill Amount",command=BillAmt).grid(row=10,column=3)
    bamt_tot5=tk.Entry(CusB_frame,textvariable=BAmt,font=('Bold',15),state='readonly').grid(row=10,column=4)
    re_Emp=ttk.Button(CusB_frame,text="Clear",command=show_data).grid(row=9,column=3)
    prnt=ttk.Button(CusB_frame,text="Print",command=prnt).grid(row=9,column=4)
    CusB_frame.pack()


def retrieve_data2():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Id FROM Supplier")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_data3():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Name FROM Supplier")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_dataRI():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Menu_id FROM Raw_Material")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_dataRN():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Menu_name FROM Raw_Material")
    data = cursor.fetchall()
    connection.close()
    return data

def retrieve_dataRP():
    connection = sqlite3.connect('FFMS.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Menu_MRP FROM Raw_Material")
    data = cursor.fetchall()
    connection.close()
    return data

def SupB():
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Supplier_Bill(date text,
        Bill_id INTEGER PRIMARY KEY AUTOINCREMENT,Supplier_ID text,Supplier_Name text,Menu_id text,Menu_name text,
        Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,Menu_name2 text,
        Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,Menu_id3 text,Menu_name3 text,
        Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,Menu_id4 text,Menu_name4 text,
        Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,Menu_id5 text,Menu_name5 text,
        Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text,Bill_AMT int)''')

    
    def prnt():

        Id1=Id.get()
        name1=name.get()
        date1=date.get()
        OBId1 = OBId.get()
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        Mid21 = Mid2.get()
        Mname21 = Mname2.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mtot21=Mtot2.get()
        Mid31 = Mid3.get()
        Mname31 = Mname3.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mtot31=Mtot3.get()
        Mid41 = Mid4.get()
        Mname41 = Mname4.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mtot41=Mtot4.get()
        Mid51 = Mid5.get()
        Mname51 = Mname5.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        Mtot51=Mtot5.get()
        Bamt1 = BAmt.get()
        
        # Create a PDF document
        pdf_doc = SimpleDocTemplate("SupplierBill.pdf", pagesize=letter)

        elements = []

        styles = getSampleStyleSheet()

        elements.append(Paragraph("Bill Report", styles['Title']))

        elements.append(Spacer(1, 12))
        #elements.append(Paragraph("This is a sample report generated using Python and ReportLab.", styles['Normal']))

        data = [[],
            ["Bill ID", OBId1 , "Bill Date",date1],
                ["Supplier Id",Id1 , "Supplier Name",name1],
                ["Menu Id","Menu Name","Qty","MRP","Total"],
                [Mid11,Mname11,Mqty11,Mmrp11,Mtot11],
                [Mid21,Mname21,Mqty21,Mmrp21,Mtot21],
                [Mid31,Mname31,Mqty31,Mmrp31,Mtot31],
                [Mid41,Mname41,Mqty41,Mmrp41,Mtot41],
                [Mid51,Mname51,Mqty51,Mmrp51,Mtot51],
                [' ',' '," ","Bill Amount",Bamt1],
                ["        THANK YOU"              ]]

        table = Table(data)
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                  ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                  ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                  ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(table)
        
        pdf_doc.build(elements)

        print("Report generated: report.pdf")

    def total():
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        
        try:
            mt1=int(Mqty11)*int(Mmrp11)
            Mtot1.set(mt1)
        except:
            mt1=0
        try:
            mt2=int(Mqty21)*int(Mmrp21)
            Mtot2.set(mt2)
        except:
            mt2=0
        try:
            mt3=int(Mqty31)*int(Mmrp31)
            Mtot3.set(mt3)
        except:
            mt3=0
        try:
            mt4=int(Mqty41)*int(Mmrp41)
            Mtot4.set(mt4)
        except:
            mt4=0
        try:
            mt5=int(Mqty51)*int(Mmrp51)
            Mtot5.set(mt5)
        except:
            mt5=0
        
        global BT
        BT=mt1+mt2+mt3+mt4+mt5
        BAmt.set(BT)
        
    def BillAmt():
        total()

        
    def show_data():
        print("RECORDS")
        cur.execute('''select * from Supplier_Bill''')
        for record in cur:
            print('Order ID :',str(record[1])+'\n')
            print('Date:',str(record[0])+'\n')
            print('ID :',str(record[2])+'\n')
            print('Name:',str(record[3])+'\n')
            print('Menu_id:',str(record[4])+'\n')
            print('Menu_name:',str(record[5])+'\n')
            print('Menu_Qty:',str(record[6])+'\n')
            print('Menu_MRP:',str(record[7]+'\n'))
            print('Menu_Total:',str(record[8]+'\n'))
            print('Menu_id2:',str(record[9])+'\n')
            print('Menu_name2:',str(record[10])+'\n')
            print('Menu_Qty2:',str(record[11])+'\n')
            print('Menu_MRP2:',str(record[12]+'\n'))
            print('Menu_Total2:',str(record[13]+'\n'))
            print('Menu_id3:',str(record[14])+'\n')
            print('Menu_name3:',str(record[15])+'\n')
            print('Menu_Qty3:',str(record[16])+'\n')
            print('Menu_MRP3:',str(record[17]+'\n'))
            print('Menu_Total3:',str(record[18]+'\n'))
            print('Menu_id4:',str(record[19])+'\n')
            print('Menu_name4:',str(record[20])+'\n')
            print('Menu_Qty4:',str(record[21])+'\n')
            print('Menu_MRP4:',str(record[22]+'\n'))
            print('Menu_Total4:',str(record[23]+'\n'))
            print('Menu_id5:',str(record[24])+'\n')
            print('Menu_name5:',str(record[25])+'\n')
            print('Menu_Qty5:',str(record[26])+'\n')
            print('Menu_MRP5:',str(record[27]+'\n'))
            print('Menu_Total5:',str(record[28]+'\n'))

        #Id.set("")
        name.set("")
        date.set(x1)
        OBId.set("")
        Mid1.set("")
        Mname1.set("")
        Mqty1.set("")
        Mmrp1.set("")
        Mtot1.set("")
        Mid2.set("")
        Mname2.set("")
        Mqty2.set("")
        Mmrp2.set("")
        Mtot2.set("")
        Mid3.set("")
        Mname3.set("")
        Mqty3.set("")
        Mmrp3.set("")
        Mtot3.set("")
        Mid4.set("")
        Mname4.set("")
        Mqty4.set("")
        Mmrp4.set("")
        Mtot4.set("")
        Mid5.set("")
        Mname5.set("")
        Mqty5.set("")
        Mmrp5.set("")
        Mtot5.set("")
        BAmt.set("")

        try:
            a=str(record[1])
            a=int(a)+1
            OBId.set(a)
        except:
            OBId.set("1")
    show_data()

    def adde():        #ADDING DATA
        Id1=Id.get()
        name1=name.get()
        date1=date.get()
        OBId1 = OBId.get()
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        Mid21 = Mid2.get()
        Mname21 = Mname2.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mtot21=Mtot2.get()
        Mid31 = Mid3.get()
        Mname31 = Mname3.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mtot31=Mtot3.get()
        Mid41 = Mid4.get()
        Mname41 = Mname4.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mtot41=Mtot4.get()
        Mid51 = Mid5.get()
        Mname51 = Mname5.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        Mtot51=Mtot5.get()
        Bamt1=BAmt.get()
        cur.execute('''Insert into Supplier_Bill(date,Supplier_ID,
            Supplier_Name,Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
            ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
            Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
            Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
            Menu_MRP5,Menu_Total5,Bill_AMT)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1))
        
        def switchM11(value):
            if value == "Bun":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Bun"''',(Mqty11))
                return "Case Bun"
            elif value == "Pizza Base":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Pizza Base"''',(Mqty11))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Nuggets"''',(Mqty11))
                return "Case Nuggets"
            elif value == "Cheese":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Cheese"''',(Mqty11))
                return "Case Cheese"
            elif value == "ketchup":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "ketchup"''',(Mqty11))
                return "Case ketchup"
            elif value == "Burger Tikki":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Burger Tikki"''',(Mqty11))
                return "Case Burger Tikki"
            else:
                return "Default Case"
        if Mname11 != (" "):
            result = switchM11(Mname11)
            print(result)

        def switchM21(value):
            if value == "Bun":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Bun"''',(Mqty21))
                return "Case Bun"
            elif value == "Pizza Base":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Pizza"''',(Mqty21))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Nuggets"''',(Mqty21))
                return "Case Nuggets"
            elif value == "Cheese":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Cheese"''',(Mqty21))
                return "Case Cheese"
            elif value == "ketchup":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "ketchup"''',(Mqty21))
                return "Case ketchup"
            elif value == "Burger Tikki":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Burger Tikki"''',(Mqty21))
                return "Case Burger Tikki"
            else:
                return "Default Case"
        if Mname21 != (" "):
            result = switchM21(Mname21)
            print(result)
        
        def switchM31(value):
            if value == "Bun":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Bun"''',(Mqty31))
                return "Case Bun"
            elif value == "Pizza Base":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Pizza"''',(Mqty31))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Nuggets"''',(Mqty31))
                return "Case Nuggets"
            elif value == "Cheese":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Cheese"''',(Mqty31))
                return "Case Cheese"
            elif value == "ketchup":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "ketchup"''',(Mqty31))
                return "Case ketchup"
            elif value == "Burger Tikki":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Burger Tikki"''',(Mqty31))
                return "Case Burger Tikki"
            else:
                return "Default Case"
        if Mname31 != (" "):
            result = switchM31(Mname31)
            print(result)

        def switchM41(value):
            if value == "Bun":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Bun"''',(Mqty41))
                return "Case Bun"
            elif value == "Pizza Base":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Pizza"''',(Mqty41))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Nuggets"''',(Mqty41))
                return "Case Nuggets"
            elif value == "Cheese":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Cheese"''',(Mqty41))
                return "Case Cheese"
            elif value == "ketchup":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "ketchup"''',(Mqty41))
                return "Case ketchup"
            elif value == "Burger Tikki":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Burger Tikki"''',(Mqty41))
                return "Case Burger Tikki"
            else:
                return "Default Case"
        if Mname41 != (" "):
            result = switchM41(Mname41)
            print(result)

        def switchM51(value):
            if value == "Bun":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Bun"''',(Mqty51))
                return "Case Bun"
            elif value == "Pizza Base":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Pizza"''',(Mqty51))
                return "Case pizza"
            elif value == "Nuggets":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Nuggets"''',(Mqty51))
                return "Case Nuggets"
            elif value == "Cheese":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Cheese"''',(Mqty51))
                return "Case Cheese"
            elif value == "ketchup":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "ketchup"''',(Mqty51))
                return "Case ketchup"
            elif value == "Burger Tikki":
                cur.execute('''Update Raw_Material set Menu_Qty = Menu_Qty+? where Menu_name = "Burger Tikki"''',(Mqty51))
                return "Case Burger Tikki"
            else:
                return "Default Case"
        if Mname51 != (" "):
            result = switchM51(Mname51)
            print(result)

        
        con.commit()
        #show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Bill successfully Added')
            
    def upe():  #UPDATING DATA
        Id1=Id.get()
        name1=name.get()
        date1=date.get()
        OBId1 = OBId.get()
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        Mid21 = Mid2.get()
        Mname21 = Mname2.get()
        Mqty21 = Mqty2.get()
        Mmrp21 = Mmrp2.get()
        Mtot21=Mtot2.get()
        Mid31 = Mid3.get()
        Mname31 = Mname3.get()
        Mqty31 = Mqty3.get()
        Mmrp31 = Mmrp3.get()
        Mtot31=Mtot3.get()
        Mid41 = Mid4.get()
        Mname41 = Mname4.get()
        Mqty41 = Mqty4.get()
        Mmrp41 = Mmrp4.get()
        Mtot41=Mtot4.get()
        Mid51 = Mid5.get()
        Mname51 = Mname5.get()
        Mqty51 = Mqty5.get()
        Mmrp51 = Mmrp5.get()
        Mtot51=Mtot5.get()
        Bamt1=BAmt.get()
        cur.execute('''Update Supplier_Bill SET date=?,Supplier_ID=?,Supplier_Name=?,
            Menu_id=?,Menu_name=?,Menu_Qty=?,Menu_MRP=?,Menu_Total=?
            ,Menu_id2=?,Menu_name2=?,Menu_Qty2=?,Menu_MRP2=?,Menu_Total2=?,Menu_id3=?,
            Menu_name3=?,Menu_Qty3=?,Menu_MRP3=?,Menu_Total3=?,Menu_id4=?,Menu_name4=?,
            Menu_Qty4=?,Menu_MRP4=?,Menu_Total4=?,Menu_id5=?,Menu_name5=?,Menu_Qty5=?,
            Menu_MRP5=?,Menu_Total5=?,Bill_AMT=? where Bill_id=?''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1,OBId1,))
        con.commit()
        #show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Bill successfully updated')

    def ad():
        lambda:init(Emp)
        add_Emp=ttk.Button(SupB_frame,text="ADD NEW",command=adde).grid(row=9,column=0)
        up_Emp=ttk.Button(SupB_frame,text="      ",command=upe,state='disabled').grid(row=9,column=1)

    def up():
        lambda:init(Emp)
        try:
            p=tkinter.simpledialog.askstring("Verification","Enter ID")
            if(p==""):
                tkinter.messagebox.showerror('Error !!','Id Cannot be Empty')
            else:
                a=bool(re.search(r'\d', p))
                if(a==False):
                    tkinter.messagebox.showerror('Error !!',' Numbers Only in ID')
                else:
                    Id.set(p)
                    up_Emp=ttk.Button(SupB_frame,text="Update",command=adde).grid(row=9,column=1)
                    add_Emp=ttk.Button(SupB_frame,text="             ",command=upe,state='disabled').grid(row=9,column=0)
        except:
            tkinter.messagebox.showerror('Error !!','Please Enter a Number')

    def dele():
        OBId1 = OBId.get()
        cur.execute('''Delete from Supplier_Bill where Bill_id=?''',(OBId1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Bill successfully Deleted')
        #show_data()

    SupB_frame=tk.Frame(main_frame)
    add1_Emp=ttk.Button(SupB_frame,text="New Entry",command=ad).grid(row=0,column=0)
    up1_Emp=ttk.Button(SupB_frame,text="Update Form",command=up).grid(row=0,column=1)
    lb = tk.Label(SupB_frame,text="Supplier Bill Page",
                  font=('Bold',40)).grid(row=0,column=2,columnspan=6)#place(x=200,y=450)
    SupB_ID=tk.Label(SupB_frame,text="Bill ID",font=('Bold',15)).grid(row=1,column=0)
    SupB_id=tk.Entry(SupB_frame,textvariable=OBId,font=('Bold',15),state='readonly').grid(row=1,column=1)
    
    SupB_Date=tk.Label(SupB_frame,text="Bill Date",font=('Bold',15)).grid(row=1,column=2)
    SupB_date=tk.Entry(SupB_frame,textvariable=date,font=('Bold',15)).grid(row=1,column=3)

    SupB_CID=tk.Label(SupB_frame,text="Supplier ID",font=('Bold',15)).grid(row=2,column=0)
    
    combo = ttk.Combobox(SupB_frame,textvariable=Id)
    data = retrieve_data2()
    try:
        combo['values'] = [item[0] for item in data]
        combo.set(" ")
        def on_combo_select(event):
            selected_item = combo.get()
            cur.execute('''select Name FROM Supplier where Id=?''',selected_item)
            for record in cur:
                a=record[0]
            name.set(a)
    
        combo.bind("<<ComboboxSelected>>", on_combo_select)
        combo.grid(row=2,column=1)
    except:
        print('error')

    Sup_Name=tk.Label(SupB_frame,text="Supplier Name",font=('Bold',15)).grid(row=2,column=2)

    combo1 = ttk.Combobox(SupB_frame,textvariable=name)
    data = retrieve_data3()
    try:
        combo1['values'] = [item[0] for item in data]
        combo1.set(" ")
        def on_combo_select(event):
            selected_item = combo1.get()
            cur.execute('''select Id FROM Supplier where Name=?''',(selected_item,))
            for record in cur:
                a=record[0]
            Id.set(a)
    
        combo1.bind("<<ComboboxSelected>>", on_combo_select)
        combo1.grid(row=2,column=3)
    except:
        print('error')

    MU_ID=tk.Label(SupB_frame,text="Menu ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(SupB_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(SupB_frame,text="Quantity",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(SupB_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    MU_TOT=tk.Label(SupB_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

### Menu item 1
    comboRI1 = ttk.Combobox(SupB_frame,textvariable=Mid1)
    data = retrieve_dataRI()
    try:
        comboRI1['values'] = [item[0] for item in data]
        comboRI1.set(" ")
        def on_combo_select(event):
            selected_item = comboRI1.get()
            cur.execute('''select * FROM Raw_Material where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[4]
            Mname1.set(a)
            Mmrp1.set(b)
    
        comboRI1.bind("<<ComboboxSelected>>", on_combo_select)
        comboRI1.grid(row=4,column=0)
    except:
        print('error')

    comboRN1 = ttk.Combobox(SupB_frame,textvariable=Mname1)
    data = retrieve_dataRN()
    try:
        comboRN1['values'] = [item[0] for item in data]
        comboRN1.set(" ")
        def on_combo_select(event):
            selected_item = comboRN1.get()
    
        comboRN1.bind("<<ComboboxSelected>>", on_combo_select)
        comboRN1.grid(row=4,column=1)
    except:
        print('error')

    comboMQ1 = ttk.Combobox(SupB_frame,textvariable=Mqty1)
    comboMQ1['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ1.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ1.get()

    comboMQ1.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ1.grid(row=4,column=2)

    comboRP1 = ttk.Combobox(SupB_frame,textvariable=Mmrp1)
    data = retrieve_dataRP()
    try:
        comboRP1['values'] = [item[0] for item in data]
        comboRP1.set(" ")
        def on_combo_select(event):
            selected_item = comboRP1.get()
    
        comboRP1.bind("<<ComboboxSelected>>", on_combo_select)
        comboRP1.grid(row=4,column=3)
    except:
        print('error')

    MU_tot1=tk.Entry(SupB_frame,textvariable=Mtot1,font=('Bold',15),state='readonly').grid(row=4,column=4)

### Menu item  2

    comboRI2 = ttk.Combobox(SupB_frame,textvariable=Mid2)
    data = retrieve_dataRI()
    try:
        comboRI2['values'] = [item[0] for item in data]
        comboRI2.set(" ")
        def on_combo_select(event):
            selected_item = comboRI2.get()
            cur.execute('''select * FROM Raw_Material where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[4]
            Mname2.set(a)
            Mmrp2.set(b)
    
        comboRI2.bind("<<ComboboxSelected>>", on_combo_select)
        comboRI2.grid(row=5,column=0)
    except:
        print('error')

    comboRN2 = ttk.Combobox(SupB_frame,textvariable=Mname2)
    data = retrieve_dataRN()
    try:
        comboRN2['values'] = [item[0] for item in data]
        comboRN2.set(" ")
        def on_combo_select(event):
            selected_item = comboRN2.get()
    
        comboRN2.bind("<<ComboboxSelected>>", on_combo_select)
        comboRN2.grid(row=5,column=1)
    except:
        print('error')

    comboMQ2 = ttk.Combobox(SupB_frame,textvariable=Mqty2)
    comboMQ2['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ2.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ2.get()

    comboMQ2.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ2.grid(row=5,column=2)

    comboRP2 = ttk.Combobox(SupB_frame,textvariable=Mmrp2)
    data = retrieve_dataRP()
    try:
        comboRP2['values'] = [item[0] for item in data]
        comboRP2.set(" ")
        def on_combo_select(event):
            selected_item = comboRP2.get()
    
        comboRP2.bind("<<ComboboxSelected>>", on_combo_select)
        comboRP2.grid(row=5,column=3)
    except:
        print('error')
        
    MU_tot2=tk.Entry(SupB_frame,textvariable=Mtot2,font=('Bold',15),state='readonly').grid(row=5,column=4)

    ### Menu item 3

    comboRI3 = ttk.Combobox(SupB_frame,textvariable=Mid3)
    data = retrieve_dataRI()
    try:
        comboRI3['values'] = [item[0] for item in data]
        comboRI3.set(" ")
        def on_combo_select(event):
            selected_item = comboRI3.get()
            cur.execute('''select * FROM Raw_Material where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[4]
            Mname3.set(a)
            Mmrp3.set(b)
    
        comboRI3.bind("<<ComboboxSelected>>", on_combo_select)
        comboRI3.grid(row=6,column=0)
    except:
        print('error')

    comboRN3 = ttk.Combobox(SupB_frame,textvariable=Mname3)
    data = retrieve_dataRN()
    try:
        comboRN3['values'] = [item[0] for item in data]
        comboRN3.set(" ")
        def on_combo_select(event):
            selected_item = comboRN3.get()
    
        comboRN3.bind("<<ComboboxSelected>>", on_combo_select)
        comboRN3.grid(row=6,column=1)
    except:
        print('error')

    comboMQ3 = ttk.Combobox(SupB_frame,textvariable=Mqty3)
    comboMQ3['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ3.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ3.get()

    comboMQ3.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ3.grid(row=6,column=2)

    comboRP3 = ttk.Combobox(SupB_frame,textvariable=Mmrp3)
    data = retrieve_dataRP()
    try:
        comboRP3['values'] = [item[0] for item in data]
        comboRP3.set(" ")
        def on_combo_select(event):
            selected_item = comboRP3.get()
    
        comboRP3.bind("<<ComboboxSelected>>", on_combo_select)
        comboRP3.grid(row=6,column=3)
    except:
        print('error')
    MU_tot=tk.Entry(SupB_frame,textvariable=Mtot3,font=('Bold',15),state='readonly').grid(row=6,column=4)

### Menu item 4

    comboRI4 = ttk.Combobox(SupB_frame,textvariable=Mid4)
    data = retrieve_dataRI()
    try:
        comboRI4['values'] = [item[0] for item in data]
        comboRI4.set(" ")
        def on_combo_select(event):
            selected_item = comboRI4.get()
            cur.execute('''select * FROM Raw_Material where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[4]
            Mname4.set(a)
            Mmrp4.set(b)
    
        comboRI4.bind("<<ComboboxSelected>>", on_combo_select)
        comboRI4.grid(row=7,column=0)
    except:
        print('error')

    comboRN4 = ttk.Combobox(SupB_frame,textvariable=Mname4)
    data = retrieve_dataRN()
    try:
        comboRN4['values'] = [item[0] for item in data]
        comboRN4.set(" ")
        def on_combo_select(event):
            selected_item = comboRN4.get()
    
        comboRN4.bind("<<ComboboxSelected>>", on_combo_select)
        comboRN4.grid(row=7,column=1)
    except:
        print('error')

    comboMQ4 = ttk.Combobox(SupB_frame,textvariable=Mqty4)
    comboMQ4['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ4.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ4.get()

    comboMQ4.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ4.grid(row=7,column=2)

    comboRP4 = ttk.Combobox(SupB_frame,textvariable=Mmrp4)
    data = retrieve_dataRP()
    try:
        comboRP4['values'] = [item[0] for item in data]
        comboRP4.set(" ")
        def on_combo_select(event):
            selected_item = comboRP4.get()
    
        comboRP4.bind("<<ComboboxSelected>>", on_combo_select)
        comboRP4.grid(row=7,column=3)
    except:
        print('error')
        
    MU_tot4=tk.Entry(SupB_frame,textvariable=Mtot4,font=('Bold',15),state='readonly').grid(row=7,column=4)

### Menu item 5

    comboRI5 = ttk.Combobox(SupB_frame,textvariable=Mid5)
    data = retrieve_dataRI()
    try:
        comboRI5['values'] = [item[0] for item in data]
        comboRI5.set(" ")
        def on_combo_select(event):
            selected_item = comboRI5.get()
            cur.execute('''select * FROM Raw_Material where Menu_id=?''',selected_item)
            for record in cur:
                a=record[1]
                b=record[4]
            Mname5.set(a)
            Mmrp5.set(b)
    
        comboRI5.bind("<<ComboboxSelected>>", on_combo_select)
        comboRI5.grid(row=8,column=0)
    except:
        print('error')

    comboRN5 = ttk.Combobox(SupB_frame,textvariable=Mname5)
    data = retrieve_dataRN()
    try:
        comboRN5['values'] = [item[0] for item in data]
        comboRN5.set(" ")
        def on_combo_select(event):
            selected_item = comboRN1.get()
    
        comboRN5.bind("<<ComboboxSelected>>", on_combo_select)
        comboRN5.grid(row=8,column=1)
    except:
        print('error')
        
    comboMQ5 = ttk.Combobox(SupB_frame,textvariable=Mqty5)
    comboMQ5['values'] = [1,2,3,4,5,6,7,8,9]
    comboMQ5.set(" ")
    def on_combo_select(event):
        selected_item = comboMQ5.get()

    comboMQ5.bind("<<ComboboxSelected>>", on_combo_select)
    comboMQ5.grid(row=8,column=2)

    comboRP5 = ttk.Combobox(SupB_frame,textvariable=Mmrp5)
    data = retrieve_dataRP()
    try:
        comboRP5['values'] = [item[0] for item in data]
        comboRP5.set(" ")
        def on_combo_select(event):
            selected_item = comboRP5.get()
    
        comboRP5.bind("<<ComboboxSelected>>", on_combo_select)
        comboRP5.grid(row=8,column=3)
    except:
        print('error')
    MU_tot5=tk.Entry(SupB_frame,textvariable=Mtot5,font=('Bold',15),state='readonly').grid(row=8,column=4)

    Bamt=ttk.Button(SupB_frame,text="Bill Amount",command=BillAmt).grid(row=10,column=3)
    bamt_tot5=tk.Entry(SupB_frame,textvariable=BAmt,font=('Bold',15),state='readonly').grid(row=10,column=4)
    re_Emp=ttk.Button(SupB_frame,text="clear").grid(row=9,column=3)
    prnt=ttk.Button(SupB_frame,text="Print",command=prnt).grid(row=9,column=4)
    SupB_frame.pack()    
root.mainloop()
