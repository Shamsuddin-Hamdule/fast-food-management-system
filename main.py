import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import webbrowser
from PIL import Image, ImageTk


root = tk.Tk()
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

Admin_btn = tk.Button(options_frame,text='Admin',font=('Bold',15),border=4,
                     fg='#1500ff',bd=3,command=lambda: init(Admin)).grid(row=0,column=0)#place(x=10,y=10)
Emp_btn = tk.Button(options_frame,text='Employee',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Emp)).grid(row=0,column=1)#place(x=90,y=10)
Cus_btn = tk.Button(options_frame,text='Customer',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Cus)).grid(row=0,column=2)#place(x=210,y=10)
Menu_btn = tk.Button(options_frame,text='Menu',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Mu)).grid(row=0,column=4)#place(x=410,y=10)
Sup_btn = tk.Button(options_frame,text='Supplier',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Sup)).grid(row=0,column=3)#place(x=320,y=10)
CusO_btn = tk.Button(options_frame,text='Customer_Order',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(CusO)).grid(row=0,column=5)#place(x=480,y=10)
SupO_btn = tk.Button(options_frame,text='Supplier_Order',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(SupO)).grid(row=0,column=6)#place(x=655,y=10)
CusB_btn = tk.Button(options_frame,text='Customer_Bill',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(CusB)).grid(row=0,column=7)#place(x=810,y=10)
SupB_btn = tk.Button(options_frame,text='Supplier_Bill',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(SupB)).grid(row=0,column=8)#place(x=960,y=10)
Stock_btn = tk.Button(options_frame,text='Stock',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Stock)).grid(row=0,column=9)#place(x=1100,y=10)
options_frame.pack()
options_frame.pack_propagate(False)
options_frame.configure(width=1200,height=100)

main_frame = tk.Frame(root,highlightbackground="black"
                      ,highlightthickness=2)
image_path = "fastfood.jfif"  # Replace this with your image file path
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
image_label = tk.Label(main_frame, image=photo)
image_label.pack(pady=100)

main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(height=700,width=1200)
    
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
Bamt = StringVar()

def Admin():
    Admin_frame=tk.Frame(main_frame)
    lb = tk.Label(Admin_frame,text="Admin Page",
                  font=('Bold',70)).pack()#place(x=200,y=450)
    button = tk.Button(Admin_frame, text="Click me to open a link", command=open_link)
    button.pack(pady=20)
    
    Admin_frame.pack()
    
