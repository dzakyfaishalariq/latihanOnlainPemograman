from cProfile import label
import imp
import os
import tkinter

from matplotlib.pyplot import text
os.system('cls')
jendela = tkinter.Tk()
# nama aplikasi
jendela.title("Latihan 3")
jendela.geometry("500x500")


def fungsi():
    variabel = 'Hi' + text_box.get()
    label_tesxt.configure(text=variabel)


label_tesxt = tkinter.Label(jendela, text="Hi", font=("Arial Italic", 10))
text_box = tkinter.Entry(jendela, width=10)
tombol1 = tkinter.Button(jendela, text="Tombol 1", bg="blue",
                         fg="green", font=("Arial Bold", 10), command=fungsi)
# tampilkan di jendela
label_tesxt.grid(row=0, column=1)
text_box.grid(row=0, column=2)
tombol1.grid(row=0, column=3)
jendela.mainloop()
