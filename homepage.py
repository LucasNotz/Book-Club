import tkinter as tk
from database import *

def build_home_frame(home_frame):
    for widget in home_frame.winfo_children():
        widget.destroy()
    
    header = tk.Label(home_frame, text=f"See books", font=("Arial",16))
    header.place(x=150,y=10)

    tk.Label(home_frame,text="Title: ",font=("Arial",10)).place(x=200,y=250)
    title_entry = tk.Entry(home_frame,)
    title_entry.place(x=240,y=250,width=100)

    tk.Label(home_frame,text="Author: ",font=("Arial",10)).place(x=10,y=200)
    author_entry = tk.Entry(home_frame)
    author_entry.place(x=60,y=200,width=100)

    tk.Label(home_frame,text="Pages: ",font=("Arial",10)).place(x=10,y=250)
    pages_entry = tk.Entry(home_frame)
    pages_entry.place(x=60,y=250,width=100)

    #tk.Label(home_frame,text="Date: ",font=("Arial",10)).place(x=200,y=200)
    #added_entry = tk.Entry(home_frame)
    #added_entry.place(x=240,y=200,width=100)


    cont = tk.Frame(home_frame, bg="white")
    cont.place(x=20,y=50,width=350,height=100)

    scrollbar = tk.Scrollbar(cont)
    scrollbar.place(x=0,y=0, width=10,height=100)

    listbox = tk.Listbox(cont,yscrollcommand=scrollbar.set)
    listbox.place(x=30,y=10, width=300, height=80)

    scrollbar.config(command=listbox.yview)

    addBook = tk.Button(home_frame, text="Add book", command=lambda: add_book(title_entry,author_entry,pages_entry))
    addBook.place(x=250,y=200)

    refBook = tk.Button(home_frame, text="Refresh", command=lambda: refresh(listbox))
    refBook.place(x=250,y=160)

    remBook = tk.Button(home_frame, text="Remove book", command=lambda: remove_book(title_entry,author_entry,pages_entry))
    remBook.place(x=100,y=160)

    books = get_books()

    y_offset =10

    for book in books:
        #lbl = tk.Label(listbox, text=f"{book[1]} by {book[2]}, {book[3]} pages", bg="white", anchor="w")
        #lbl.place(x=10,y=y_offset)

        listbox.insert(tk.END, f"{book[1]} by {book[2]}, {book[3]} pages")
        y_offset +=20
