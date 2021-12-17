import json
import tkinter
from tkinter import *
import pymysql

root = tkinter.Tk()
root.title("login")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0, 0)
# LoginPage
# def LoginPage()

Label(root, text="Please enter login details", width=100, height=2,
      font=("Felix Titling", 15),
      background="#000000",
      foreground="#FACA2F").pack()
Label(root, text="").pack()
Label(root, text="Username", background="#ffffff",
      font=("Felix Titling", 14),
      justify="center").pack()
username_login_entry = Entry(root, textvariable="username")
username_login_entry.pack()
Label(root, text="").pack()
Label(root, text="Password", background="#ffffff",
      font=("Felix Titling", 14),
      justify="center",).pack()
password__login_entry = Entry(
    root, textvariable="password", show='*')
password__login_entry.pack()
Label(root, text="").pack()
Button(root, text="Login", font=("Felix Titling", 15),
       background="#ffffff",
       width=10, height=1,).pack(pady=(10, 100))


# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     database="pythonpracs")
# cursor = connection.cursor()
# cursor.execute("INSERT INTO logininfo(username, password) VALUES(%s,%s);")


connection = pymysql.connect(
    host="localhost",
    user="root",
    database="quizstar")
cursorObj = connection.cursor()
cursorObj.execute(
    "INSERT INTO logininfo VALUES ('1', 'Abhinav','abhinav@quizstar')")
root.mainloop()
