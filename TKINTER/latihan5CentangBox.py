import os
import tkinter
from tkinter import *
from tkinter .ttk import *

from numpy import var
os.system('cls')
jendela = Tk()
jendela.title('Centang Box')
jendela.geometry('500x500')

# membuat tanda centang
centang = BooleanVar()
centang.set(False)
centang_ = Checkbutton(
    jendela,
    text='Saya menyetujui',
    var=centang
)

# tampilkan di jendela
centang_.grid(row=0, column=0)
jendela.mainloop()
