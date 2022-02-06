from numpy import var
import os
from tkinter import *
from tkinter.ttk import *
os.system('cls')
jendela = Tk()

jendela.title('Radio Button')
jendela.geometry('500x500')
# inisial pengambilan
var = StringVar()


def fungsi():
    selecsi = "Anda memilih " + var.get()
    label.config(text=selecsi)


# atribut dalam jendela
label_text = Label(
    jendela,
    text='Pilih Jenis Kelamin : ',
    font=('Arial', 12)
)

# radio button
R1 = Radiobutton(
    jendela,
    text='Laki-Laki',
    variable=var,
    value='Laki-Laki',
    command=fungsi
)
R2 = Radiobutton(
    jendela,
    text='Perempuan',
    variable=var,
    value='Perempuan',
    command=fungsi
)
label = Label(jendela)
# tampilkan di jendela

label_text.grid(row=0, column=0)
R1.grid(row=1, column=0)
R2.grid(row=2, column=0)
label.grid(row=3, column=0)
if __name__ == '__main__':
    jendela.mainloop()
