from tkinter import *

jendela = Tk()

jendela.title('Area test')
jendela.geometry('300x300')
jendela.resizable(False, False)
ketikan = StringVar()


def fungsi(nilai):
    area = nilai
    ketikan.set(area)
    pass


tex_box = Entry(jendela, width=10, font=('arial', 10, 'bold'))
tombol_hasil = Button(jendela, text='HASIL', font=(
    'arial', 10, 'bold'), bg='#00FFFF', fg='white', command=lambda: fungsi(tex_box.get()))
tex_box2 = Entry(jendela, width=10, font=(
    'arial', 10, 'bold'), textvariable=ketikan)

tex_box.place(x=10, y=10)
tombol_hasil.place(x=10, y=50)
tex_box2.place(x=10, y=100)
jendela.mainloop()
