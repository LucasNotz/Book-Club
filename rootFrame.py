import tkinter as tk 
from tkinter import messagebox
import sqlite3
import hashlib
from loginpage import *
from database import *
from homepage import *


#root

root = tk.Tk()
root.title()
root.geometry("390x300")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

login_frame = tk.Frame(root)
home_frame = tk.Frame(root)


for frame in (login_frame,home_frame):
    frame.grid(row=0,column=0, sticky="nsew")

#show frame function

def show_frame(frame, title=None):
    frame.tkraise()
    if title:
        root.title(title)


build_login_frame(show_frame, home_frame, login_frame, log_click, create_user,add_path)
show_frame(login_frame, "Log In")

build_home_frame(home_frame)



root.mainloop()
