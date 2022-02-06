import os
from tkinter import *
from tkinter.ttk import *
import time

from click import style
os.system('cls')
jendela = Tk()

jendela.title('Kotak Pesan')
jendela.geometry('500x500')
stelan = Style()
stelan.configure(
    'black.Horizontal.TProgressbar',
    background='blue'
)
area_main_bar = Progressbar(
    jendela,
    length=200,
    style='black.Horizontal.TProgressbar'
)
# perulangan untuk membuat progress bar
for i in range(200):
    area_main_bar['value'] = i
area_main_bar.grid(row=0, column=0)
jendela.mainloop()
