from tkinter import *
from tkinter import messagebox
import os

from numpy import size
os.system('cls')
jendela = Tk()

jendela.title("Kalkulator")
jendela.geometry("300x300")
jendela.resizable(width=False, height=False)
# fungsi untuk menghitung
angka1 = ""


def btn_huruf(huruf):
    global angka1
    angka1 = angka1 + str(huruf)
    ketikan.set(angka1)


def btn_clear():
    global angka1
    angka1 = ""
    ketikan.set(angka1)


def btn_delete():
    global angka1
    angka1 = angka1[:-1]
    ketikan.set(angka1)


def btn_hasil():
    global angka1
    angka2 = ketikan.get()
    # eval digunakan untuk menghitung suatu atribut dari string
    hasil = eval(angka2)
    ketikan.set(hasil)
    angka1 = ""


# membuat atribut untuk menampung nilai yang diketik
ketikan = StringVar()
tex_boxt = Entry(jendela, textvariable=ketikan, width=18,
                 font=("Arial", 20), justify="right")
# btn angka
btn1 = Button(jendela, text="1", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(1))
btn2 = Button(jendela, text="2", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(2))
btn3 = Button(jendela, text="3", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(3))
btn4 = Button(jendela, text="4", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(4))
btn5 = Button(jendela, text="5", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(5))
btn6 = Button(jendela, text="6", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(6))
btn7 = Button(jendela, text="7", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(7))
btn8 = Button(jendela, text="8", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(8))
btn9 = Button(jendela, text="9", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(9))
btn0 = Button(jendela, text="0", width=4, height=2,
              font=("Arial", 9), command=lambda: btn_huruf(0))
btntambah = Button(jendela, text="+", width=4, height=2,
                   font=("Arial", 9), command=lambda: btn_huruf("+"))
btnkurang = Button(jendela, text="-", width=4, height=2,
                   font=("Arial", 9), command=lambda: btn_huruf("-"))
btnbagi = Button(jendela, text="/", width=4, height=2,
                 font=("Arial", 9), command=lambda: btn_huruf("/"))
btnkali = Button(jendela, text="x", width=4, height=2,
                 font=("Arial", 9), command=lambda: btn_huruf("*"))
btnmodus = Button(jendela, text="mod", width=4, height=2,
                  font=("Arial", 9), command=lambda: btn_huruf("%"))
btnclear = Button(jendela, text="C", width=4, height=2,
                  font=("Arial", 9), command=btn_clear)
btndelet = Button(jendela, text="DEL", width=4, height=2,
                  font=("Arial", 9), command=btn_delete)
btnhasil = Button(jendela, text="=", width=4, height=2,
                  font=("Arial", 9), command=btn_hasil)
# tampilkan atribut di jendela
tex_boxt.place(x=10, y=10)
btn1.place(x=10, y=50)
btn2.place(x=50, y=50)
btn3.place(x=90, y=50)
btn4.place(x=10, y=90)
btn5.place(x=50, y=90)
btn6.place(x=90, y=90)
btn7.place(x=10, y=130)
btn8.place(x=50, y=130)
btn9.place(x=90, y=130)
btn0.place(x=50, y=180)
btntambah.place(x=150, y=50)
btnkurang.place(x=150, y=90)
btnbagi.place(x=150, y=130)
btnkali.place(x=190, y=50)
btnmodus.place(x=190, y=90)
btnclear.place(x=10, y=180)
btndelet.place(x=90, y=180)
btnhasil.place(x=190, y=130)
jendela.mainloop()
