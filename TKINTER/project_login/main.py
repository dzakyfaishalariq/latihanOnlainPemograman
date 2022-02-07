from tkinter import *
from libray.fungsi_project import login
from tkinter import messagebox
import os
os.system('cls')
# fungsi untuk jalankan tombol


def login_f():
    user = text_box.get()
    password = box_password.get()
    fungsi.tombol(user, password)
    # menghapus tulisan di username dan password
    text_box.delete(0, END)
    box_password.delete(0, END)


jendela = Tk()
# area untuk alas atribut login
fungsi = login()
jendela.title('Login')
jendela.geometry('400x400')
Canvas(jendela, width=400, height=400, bg='green').pack()
# area untuk membuat atribut login
text_label = Label(jendela, text="Silahkan Login",
                   font=('Arial', 20), bg='blue', fg='white')
username_text = Label(jendela, text="Username",
                      font=('Arial', 10), bg='green', fg='white')
text_box = Entry(jendela, width=12, font=('Arial', 20))
password_text = Label(jendela, text="Password", font=(
    'Arial', 10), bg='green', fg='white')
box_password = Entry(jendela, width=12, show='*', font=('Arial', 20))
tombol_login = Button(jendela, text="Login", font=(
    'Arial', 10), bg='yellow', fg='blue', command=login_f)
# tampilkan atribut di jendela
text_label.place(x=100, y=100)
username_text.place(x=100, y=150)
text_box.place(x=100, y=170)
password_text.place(x=100, y=215)
box_password.place(x=100, y=235)
tombol_login.place(x=100, y=280)
jendela.mainloop()
