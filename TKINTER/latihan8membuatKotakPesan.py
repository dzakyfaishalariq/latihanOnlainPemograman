import os
from tkinter import *
from tkinter import messagebox
os.system('cls')
jendela = Tk()

jendela.title('Kotak Pesan')
jendela.geometry('500x500')
# membuat area masexbox


def kotakpesan():
    messagebox.showinfo(
        'Informasi',
        'Area info'
    )
    messagebox.showwarning(
        "warning",
        "area warnig"
    )
    messagebox.showerror(
        "error",
        "area error"
    )
    areaCencel = messagebox.askokcancel(
        "Apakah anda yakin?",
    )
    print(areaCencel)
    iyatidak = messagebox.askyesno(
        "Lanjut atau tidak?",
    )
    print(iyatidak)


tombol1 = Button(jendela, text='Kotak Pesan', command=kotakpesan)
# tampilkan di jendela
tombol1.grid(row=0, column=0)
jendela.mainloop()
