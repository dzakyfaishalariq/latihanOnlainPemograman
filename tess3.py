import time
from tkinter import *
from tkinter import messagebox
import os
os.system('cls')
jendela = Tk()
jendela.title("game")
jendela.geometry("300x300")
carakter_ular = Canvas(jendela, width=10, height=10, bg="blue")
# tampilkan gambar
for i in range(100):
    time.sleep(0.001)
    carakter_ular.place(x=i, y=0)
    jendela.update()
# tampilkan jendela aplikasi
jendela.mainloop()
