from tkinter import *
from tkinter.ttk import *

jendela = Tk()

jendela.title('Radio Button')
jendela.geometry('500x500')

# atribut dalam jendela
label_text = Label(
    jendela,
    text='Tentukan ukuran jarak dalam meter : ',
    font=('Arial', 12)
)
s1 = Spinbox(
    jendela,
    from_=1,
    to=100,
    width=5
)
label_text.grid(row=0, column=0)
s1.grid(row=0, column=1)
jendela.mainloop()
