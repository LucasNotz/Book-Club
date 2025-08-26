import sqlite3
import tkinter as tk
from tkinter import messagebox
import hashlib 
from datetime import datetime

#path func

def define(dataEntry):
    defined = dataEntry.get()
    if not dataEntry:
        messagebox.showwarning("Input error", "Enter path")
        return
    
    return defined
    


conn = sqlite3.connect("SI.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        pages INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT NOT NULL
    )
""")

conn.commit()



def add_path(data_entry):
    path = data_entry.get()
    if not data_entry:
        messagebox.showwarning("Input error", "Enter path")
        return
    try: 
        cursor.execute(
            "insert into data (path)", 
            (path)
        )
    except sqlite3.IntegrityError:
        messagebox.showerror("Error","Path already exists")


def hash_password(password):
    password_bytes = password.encode("utf-8")
    hashed = hashlib.sha256(password_bytes).hexdigest()
    return hashed



def create_user(userCEntry,passCEntry):
    username = userCEntry.get()
    password = passCEntry.get()
    if not username or not password:
        messagebox.showwarning("Input error", "Enter both username and password")
        return
    
    password_hashed = hash_password(password)

    try:
        cursor.execute(
            "insert into users (username, password_hash) values (?, ?)",
            (username,password_hashed)
        )
        conn.commit()
        messagebox.showinfo("Great Success", f"User {username} created")
        userCEntry.delete(0, tk.END)
        passCEntry.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")



def log_click(userEntry,passEntry,home_frame,show_frame):
    username = userEntry.get()
    password = passEntry.get()
    if not username or not password:
        messagebox.showwarning("Input error", "Enter both username and password")
        return
    
    password_hashed = hash_password(password)

    cursor.execute(
        "select * from users where username = ? and password_hash = ?", 
        (username, password_hashed)
    )
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome {username}")
        show_frame(home_frame, "Home")
        return username

    else:
        messagebox.showerror("Login Failed", "Bye Bye hacker")




def add_book(title_entry, author_entry, pages_entry):
    if not title_entry or not author_entry or not pages_entry:
        messagebox.showwarning("Input error", "Enter all fields")
        return
    title = title_entry.get()
    author = author_entry.get()
    pages = pages_entry.get()
    cursor.execute(
        "insert into books (title, author, pages) values (?, ?, ?)",
        (title, author, pages)
    )
    messagebox.showinfo("Success", f"Book {title} added")
    conn.commit()

def get_books():
    cursor.execute(
        "select * from books"
    )
    return cursor.fetchall()

def refresh(listbox):
    listbox.delete(0, tk.END)

    cursor.execute(
        "select * from books"
    )
    newBooks = cursor.fetchall()
    for book in newBooks:
        listbox.insert(tk.END, f"{book[1]} by {book[2]}, {book[3]} pages")

def remove_book(title_entry, author_entry, pages_entry):
    if not title_entry or not author_entry or not pages_entry:
        messagebox.showwarning("Input error", "Enter all fields")
        return
    title = title_entry.get()
    author = author_entry.get()
    pages = pages_entry.get()
    cursor.execute(
        "delete from books where title = ? and author = ? and pages = ?",
        (title, author, pages)
    )
    messagebox.showinfo("Success", f"Book {title} removed")
    conn.commit()