def Emp():   ### EMPLOYEE TABLE
    E_head=tk.Frame(main_frame)
    lb = tk.Label(E_head,text="Employee Page",
                  font=('Bold',40)).grid(row=0,columnspan=4)#place(x=200,y=450)
    E_head.pack()
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Employee(ID text,
        Name text,Email text, gender text,Date_Of_Joining text,
        Date_Of_Birth text,Phone text,Designation text,Address text)''')
    con.commit
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
            label = tk.Label(E_frame, text=f"{Id1}{name1}{email1}"
                             ,font=('Bold',40)).pack()
        con.commit()
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
        cur.execute('''Insert into Employee(ID,Name,Email,gender,
            Date_Of_Joining,Date_Of_Birth,Phone,Designation,Address)
            values(?,?,?,?,?,?,?,?,?)''',(Id1,name1,email1,gen1,doj1,dob1,phone1,des1,add1))
        
        #con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Employee successfully Added')

            
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
        cur.execute('''Update Employee
                    SET Name=?,Email=?,gender=?, Date_Of_Joining=?,
                    Date_Of_Birth=?,Phone=?,Designation=?,Address=?
                    WHERE ID=?''',(name1,email1,gen1,doj1,dob1,phone1,des1,add1,Id1,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Employee successfully updated')

    def dele():
        Id1=Id.get()
        cur.execute('''Delete from Employee where ID=?''',(Id1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Employee successfully Deleted')
        show_data()
    Emp_frame=tk.Frame(main_frame)
    Emp_ID=tk.Label(Emp_frame,text="Employee ID",font=('Bold',15)).grid(row=1,column=0)
    Emp_id=tk.Entry(Emp_frame,textvariable=Id,font=('Bold',15)).grid(row=1,column=1)
    
    Emp_Name=tk.Label(Emp_frame,text="Employee Name",font=('Bold',15)).grid(row=1,column=2)
    Emp_name=tk.Entry(Emp_frame,textvariable=name,font=('Bold',15)).grid(row=1,column=3)
    
    Emp_Email=tk.Label(Emp_frame,text="Email Id",font=('Bold',15)).grid(row=2,column=0)
    Emp_email=tk.Entry(Emp_frame,textvariable=email,font=('Bold',15)).grid(row=2,column=1)
    
    Emp_Gen=tk.Label(Emp_frame,text="Gender",font=('Bold',15)).grid(row=2,column=2)
    Emp_gen=tk.Entry(Emp_frame,textvariable=gen,font=('Bold',15)).grid(row=2,column=3)
    
    EDOJ=tk.Label(Emp_frame,text="Date Of joining",font=('Bold',15)).grid(row=3,column=0)
    edoj=tk.Entry(Emp_frame,textvariable=doj,font=('Bold',15)).grid(row=3,column=1)
    
    EDOB=tk.Label(Emp_frame,text="Date Of Birth",font=('Bold',15)).grid(row=3,column=2)
    edob=tk.Entry(Emp_frame,textvariable=dob,font=('Bold',15)).grid(row=3,column=3)
    
    Ephone=tk.Label(Emp_frame,text="Phone no:",font=('Bold',15)).grid(row=4,column=0)
    ephone=tk.Entry(Emp_frame,textvariable=phone,font=('Bold',15)).grid(row=4,column=1)
    
    EDesignation=tk.Label(Emp_frame,text="Designation",font=('Bold',15)).grid(row=4,column=2)
    edes=tk.Entry(Emp_frame,textvariable=des,font=('Bold',15)).grid(row=4,column=3)
    
    Address=tk.Label(Emp_frame,text="Address",font=('Bold',15)).grid(row=5,column=0)
    Add=tk.Entry(Emp_frame,width=50,textvariable=add,font=('Bold',15)).grid(row=5,column=1,columnspan=3)
    add_Emp=tk.Button(Emp_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=6,column=0)
    up_Emp=tk.Button(Emp_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=6,column=1)
    del_Emp=tk.Button(Emp_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=6,column=2)
    re_Emp=tk.Button(Emp_frame,text="Show Data",font=('Bold',15),
                     command=show_data).grid(row=6,column=3)
    
##    # Create a Treeview widget to display the data
##    tree = ttk.Treeview(root)
##    tree['columns'] = tuple(range(len(data[0])))  # Define the number of columns
##
##    # Add columns to the Treeview
##    for i in range(len(data[0])):
##        tree.column('#' + str(i), anchor=tk.CENTER)
##        tree.heading('#' + str(i), text='Column ' + str(i))
##
##    # Insert data into the Treeview
##    for row in data:
##        tree.insert('', 'end', values=row)
##
##    # Pack the Treeview widget
##    tree.grid(row=7,column=0)
    Emp_frame.pack()


def Cus():   #Customer TABLE
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Customer(ID text,
        Name text,Email text, gender text,
        Date_Of_Birth text,Phone text,Address text)''')
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
    show_data()
    def adde():           #ADDING DATA
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        dob1=dob.get()
        phone1=phone.get()
        add1=add.get()
        
        cur.execute('''Insert into Customer(ID,Name,Email,gender,
            Date_Of_Birth,Phone,Address)values(?,?,?,?,?,?,?)''',(Id1,name1,email1,gen1,dob1,phone1,add1))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer successfully Added')

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

    def dele():
        Id1=Id.get()
        cur.execute('''Delete from Customer where ID=?''',(Id1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Customer successfully Deleted')
        show_data()
    
    Cus_frame=tk.Frame(main_frame)
    lb = tk.Label(Cus_frame,text="Customer Page",
                  font=('Bold',40)).grid(row=0,column=0,columnspan=4)#place(x=200,y=450)
    Cus_ID=tk.Label(Cus_frame,text="Customer ID",font=('Bold',15)).grid(row=1,column=0)
    Cus_id=tk.Entry(Cus_frame,textvariable=Id,font=('Bold',15)).grid(row=1,column=1)
    
    Cus_Name=tk.Label(Cus_frame,text="Customer Name",font=('Bold',15)).grid(row=1,column=2)
    Cus_name=tk.Entry(Cus_frame,textvariable=name,font=('Bold',15)).grid(row=1,column=3)
    
    Cus_Email=tk.Label(Cus_frame,text="Email Id",font=('Bold',15)).grid(row=2,column=0)
    Cus_email=tk.Entry(Cus_frame,textvariable=email,font=('Bold',15)).grid(row=2,column=1)
    
    Cus_Gen=tk.Label(Cus_frame,text="Gender",font=('Bold',15)).grid(row=2,column=2)
    Cus_gen=tk.Entry(Cus_frame,textvariable=gen,font=('Bold',15)).grid(row=2,column=3)
    
    CDOB=tk.Label(Cus_frame,text="Date Of Birth",font=('Bold',15)).grid(row=3,column=2)
    cdob=tk.Entry(Cus_frame,textvariable=dob,font=('Bold',15)).grid(row=3,column=3)
    
    Cphone=tk.Label(Cus_frame,text="Phone no:",font=('Bold',15)).grid(row=3,column=0)
    cphone=tk.Entry(Cus_frame,textvariable=phone,font=('Bold',15)).grid(row=3,column=1)
    
    Address=tk.Label(Cus_frame,text="Address",font=('Bold',15)).grid(row=5,column=0)
    Add=tk.Entry(Cus_frame,width=50,textvariable=add,font=('Bold',15)).grid(row=5,column=1,columnspan=3)
    add_Emp=tk.Button(Cus_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=6,column=0)
    up_Emp=tk.Button(Cus_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=6,column=1)
    del_Emp=tk.Button(Cus_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=6,column=2)
    re_Emp=tk.Button(Cus_frame,text="Show data",font=('Bold',15),
                     command=show_data).grid(row=6,column=3)
    
    Cus_frame.pack()
    
def Sup():   # SUPPLIER TABLE
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Supplier(ID text,
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
    show_data()
    
    def adde():     #ADDING DATA
        Id1=Id.get()
        name1=name.get()
        email1=email.get()
        gen1=gen.get()
        dob1=dob.get()
        phone1=phone.get()
        add1=add.get()
        cur.execute('''Insert into Supplier(ID,Name,Email,gender,
            Date_Of_Birth,Phone,Address)values(?,?,?,?,?,?,?)''',(Id1,name1,email1,gen1,dob1,phone1,add1))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier successfully Added')

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

    def dele():
        Id1=Id.get()
        cur.execute('''Delete from Supplier where ID=?''',(Id1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier successfully Deleted')
        show_data()

    
    Sup_frame=tk.Frame(main_frame)
    lb = tk.Label(Sup_frame,text="Supplier Page",
                  font=('Bold',40)).grid(row=0,column=0,columnspan=4)
    Sup_ID=tk.Label(Sup_frame,text="Supplier ID",font=('Bold',15)).grid(row=1,column=0)
    Sup_id=tk.Entry(Sup_frame,textvariable=Id,font=('Bold',15)).grid(row=1,column=1)
    
    Sup_Name=tk.Label(Sup_frame,text="Supplier Name",font=('Bold',15)).grid(row=1,column=2)
    Sup_name=tk.Entry(Sup_frame,textvariable=name,font=('Bold',15)).grid(row=1,column=3)
    
    Sup_Email=tk.Label(Sup_frame,text="Email Id",font=('Bold',15)).grid(row=2,column=0)
    Sup_email=tk.Entry(Sup_frame,textvariable=email,font=('Bold',15)).grid(row=2,column=1)
    
    Sup_Gen=tk.Label(Sup_frame,text="Gender",font=('Bold',15)).grid(row=2,column=2)
    Sup_gen=tk.Entry(Sup_frame,textvariable=gen,font=('Bold',15)).grid(row=2,column=3)
    
    SDOB=tk.Label(Sup_frame,text="Date Of Birth",font=('Bold',15)).grid(row=3,column=2)
    sdob=tk.Entry(Sup_frame,textvariable=dob,font=('Bold',15)).grid(row=3,column=3)
    
    Sphone=tk.Label(Sup_frame,text="Phone no:",font=('Bold',15)).grid(row=3,column=0)
    sphone=tk.Entry(Sup_frame,textvariable=phone,font=('Bold',15)).grid(row=3,column=1)
    
    Address=tk.Label(Sup_frame,text="Address",font=('Bold',15)).grid(row=5,column=0)
    Add=tk.Entry(Sup_frame,width=50,textvariable=add,font=('Bold',15)).grid(row=5,column=1,columnspan=3)
    add_Emp=tk.Button(Sup_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=6,column=0)
    up_Emp=tk.Button(Sup_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=6,column=1)
    del_Emp=tk.Button(Sup_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=6,column=2)
    re_Emp=tk.Button(Sup_frame,text="Show Data",font=('Bold',15),
                     command=show_data).grid(row=6,column=3)
    Sup_frame.pack()

def Mu():
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

    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Menu(Menu_id text,Menu_name text,
    Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,
    Menu_name2 text,Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,
    Menu_id3 text,Menu_name3 text,Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,
    Menu_id4 text,Menu_name4 text,Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,
    Menu_id5 text,Menu_name5 text,Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text)''')


    def show_data():
        print("RECORDS")
        cur.execute('''select * from Menu''')
        for record in cur:
            print('Menu_id:',str(record[0])+'\n')
            print('Menu_name:',str(record[1])+'\n')
            print('Menu_Qty:',str(record[2])+'\n')
            print('Menu_MRP:',str(record[3]+'\n'))
            print('Menu_Total:',str(record[4]+'\n'))
##        print('Menu_id2:',str(record[5])+'\n')
##        print('Menu_name2:',str(record[6])+'\n')
##        print('Menu_Qty2:',str(record[7])+'\n')
##        print('Menu_MRP2:',str(record[8]+'\n'))
##        print('Menu_Total2:',str(record[9]+'\n'))
##        print('Menu_id3:',str(record[10])+'\n')
##        print('Menu_name3:',str(record[11])+'\n')
##        print('Menu_Qty3:',str(record[12])+'\n')
##        print('Menu_MRP3:',str(record[13]+'\n'))
##        print('Menu_Total3:',str(record[14]+'\n'))
##        print('Menu_id4:',str(record[15])+'\n')
##        print('Menu_name4:',str(record[16])+'\n')
##        print('Menu_Qty4:',str(record[17])+'\n')
##        print('Menu_MRP4:',str(record[18]+'\n'))
##        print('Menu_Total4:',str(record[19]+'\n'))
##        print('Menu_id5:',str(record[20])+'\n')
##        print('Menu_name5:',str(record[21])+'\n')
##        print('Menu_Qty5:',str(record[22])+'\n')
##        print('Menu_MRP5:',str(record[23]+'\n'))
##        print('Menu_Total5:',str(record[24]+'\n'))
    show_data()

    def adde():        #ADDING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        cur.execute('''Insert into Menu(Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
                    ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
                    Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
                    Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
                    Menu_MRP5,Menu_Total5)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?)''',(Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51))
       
    
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully Added')

            
    def upe():  #UPDATING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        cur.execute('''Update Menu SET Menu_name=?,
                Menu_Qty=?,Menu_MRP=?,Menu_Total=?
                where Menu_id=?''',(Mname11,Mqty11,Mmrp11,Mtot11,Mid11,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully updated')

    def dele():
        Mid11 =Mid1.get()
        cur.execute('''Delete from Menu where Menu_id=?''',(Mid11,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully Deleted')
        show_data()
        
    mu_frame=tk.Frame(main_frame)
    lb = tk.Label(mu_frame,text="Menu Page",
                  font=('Bold',40)).grid(row=0,columnspan=5)#place(x=200,y=450)
    MU_ID=tk.Label(mu_frame,text="Menu ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(mu_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(mu_frame,text="Serving Size",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(mu_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    MU_TOT=tk.Label(mu_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

### Menu item 1
    MU_id1=tk.Entry(mu_frame,textvariable=Mid1,font=('Bold',15)).grid(row=4,column=0)

    MU_name1=tk.Entry(mu_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    MU_qty1=tk.Entry(mu_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)

    MU_mrp1=tk.Entry(mu_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)

    MU_tot1=tk.Entry(mu_frame,textvariable=Mtot1,font=('Bold',15)).grid(row=4,column=4)

##### Menu item  2
##    MU_id2=tk.Entry(mu_frame,textvariable=Mid2,font=('Bold',15)).grid(row=5,column=0)
##
##    MU_name2=tk.Entry(mu_frame,textvariable=Mname2,font=('Bold',15)).grid(row=5,column=1)
##
##    MU_qty2=tk.Entry(mu_frame,textvariable=Mqty2,font=('Bold',15)).grid(row=5,column=2)
##
##    MU_mrp2=tk.Entry(mu_frame,textvariable=Mmrp2,font=('Bold',15)).grid(row=5,column=3)
##
##    MU_tot2=tk.Entry(mu_frame,textvariable=Mtot2,font=('Bold',15)).grid(row=5,column=4)
##
##
##    ### Menu item 3
##    MU_id3=tk.Entry(mu_frame,textvariable=Mid3,font=('Bold',15)).grid(row=6,column=0)
##
##    MU_name3=tk.Entry(mu_frame,textvariable=Mname3,font=('Bold',15)).grid(row=6,column=1)
##
##    MU_qty3=tk.Entry(mu_frame,textvariable=Mqty3,font=('Bold',15)).grid(row=6,column=2)
##
##    MU_mrp3=tk.Entry(mu_frame,textvariable=Mmrp3,font=('Bold',15)).grid(row=6,column=3)
##
##    MU_tot3=tk.Entry(mu_frame,textvariable=Mtot3,font=('Bold',15)).grid(row=6,column=4)
##
##### Menu item 4
##    MU_id4=tk.Entry(mu_frame,textvariable=Mid4,font=('Bold',15)).grid(row=7,column=0)
##
##    MU_name4=tk.Entry(mu_frame,textvariable=Mname4,font=('Bold',15)).grid(row=7,column=1)
##
##    MU_qty4=tk.Entry(mu_frame,textvariable=Mqty4,font=('Bold',15)).grid(row=7,column=2)
##
##    MU_mrp4=tk.Entry(mu_frame,textvariable=Mmrp4,font=('Bold',15)).grid(row=7,column=3)
##
##    MU_tot4=tk.Entry(mu_frame,textvariable=Mtot4,font=('Bold',15)).grid(row=7,column=4)
##
##### Menu item 5
##    MU_id5=tk.Entry(mu_frame,textvariable=Mid5,font=('Bold',15)).grid(row=8,column=0)
##
##    MU_name5=tk.Entry(mu_frame,textvariable=Mname5,font=('Bold',15)).grid(row=8,column=1)
##
##    MU_qty5=tk.Entry(mu_frame,textvariable=Mqty5,font=('Bold',15)).grid(row=8,column=2)
##
##    MU_mrp5=tk.Entry(mu_frame,textvariable=Mmrp5,font=('Bold',15)).grid(row=8,column=3)
##
##    MU_tot5=tk.Entry(mu_frame,textvariable=Mtot5,font=('Bold',15)).grid(row=8,column=4)


    add_Emp=tk.Button(mu_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=9,column=0)
    up_Emp=tk.Button(mu_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=9,column=1)
    del_Emp=tk.Button(mu_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=9,column=2)
    re_Emp=tk.Button(mu_frame,text="show data",font=('Bold',15),
                     command=show_data).grid(row=9,column=3)

    mu_frame.pack()
    
def CusO():
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Customer_Order(date text,
        Order_id text,Customer_ID text,Customer_Name text,Menu_id text,Menu_name text,Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,
    Menu_name2 text,Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,
    Menu_id3 text,Menu_name3 text,Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,
    Menu_id4 text,Menu_name4 text,Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,
    Menu_id5 text,Menu_name5 text,Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text)''')
        
    def show_data():
        print("RECORDS")
        cur.execute('''select * from Customer_Order''')
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
        cur.execute('''Insert into Customer_Order(date,Order_id,Customer_ID,
            Customer_Name,Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
            ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
            Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
            Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
            Menu_MRP5,Menu_Total5)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(date1,OBId1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51))
        
        con.commit()
        cur.execute('''Update Stock set Menu_Qty=Menu_Qty-1 where Menu_id=?''',(Mid11,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Order successfully Added')

            
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
        cur.execute('''Update Customer_Order SET date=?,Customer_ID=?,Customer_Name=?,
            Menu_id=?,Menu_name=?,Menu_Qty=?,Menu_MRP=?,Menu_Total=?
            ,Menu_id2=?,Menu_name2=?,Menu_Qty2=?,Menu_MRP2=?,Menu_Total2=?,Menu_id3=?,
            Menu_name3=?,Menu_Qty3=?,Menu_MRP3=?,Menu_Total3=?,Menu_id4=?,Menu_name4=?,
            Menu_Qty4=?,Menu_MRP4=?,Menu_Total4=?,Menu_id5=?,Menu_name5=?,Menu_Qty5=?,
            Menu_MRP5=?,Menu_Total5=? where Order_id=?''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,OBId1,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Order successfully updated')

    def dele():
        OBId1 = OBId.get()
        cur.execute('''Delete from Customer_Order where Order_id=?''',(OBId1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Order successfully Deleted')
        show_data()
    
    CusO_frame=tk.Frame(main_frame)
    lb = tk.Label(CusO_frame,text="Customer Order Page",
                  font=('Bold',40)).grid(row=0,column=0,columnspan=6)
    CusO_ID=tk.Label(CusO_frame,text="Order ID",font=('Bold',15)).grid(row=1,column=0)
    CusO_id=tk.Entry(CusO_frame,textvariable=OBId,font=('Bold',15)).grid(row=1,column=1)
    
    CusO_Date=tk.Label(CusO_frame,text="Order Date",font=('Bold',15)).grid(row=1,column=3)
    CusO_date=tk.Entry(CusO_frame,textvariable=date,font=('Bold',15)).grid(row=1,column=4)

    CusO_CID=tk.Label(CusO_frame,text="Customer ID",font=('Bold',15)).grid(row=2,column=0)
    CusO_cid=tk.Entry(CusO_frame,textvariable=Id,font=('Bold',15)).grid(row=2,column=1)

    Cus_Name=tk.Label(CusO_frame,text="Customer Name",font=('Bold',15)).grid(row=2,column=3)
    Cus_name=tk.Entry(CusO_frame,textvariable=name,font=('Bold',15)).grid(row=2,column=4)

    MU_ID=tk.Label(CusO_frame,text="Menu ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(CusO_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(CusO_frame,text="Quantity",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(CusO_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    MU_TOT=tk.Label(CusO_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

### Menu item 1
    MU_id1=tk.Entry(CusO_frame,textvariable=Mid1,font=('Bold',15)).grid(row=4,column=0)

    MU_name1=tk.Entry(CusO_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    MU_qty1=tk.Entry(CusO_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)

    MU_mrp1=tk.Entry(CusO_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)

    MU_tot1=tk.Entry(CusO_frame,textvariable=Mtot1,font=('Bold',15)).grid(row=4,column=4)

### Menu item  2
    MU_id2=tk.Entry(CusO_frame,textvariable=Mid2,font=('Bold',15)).grid(row=5,column=0)

    MU_name2=tk.Entry(CusO_frame,textvariable=Mname2,font=('Bold',15)).grid(row=5,column=1)

    MU_qty2=tk.Entry(CusO_frame,textvariable=Mqty2,font=('Bold',15)).grid(row=5,column=2)

    MU_mrp2=tk.Entry(CusO_frame,textvariable=Mmrp2,font=('Bold',15)).grid(row=5,column=3)

    MU_tot2=tk.Entry(CusO_frame,textvariable=Mtot2,font=('Bold',15)).grid(row=5,column=4)


    ### Menu item 3
    MU_id3=tk.Entry(CusO_frame,textvariable=Mid3,font=('Bold',15)).grid(row=6,column=0)

    MU_name3=tk.Entry(CusO_frame,textvariable=Mname3,font=('Bold',15)).grid(row=6,column=1)

    MU_qty3=tk.Entry(CusO_frame,textvariable=Mqty3,font=('Bold',15)).grid(row=6,column=2)

    MU_mrp3=tk.Entry(CusO_frame,textvariable=Mmrp3,font=('Bold',15)).grid(row=6,column=3)

    MU_tot3=tk.Entry(CusO_frame,textvariable=Mtot3,font=('Bold',15)).grid(row=6,column=4)

### Menu item 4
    MU_id4=tk.Entry(CusO_frame,textvariable=Mid4,font=('Bold',15)).grid(row=7,column=0)

    MU_name4=tk.Entry(CusO_frame,textvariable=Mname4,font=('Bold',15)).grid(row=7,column=1)

    MU_qty4=tk.Entry(CusO_frame,textvariable=Mqty4,font=('Bold',15)).grid(row=7,column=2)

    MU_mrp4=tk.Entry(CusO_frame,textvariable=Mmrp4,font=('Bold',15)).grid(row=7,column=3)

    MU_tot4=tk.Entry(CusO_frame,textvariable=Mtot4,font=('Bold',15)).grid(row=7,column=4)

### Menu item 5
    MU_id5=tk.Entry(CusO_frame,textvariable=Mid5,font=('Bold',15)).grid(row=8,column=0)

    MU_name5=tk.Entry(CusO_frame,textvariable=Mname5,font=('Bold',15)).grid(row=8,column=1)

    MU_qty5=tk.Entry(CusO_frame,textvariable=Mqty5,font=('Bold',15)).grid(row=8,column=2)

    MU_mrp5=tk.Entry(CusO_frame,textvariable=Mmrp5,font=('Bold',15)).grid(row=8,column=3)

    MU_tot5=tk.Entry(CusO_frame,textvariable=Mtot5,font=('Bold',15)).grid(row=8,column=4)


    add_Emp=tk.Button(CusO_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=9,column=0)
    up_Emp=tk.Button(CusO_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=9,column=1)
    del_Emp=tk.Button(CusO_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=9,column=2)
    re_Emp=tk.Button(CusO_frame,text="show data",font=('Bold',15)
                     ,command=show_data).grid(row=9,column=3)

    CusO_frame.pack()
    
def SupO():
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Supplier_Order(date text,
        Order_id text,Supplier_ID text,Supplier_Name text,Menu_id text,Menu_name text,Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,
    Menu_name2 text,Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,
    Menu_id3 text,Menu_name3 text,Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,
    Menu_id4 text,Menu_name4 text,Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,
    Menu_id5 text,Menu_name5 text,Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text)''')
        
    def show_data():
        print("RECORDS")
        cur.execute('''select * from Supplier_Order''')
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
        cur.execute('''Insert into Supplier_Order(date,Order_id,Supplier_ID,
            Supplier_Name,Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
            ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
            Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
            Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
            Menu_MRP5,Menu_Total5 where OBId1=?)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(date1,OBId1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51))
        
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Order successfully Added')

            
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
        cur.execute('''Update Supplier_Order SET date,Order_id,Supplier_ID,
            Supplier_Name,Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
            ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
            Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
            Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
            Menu_MRP5,Menu_Total5''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,OBId1,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Order successfully updated')

    def dele():
        OBId1 = OBId.get()
        cur.execute('''Delete from Supplier_Order where Order_id=?''',(OBId1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Order successfully Deleted')
        show_data()

    SupO_frame=tk.Frame(main_frame)
    lb = tk.Label(SupO_frame,text="Supplier Order Page",
                  font=('Bold',40)).grid(row=0,column=0,columnspan=6)#place(x=200,y=450)
    SupO_ID=tk.Label(SupO_frame,text="Order ID",font=('Bold',15)).grid(row=1,column=0)
    SupO_id=tk.Entry(SupO_frame,textvariable=OBId,font=('Bold',15)).grid(row=1,column=1)
    
    SupO_Date=tk.Label(SupO_frame,text="Order Date",font=('Bold',15)).grid(row=1,column=2)
    SupO_date=tk.Entry(SupO_frame,textvariable=date,font=('Bold',15)).grid(row=1,column=3)

    SupO_CID=tk.Label(SupO_frame,text="Supplier ID",font=('Bold',15)).grid(row=2,column=0)
    SupO_cid=tk.Entry(SupO_frame,textvariable=Id,font=('Bold',15)).grid(row=2,column=1)

    Sup_Name=tk.Label(SupO_frame,text="Supplier Name",font=('Bold',15)).grid(row=2,column=2)
    Sup_name=tk.Entry(SupO_frame,textvariable=name,font=('Bold',15)).grid(row=2,column=3)

    MU_ID=tk.Label(SupO_frame,text="Menu ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(SupO_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(SupO_frame,text="Quantity",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(SupO_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    MU_TOT=tk.Label(SupO_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

### Menu item 1
    MU_id1=tk.Entry(SupO_frame,textvariable=Mid1,font=('Bold',15)).grid(row=4,column=0)

    MU_name1=tk.Entry(SupO_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    MU_qty1=tk.Entry(SupO_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)

    MU_mrp1=tk.Entry(SupO_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)

    MU_tot1=tk.Entry(SupO_frame,textvariable=Mtot1,font=('Bold',15)).grid(row=4,column=4)

### Menu item  2
    MU_id2=tk.Entry(SupO_frame,textvariable=Mid2,font=('Bold',15)).grid(row=5,column=0)

    MU_name2=tk.Entry(SupO_frame,textvariable=Mname2,font=('Bold',15)).grid(row=5,column=1)

    MU_qty2=tk.Entry(SupO_frame,textvariable=Mqty2,font=('Bold',15)).grid(row=5,column=2)

    MU_mrp2=tk.Entry(SupO_frame,textvariable=Mmrp2,font=('Bold',15)).grid(row=5,column=3)

    MU_tot2=tk.Entry(SupO_frame,textvariable=Mtot2,font=('Bold',15)).grid(row=5,column=4)


    ### Menu item 3
    MU_id3=tk.Entry(SupO_frame,textvariable=Mid3,font=('Bold',15)).grid(row=6,column=0)

    MU_name3=tk.Entry(SupO_frame,textvariable=Mname3,font=('Bold',15)).grid(row=6,column=1)

    MU_qty3=tk.Entry(SupO_frame,textvariable=Mqty3,font=('Bold',15)).grid(row=6,column=2)

    MU_mrp3=tk.Entry(SupO_frame,textvariable=Mmrp3,font=('Bold',15)).grid(row=6,column=3)

    MU_tot3=tk.Entry(SupO_frame,textvariable=Mtot3,font=('Bold',15)).grid(row=6,column=4)

### Menu item 4
    MU_id4=tk.Entry(SupO_frame,textvariable=Mid4,font=('Bold',15)).grid(row=7,column=0)

    MU_name4=tk.Entry(SupO_frame,textvariable=Mname4,font=('Bold',15)).grid(row=7,column=1)

    MU_qty4=tk.Entry(SupO_frame,textvariable=Mqty4,font=('Bold',15)).grid(row=7,column=2)

    MU_mrp4=tk.Entry(SupO_frame,textvariable=Mmrp4,font=('Bold',15)).grid(row=7,column=3)

    MU_tot4=tk.Entry(SupO_frame,textvariable=Mtot4,font=('Bold',15)).grid(row=7,column=4)

### Menu item 5
    MU_id5=tk.Entry(SupO_frame,textvariable=Mid5,font=('Bold',15)).grid(row=8,column=0)

    MU_name5=tk.Entry(SupO_frame,textvariable=Mname5,font=('Bold',15)).grid(row=8,column=1)

    MU_qty5=tk.Entry(SupO_frame,textvariable=Mqty5,font=('Bold',15)).grid(row=8,column=2)

    MU_mrp5=tk.Entry(SupO_frame,textvariable=Mmrp5,font=('Bold',15)).grid(row=8,column=3)

    MU_tot5=tk.Entry(SupO_frame,textvariable=Mtot5,font=('Bold',15)).grid(row=8,column=4)


    add_Emp=tk.Button(SupO_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=9,column=0)
    up_Emp=tk.Button(SupO_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=9,column=1)
    del_Emp=tk.Button(SupO_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=9,column=2)
    re_Emp=tk.Button(SupO_frame,text="show data",font=('Bold',15),
                      command=show_data).grid(row=9,column=3)
    
    SupO_frame.pack()
def CusB():
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Customer_Bill(date text,
        Bill_id text,Customer_ID text,Customer_Name text,Menu_id text,Menu_name text,
        Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,Menu_name2 text,
        Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,Menu_id3 text,Menu_name3 text,
        Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,Menu_id4 text,Menu_name4 text,
        Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,Menu_id5 text,Menu_name5 text,
        Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text,Bill_AMT int)''')
        
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
        Bamt1 = Bamt.get()
        cur.execute('''Insert into Customer_Bill(date,Bill_id,Customer_ID,
            Customer_Name,Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
            ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
            Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
            Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
            Menu_MRP5,Menu_Total5,Bill_AMT)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(date1,OBId1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1))
        
        con.commit()
        show_data()
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
        Bamt1 = Bamt.get()
        cur.execute('''Update Customer_Bill SET date=?,Customer_ID=?,Customer_Name=?,
            Menu_id=?,Menu_name=?,Menu_Qty=?,Menu_MRP=?,Menu_Total=?
            ,Menu_id2=?,Menu_name2=?,Menu_Qty2=?,Menu_MRP2=?,Menu_Total2=?,Menu_id3=?,
            Menu_name3=?,Menu_Qty3=?,Menu_MRP3=?,Menu_Total3=?,Menu_id4=?,Menu_name4=?,
            Menu_Qty4=?,Menu_MRP4=?,Menu_Total4=?,Menu_id5=?,Menu_name5=?,Menu_Qty5=?,
            Menu_MRP5=?,Menu_Total5=?,Bill_AMT=? where Bill_id=?''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1,OBId1,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Bill successfully updated')

    def dele():
        OBId1 = OBId.get()
        cur.execute('''Delete from Customer_Bill where Bill_id=?''',(OBId1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Customer_Bill successfully Deleted')
        show_data()

    CusB_frame=tk.Frame(main_frame)
    lb = tk.Label(CusB_frame,text="Customer Bill Page",
                  font=('Bold',40)).grid(row=0,column=0,columnspan=6)
    CusB_ID=tk.Label(CusB_frame,text="Bill ID",font=('Bold',15)).grid(row=1,column=0)
    CusB_id=tk.Entry(CusB_frame,textvariable=OBId,font=('Bold',15)).grid(row=1,column=1)
    
    CusB_Date=tk.Label(CusB_frame,text="Bill Date",font=('Bold',15)).grid(row=1,column=2)
    CusB_date=tk.Entry(CusB_frame,textvariable=date,font=('Bold',15)).grid(row=1,column=3)

    CusB_CID=tk.Label(CusB_frame,text="Customer ID",font=('Bold',15)).grid(row=2,column=0)
    CusB_cid=tk.Entry(CusB_frame,textvariable=Id,font=('Bold',15)).grid(row=2,column=1)

    Cus_Name=tk.Label(CusB_frame,text="Customer Name",font=('Bold',15)).grid(row=2,column=2)
    Cus_name=tk.Entry(CusB_frame,textvariable=name,font=('Bold',15)).grid(row=2,column=3)


    MU_ID=tk.Label(CusB_frame,text="Menu ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(CusB_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(CusB_frame,text="Quantity",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(CusB_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    MU_TOT=tk.Label(CusB_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

### Menu item 1
    MU_id1=tk.Entry(CusB_frame,textvariable=Mid1,font=('Bold',15)).grid(row=4,column=0)

    MU_name1=tk.Entry(CusB_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    MU_qty1=tk.Entry(CusB_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)

    MU_mrp1=tk.Entry(CusB_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)

    MU_tot1=tk.Entry(CusB_frame,textvariable=Mtot1,font=('Bold',15)).grid(row=4,column=4)

### Menu item  2
    MU_id2=tk.Entry(CusB_frame,textvariable=Mid2,font=('Bold',15)).grid(row=5,column=0)

    MU_name2=tk.Entry(CusB_frame,textvariable=Mname2,font=('Bold',15)).grid(row=5,column=1)

    MU_qty2=tk.Entry(CusB_frame,textvariable=Mqty2,font=('Bold',15)).grid(row=5,column=2)

    MU_mrp2=tk.Entry(CusB_frame,textvariable=Mmrp2,font=('Bold',15)).grid(row=5,column=3)

    MU_tot2=tk.Entry(CusB_frame,textvariable=Mtot2,font=('Bold',15)).grid(row=5,column=4)


    ### Menu item 3
    MU_id3=tk.Entry(CusB_frame,textvariable=Mid3,font=('Bold',15)).grid(row=6,column=0)

    MU_name3=tk.Entry(CusB_frame,textvariable=Mname3,font=('Bold',15)).grid(row=6,column=1)

    MU_qty3=tk.Entry(CusB_frame,textvariable=Mqty3,font=('Bold',15)).grid(row=6,column=2)

    MU_mrp3=tk.Entry(CusB_frame,textvariable=Mmrp3,font=('Bold',15)).grid(row=6,column=3)

    MU_tot3=tk.Entry(CusB_frame,textvariable=Mtot3,font=('Bold',15)).grid(row=6,column=4)

### Menu item 4
    MU_id4=tk.Entry(CusB_frame,textvariable=Mid4,font=('Bold',15)).grid(row=7,column=0)

    MU_name4=tk.Entry(CusB_frame,textvariable=Mname4,font=('Bold',15)).grid(row=7,column=1)

    MU_qty4=tk.Entry(CusB_frame,textvariable=Mqty4,font=('Bold',15)).grid(row=7,column=2)

    MU_mrp4=tk.Entry(CusB_frame,textvariable=Mmrp4,font=('Bold',15)).grid(row=7,column=3)

    MU_tot4=tk.Entry(CusB_frame,textvariable=Mtot4,font=('Bold',15)).grid(row=7,column=4)

### Menu item 5
    MU_id5=tk.Entry(CusB_frame,textvariable=Mid5,font=('Bold',15)).grid(row=8,column=0)

    MU_name5=tk.Entry(CusB_frame,textvariable=Mname5,font=('Bold',15)).grid(row=8,column=1)

    MU_qty5=tk.Entry(CusB_frame,textvariable=Mqty5,font=('Bold',15)).grid(row=8,column=2)

    MU_mrp5=tk.Entry(CusB_frame,textvariable=Mmrp5,font=('Bold',15)).grid(row=8,column=3)

    MU_tot5=tk.Entry(CusB_frame,textvariable=Mtot5,font=('Bold',15)).grid(row=8,column=4)

    Bamt=tk.Button(CusB_frame,text="Bill Amount",font=('Bold',15),).grid(row=10,column=3)
    bamt_tot5=tk.Entry(CusB_frame,textvariable=Bamt,font=('Bold',15)).grid(row=10,column=4)


    add_Emp=tk.Button(CusB_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=9,column=0)
    up_Emp=tk.Button(CusB_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=9,column=1)
    del_Emp=tk.Button(CusB_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=9,column=2)
    re_Emp=tk.Button(CusB_frame,text="show data",font=('Bold',15),command=show_data).grid(row=9,column=3)

    CusB_frame.pack()
def SupB():
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Supplier_Bill(date text,
        Bill_id text,Supplier_ID text,Supplier_Name text,Menu_id text,Menu_name text,
        Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,Menu_name2 text,
        Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,Menu_id3 text,Menu_name3 text,
        Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,Menu_id4 text,Menu_name4 text,
        Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,Menu_id5 text,Menu_name5 text,
        Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text,Bill_AMT int)''')
        
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
        cur.execute('''Insert into Supplier_Bill(date,Bill_id,Supplier_ID,
            Supplier_Name,Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
            ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
            Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
            Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
            Menu_MRP5,Menu_Total5,Bill_AMT)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(date1,OBId1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1))
        
        con.commit()
        show_data()
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
        cur.execute('''Update Supplier_Bill SET date=?,Supplier_ID=?,Supplier_Name=?,
            Menu_id=?,Menu_name=?,Menu_Qty=?,Menu_MRP=?,Menu_Total=?
            ,Menu_id2=?,Menu_name2=?,Menu_Qty2=?,Menu_MRP2=?,Menu_Total2=?,Menu_id3=?,
            Menu_name3=?,Menu_Qty3=?,Menu_MRP3=?,Menu_Total3=?,Menu_id4=?,Menu_name4=?,
            Menu_Qty4=?,Menu_MRP4=?,Menu_Total4=?,Menu_id5=?,Menu_name5=?,Menu_Qty5=?,
            Menu_MRP5=?,Menu_Total5=?,Bill_AMT=? where Bill_id=?''',(date1,Id1,name1,Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51,Bamt1,OBId1,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Bill successfully updated')

    def dele():
        OBId1 = OBId.get()
        cur.execute('''Delete from Supplier_Bill where Bill_id=?''',(OBId1,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Supplier_Bill successfully Deleted')
        show_data()

    SupB_frame=tk.Frame(main_frame)
    lb = tk.Label(SupB_frame,text="Supplier Bill Page",
                  font=('Bold',40)).grid(row=0,column=0,columnspan=6)#place(x=200,y=450)
    SupB_ID=tk.Label(SupB_frame,text="Bill ID",font=('Bold',15)).grid(row=1,column=0)
    SupB_id=tk.Entry(SupB_frame,textvariable=OBId,font=('Bold',15)).grid(row=1,column=1)
    
    SupB_Date=tk.Label(SupB_frame,text="Bill Date",font=('Bold',15)).grid(row=1,column=2)
    SupB_date=tk.Entry(SupB_frame,textvariable=date,font=('Bold',15)).grid(row=1,column=3)

    SupB_CID=tk.Label(SupB_frame,text="Supplier ID",font=('Bold',15)).grid(row=2,column=0)
    SupB_cid=tk.Entry(SupB_frame,textvariable=Id,font=('Bold',15)).grid(row=2,column=1)

    Sup_Name=tk.Label(SupB_frame,text="Supplier Name",font=('Bold',15)).grid(row=2,column=2)
    Sup_name=tk.Entry(SupB_frame,textvariable=name,font=('Bold',15)).grid(row=2,column=3)

    MU_ID=tk.Label(SupB_frame,text="Menu ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(SupB_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(SupB_frame,text="Quantity",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(SupB_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    MU_TOT=tk.Label(SupB_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

### Menu item 1
    MU_id1=tk.Entry(SupB_frame,textvariable=Mid1,font=('Bold',15)).grid(row=4,column=0)

    MU_name1=tk.Entry(SupB_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    MU_qty1=tk.Entry(SupB_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)

    MU_mrp1=tk.Entry(SupB_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)

    MU_tot1=tk.Entry(SupB_frame,textvariable=Mtot1,font=('Bold',15)).grid(row=4,column=4)

### Menu item  2
    MU_id2=tk.Entry(SupB_frame,textvariable=Mid2,font=('Bold',15)).grid(row=5,column=0)

    MU_name2=tk.Entry(SupB_frame,textvariable=Mname2,font=('Bold',15)).grid(row=5,column=1)

    MU_qty2=tk.Entry(SupB_frame,textvariable=Mqty2,font=('Bold',15)).grid(row=5,column=2)

    MU_mrp2=tk.Entry(SupB_frame,textvariable=Mmrp2,font=('Bold',15)).grid(row=5,column=3)

    MU_tot2=tk.Entry(SupB_frame,textvariable=Mtot2,font=('Bold',15)).grid(row=5,column=4)


    ### Menu item 3
    MU_id3=tk.Entry(SupB_frame,textvariable=Mid3,font=('Bold',15)).grid(row=6,column=0)

    MU_name3=tk.Entry(SupB_frame,textvariable=Mname3,font=('Bold',15)).grid(row=6,column=1)

    MU_qty3=tk.Entry(SupB_frame,textvariable=Mqty3,font=('Bold',15)).grid(row=6,column=2)

    MU_mrp3=tk.Entry(SupB_frame,textvariable=Mmrp3,font=('Bold',15)).grid(row=6,column=3)

    MU_tot=tk.Entry(SupB_frame,textvariable=Mtot3,font=('Bold',15)).grid(row=6,column=4)

### Menu item 4
    MU_id4=tk.Entry(SupB_frame,textvariable=Mid4,font=('Bold',15)).grid(row=7,column=0)

    MU_name4=tk.Entry(SupB_frame,textvariable=Mname4,font=('Bold',15)).grid(row=7,column=1)

    MU_qty4=tk.Entry(SupB_frame,textvariable=Mqty4,font=('Bold',15)).grid(row=7,column=2)

    MU_mrp4=tk.Entry(SupB_frame,textvariable=Mmrp4,font=('Bold',15)).grid(row=7,column=3)

    MU_tot4=tk.Entry(SupB_frame,textvariable=Mtot4,font=('Bold',15)).grid(row=7,column=4)

### Menu item 5
    MU_id5=tk.Entry(SupB_frame,textvariable=Mid5,font=('Bold',15)).grid(row=8,column=0)

    MU_name5=tk.Entry(SupB_frame,textvariable=Mname5,font=('Bold',15)).grid(row=8,column=1)

    MU_qty5=tk.Entry(SupB_frame,textvariable=Mqty5,font=('Bold',15)).grid(row=8,column=2)

    MU_mrp5=tk.Entry(SupB_frame,textvariable=Mmrp5,font=('Bold',15)).grid(row=8,column=3)

    MU_tot5=tk.Entry(SupB_frame,textvariable=Mtot5,font=('Bold',15)).grid(row=8,column=4)

    Bamt=tk.Button(SupB_frame,text="Bill Amount",font=('Bold',15),).grid(row=10,column=3)
    bamt_tot5=tk.Entry(SupB_frame,textvariable=Bamt,font=('Bold',15)).grid(row=10,column=4)


    add_Emp=tk.Button(SupB_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=9,column=0)
    up_Emp=tk.Button(SupB_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=9,column=1)
    del_Emp=tk.Button(SupB_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=9,column=2)
    re_Emp=tk.Button(SupB_frame,text="show data",font=('Bold',15)).grid(row=9,column=3)
  
    SupB_frame.pack()
    
def Stock():
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
    con= sqlite3.connect('FFMS.db')
    cur= con.cursor()
    cur.execute('''create table if not exists Stock(Menu_id text,Menu_name text,
    Menu_Qty text,Menu_MRP text,Menu_Total text,Menu_id2 text,
    Menu_name2 text,Menu_Qty2 text,Menu_MRP2 text,Menu_Total2 text,
    Menu_id3 text,Menu_name3 text,Menu_Qty3 text,Menu_MRP3 text,Menu_Total3 text,
    Menu_id4 text,Menu_name4 text,Menu_Qty4 text,Menu_MRP4 text,Menu_Total4 text,
    Menu_id5 text,Menu_name5 text,Menu_Qty5 text,Menu_MRP5 text,Menu_Total5 text)''')


    def show_data():
        print("RECORDS")
        cur.execute('''select * from Stock''')
        for record in cur:
            print('Stock_id:',str(record[0])+'\n')
            print('Stock_name:',str(record[1])+'\n')
            print('Stock_Qty:',str(record[2])+'\n')
            print('Stock_MRP:',str(record[3]+'\n'))
            print('Stock_Total:',str(record[4]+'\n'))
    show_data()

    def adde():        #ADDING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        cur.execute('''Insert into Stock (Menu_id,Menu_name,Menu_Qty,Menu_MRP,Menu_Total
                    ,Menu_id2,Menu_name2,Menu_Qty2,Menu_MRP2,Menu_Total2,Menu_id3,
                    Menu_name3,Menu_Qty3,Menu_MRP3,Menu_Total3,Menu_id4,Menu_name4,
                    Menu_Qty4,Menu_MRP4,Menu_Total4,Menu_id5,Menu_name5,Menu_Qty5,
                    Menu_MRP5,Menu_Total5)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?)''',(Mid11,Mname11,Mqty11,Mmrp11,Mtot11,Mid21,Mname21
                    ,Mqty21,Mmrp21,Mtot21,Mid31,Mname31,Mqty31,Mmrp31,Mtot31,Mid41,
                    Mname41,Mqty41,Mmrp41,Mtot41,Mid51,Mname51,Mqty51,Mmrp51,Mtot51))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Stock successfully Added')

    def upe():  #UPDATING DATA
        Mid11 =Mid1.get()
        Mname11 = Mname1.get()
        Mqty11 = Mqty1.get()
        Mmrp11 = Mmrp1.get()
        Mtot11=Mtot1.get()
        cur.execute('''Update Stock SET Menu_name=?,
                Menu_Qty=?,Menu_MRP=?,Menu_Total=?
                where Menu_id=?''',(Mname11,Mqty11,Mmrp11,Mtot11,Mid11,))
        con.commit()
        show_data()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully updated')

    def dele():
        Mid11 =Mid1.get()
        cur.execute('''Delete from Stock where Menu_id=?''',(Mid11,))
        con.commit()
        tkinter.messagebox.showinfo('Congratulations !!','Menu successfully Deleted')
        show_data()

    mu_frame=tk.Frame(main_frame)
    lb = tk.Label(mu_frame,text="Stock Page",
                  font=('Bold',40)).grid(row=0,columnspan=5)#place(x=200,y=450)
    MU_ID=tk.Label(mu_frame,text="Stock ID",font=('Bold',15)).grid(row=3,column=0)
    MU_Name=tk.Label(mu_frame,text="Name",font=('Bold',15)).grid(row=3,column=1)
    MU_QTY=tk.Label(mu_frame,text="Quantity",font=('Bold',15)).grid(row=3,column=2)
    MU_MRP=tk.Label(mu_frame,text="MRP",font=('Bold',15)).grid(row=3,column=3)
    MU_TOT=tk.Label(mu_frame,text="Total",font=('Bold',15)).grid(row=3,column=4)

    MU_id1=tk.Entry(mu_frame,textvariable=Mid1,font=('Bold',15)).grid(row=4,column=0)

    MU_name1=tk.Entry(mu_frame,textvariable=Mname1,font=('Bold',15)).grid(row=4,column=1)

    MU_qty1=tk.Entry(mu_frame,textvariable=Mqty1,font=('Bold',15)).grid(row=4,column=2)

    MU_mrp1=tk.Entry(mu_frame,textvariable=Mmrp1,font=('Bold',15)).grid(row=4,column=3)

    MU_tot1=tk.Entry(mu_frame,textvariable=Mtot1,font=('Bold',15)).grid(row=4,column=4)

    add_Emp=tk.Button(mu_frame,text="ADD NEW",font=('Bold',15)
                      ,command=adde).grid(row=9,column=0)
    up_Emp=tk.Button(mu_frame,text="Update",font=('Bold',15),
                     command=upe).grid(row=9,column=1)
    del_Emp=tk.Button(mu_frame,text="Delete",font=('Bold',15),
                      command=dele).grid(row=9,column=2)
    re_Emp=tk.Button(mu_frame,text="show data",font=('Bold',15),
                     command=show_data).grid(row=9,column=3)

    mu_frame.pack()


root.mainloop()
