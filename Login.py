from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
#import main

root = tk.Tk()
window_width = 700
window_height = 600

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

###left side Frame
##lside_frame = tk.Frame(root)
##image_path = "burgerfriesdrink.jpg"
##image = Image.open(image_path)
##photo = ImageTk.PhotoImage(image)
##
##image_label = tk.Label(lside_frame, image=photo)
##image_label.pack()
##
##lside_frame.grid(row=0,column=0,rowspan=2)
###lside_frame.pack_propagate(False)
##lside_frame.configure(height=700,width=100)

main_frame = tk.Frame(root,highlightbackground="black"
                      ,highlightthickness=2)
image_path = "fastfood.jfif"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(main_frame, image=photo)
image_label.pack()

main_frame.pack()
#main_frame.pack_propagate(False)
main_frame.configure(height=300,width=100)

# Dummy user credentials
valid_credentials = {
    "Admin":"admin",
    "s": "s",
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

Username = StringVar()
Password = StringVar()

def validate_login():
    username = Username.get()
    password = Password.get()

    if username in valid_credentials and valid_credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome on Board, {}".format(username))
        open_link()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_link():
    subprocess.run(["python", "main.py"])
    #main.self()
    #url = "main.py"  # Replace this with your desired link
    #webbrowser.open(url)

Login_Frame = tk.Frame(root)
Login_Frame.pack()
#Login_Frame.pack_propagate(False)
Login_Frame.configure(width=100,height=300)

###right side Frame
##rside_frame = tk.Frame(root,highlightbackground="black"
##                      ,highlightthickness=2)
##image_path = "cafe.jpg"
##image = Image.open(image_path)
##photo = ImageTk.PhotoImage(image)
##
##image_label = tk.Label(rside_frame, image=photo)
##image_label.pack()
##
##rside_frame.grid(row=0,rowspan=2,column=2)
###rside_frame.pack_propagate(False)
##rside_frame.configure(height=700,width=100)

def create_login_page():

    lb = tk.Label(Login_Frame,text="Login Page",
                  font=('Bold',50)).grid(row=0,columnspan=4)

    label_username = tk.Label(Login_Frame, text="Username:",font=('Bold',15))
    label_username.grid(row=1,column=2)
    entry_username = tk.Entry(Login_Frame,textvariable=Username,font=('Bold',15))
    entry_username.grid(row=1,column=3)

    label_password = tk.Label(Login_Frame, text="Password:",font=('Bold',15))
    label_password.grid(row=2,column=2)
    entry_password = tk.Entry(Login_Frame, show="*",textvariable=Password,font=('Bold',15))
    entry_password.grid(row=2,column=3)

    login_button = tk.Button(Login_Frame, text="Login", command=validate_login,font=('Bold',15))
    login_button.grid(row=3,column=2,columnspan=4,pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_login_page()
