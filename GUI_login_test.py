import tkinter 
import sqlite3
from tkinter import messagebox


def login():
    db=sqlite3.connect('login.sqlite')
    db.execute("CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)")
    db.execute("INSERT INTO login(username, password) VALUES('admin','admin')")
    cursor=db.cursor
    cursor.execute("SELECT * FROM login where username =? AND password=?",(user_input.get(),pass_input.get()))  
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'login success')
    else: messagebox.showinfo('info', 'login failed')


main_window=tkinter.Tk()
main_window.title('Login App')
main_window.geometry('400x300') #optimize size for app
padd=20
main_window['padx']=padd
user_input=tkinter.StringVar()
pass_input = tkinter.StringVar()
info_label=tkinter.Label(main_window, text = 'Login Application')
info_label.grid(row = 0, column = 0, pady = 20)


info_user=tkinter.Label(main_window, text='Username')
info_user.grid(row = 1, column = 0)
user_input = tkinter.Entry(main_window, textvariable=user_input)
user_input.grid(row = 1, column = 1)

info_pass=tkinter.Label(main_window, text='Password')
info_pass.grid(row = 2, column = 0, pady = 20)
pass_input = tkinter.Entry(main_window, textvariable=pass_input)
pass_input.grid(row = 2, column = 1)

login_btn=tkinter.Button(main_window,text='Login', command = login)
login_btn.grid(row = 3, column = 1)


main_window.mainloop()


