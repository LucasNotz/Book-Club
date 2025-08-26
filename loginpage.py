import tkinter as tk
from tkinter import messagebox

def build_login_frame(show_frame, home_frame, login_frame, log_click, create_user,add_path,):

    label = tk.Label(login_frame, text="Welcome to the club of books", font=("Arial", 16))
    label.place(x=60,y=10)

    #login user struct

    userLabel = tk.Label(login_frame, text="Username: ", font=("Arial",10))
    userLabel.place(x=20,y=50)

    userEntry = tk.Entry(login_frame)
    userEntry.place(x=100,y=50,width=160,height=25)

    passLabel = tk.Label(login_frame, text="Password: ", font=("Arial",10))
    passLabel.place(x=20,y=80)

    passEntry = tk.Entry(login_frame)
    passEntry.place(x=100,y=80,width=160,height=25)

    '''
    #path func

    def define(dataEntry):
        defined = dataEntry.get()
        if not dataEntry:
            messagebox.showwarning("Input error", "Enter path")
            return
        
        return defined
    
    #database path

    dataLabel = tk.Label(login_frame, text="DB PATH ", font=("Arial",11))
    dataLabel.place(x=20,y=200)

    dataEntry = tk.Entry(login_frame)
    dataEntry.place(x=20,y=230,width=140,height=25)

    dataButton = tk.Button(login_frame, text="Define", command=lambda: define(dataEntry))
    dataButton.place(x=20,y=260,width=85,height=25)

    data2Button = tk.Button(login_frame, text="Add path", command=lambda: add_path(dataEntry))
    data2Button.place(x=100,y=260,width=85,height=25)



    #database path saved
    

    holder = tk.Frame(login_frame, bg="white")
    holder.place(x=180,y=200,width=180,height=70)

    scrollbar1 = tk.Scrollbar(holder)
    scrollbar1.place(x=0,y=0, width=10,height=70)

    listbox1 = tk.Listbox(holder, yscrollcommand=scrollbar1.set)
    listbox1.place(x=10,y=0,width=170,height=70)

    '''

    #create user structx=285,y=75

    Clabel = tk.Label(login_frame, text="Create user", font=("Arial", 11))
    Clabel.place(x=130,y=105)

    userCLabel = tk.Label(login_frame, text="Username: ", font=("Arial",10))
    userCLabel.place(x=20,y=130)

    userCEntry = tk.Entry(login_frame)
    userCEntry.place(x=100,y=130,width=160,height=25)

    passCLabel = tk.Label(login_frame, text="Password: ", font=("Arial",10))
    passCLabel.place(x=20,y=160)

    passCEntry = tk.Entry(login_frame)
    passCEntry.place(x=100,y=160,width=160,height=25)

    #login user button

    logButton = tk.Button(login_frame, text="Log In", command=lambda: log_click(userEntry,passEntry,home_frame,show_frame))
    logButton.place(x=285,y=75)

    #create user button

    CButton = tk.Button(login_frame, text="Create", command=lambda: create_user(userCEntry, passCEntry))
    CButton.place(x=285,y=140)
