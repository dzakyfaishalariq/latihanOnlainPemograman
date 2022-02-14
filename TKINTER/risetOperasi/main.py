import numpy as np
from libray_saya import fungsi_RO as RO
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
import os

os.system('cls')
fungsi = RO.area_fungsi()
jendela = Tk()
# area fungsi


def hasil_tampilan():
    a = int(text_boxt.get())
    b = int(text_boxt2.get())
    c = int(text_boxt3.get())
    d = int(text_boxt4.get())
    e = int(text_boxt5.get())
    f = int(text_boxt6.get())
    g = int(text_boxt7.get())
    h = int(text_boxt8.get())
    '''
    ax + by = c
    dx + ey = f
    '''
    n_x = np.arange(0, 50, 1)
    y1_ = (c - (a * n_x)) / b
    y2_ = (f - (d * n_x)) / e
    ax.plot(n_x, y1_, 'r')
    ax.plot(n_x, y2_, 'b')
    areaGrafik.draw()


def reset():
    ax.clear()
    ax.grid()
    areaGrafik.draw()


jendela.title('Riset Operasi')
jendela.geometry('900x500')
jendela.resizable(False, False)
area_tombol = Frame(jendela, width=300, height=500, bg='#006699')
# navigasi
text_label = Label(jendela, text='Riset Operasi', font=(
    'arial', 20, 'bold'), bg='#006699', fg='white')
text_label2 = Label(jendela, text='Fungsi Kendala : ', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
text_label3 = Label(jendela, text='Fungsi tujuan : ', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_x = Label(jendela, text='x', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_y = Label(jendela, text='y', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_tambah = Label(jendela, text='+', font=('arial', 10,
                 'bold'), bg='#006699', fg='white')
v_samadengan = Label(jendela, text='<=', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_x1 = Label(jendela, text='x', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_y1 = Label(jendela, text='y', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_tambah1 = Label(jendela, text='+', font=('arial', 10,
                                           'bold'), bg='#006699', fg='white')
v_samadengan1 = Label(jendela, text='<=', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_z = Label(jendela, text='z', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_x2 = Label(jendela, text='x', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_y2 = Label(jendela, text='y', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
v_tambah2 = Label(jendela, text='+', font=('arial', 10,
                                           'bold'), bg='#006699', fg='white')
v_samadengan2 = Label(jendela, text='=', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
tombol_hasil = Button(jendela, text='HASIL', font=(
    'arial', 10, 'bold'), bg='#00FFFF', fg='white', command=hasil_tampilan)
text_label4 = Label(jendela, text='Nilai maksimum / minimum jatuh di x dan y: ', font=(
    'arial', 10, 'bold'), bg='#006699', fg='white')
text_area = Text(jendela, width=30, height=10, font=(
    'arial', 10, 'bold'))
tombol_reset = Button(jendela, text='RESET', font=(
    'arial', 10, 'bold'), bg='#00FFFF', fg='white', command=reset)
text_boxt = Entry(jendela, width=4, font=('arial', 10, 'bold'))
text_boxt2 = Entry(jendela, width=4, font=('arial', 10, 'bold'))
text_boxt3 = Entry(jendela, width=4, font=('arial', 10, 'bold'))
text_boxt4 = Entry(jendela, width=4, font=('arial', 10, 'bold'))
text_boxt5 = Entry(jendela, width=4, font=('arial', 10, 'bold'))
text_boxt6 = Entry(jendela, width=4, font=('arial', 10, 'bold'))
text_boxt7 = Entry(jendela, width=4, font=('arial', 10, 'bold'))
text_boxt8 = Entry(jendela, width=4, font=('arial', 10, 'bold'))
area_grafik = Frame(jendela, width=600, height=500, bg='#00FFFF')


# gambar gerafik di area jendela
f = Figure(figsize=(5, 4), dpi=100)
ax = f.add_subplot(111)
ax.set_title('Grafik Area')
ax.grid(True)
ax.axis([0, 10, 0, 10])
areaGrafik = FigureCanvasTkAgg(f, master=area_grafik)
areaGrafik.get_tk_widget().place(relheight=1, relwidth=1)


# tampilkan di layar
area_tombol.place(x=0, y=0)
text_label.place(x=50, y=50)
text_label2.place(x=50, y=100)
text_boxt.place(x=50, y=130)
v_x.place(x=80, y=130)
v_tambah.place(x=100, y=130)
text_boxt2.place(x=120, y=130)
v_y.place(x=155, y=130)
v_samadengan.place(x=165, y=130)
text_boxt3.place(x=185, y=130)
text_boxt4.place(x=50, y=160)
v_x1.place(x=80, y=160)
v_tambah1.place(x=100, y=160)
text_boxt5.place(x=120, y=160)
v_y1.place(x=155, y=160)
v_samadengan1.place(x=165, y=160)
text_boxt6.place(x=185, y=160)
text_label3.place(x=50, y=190)
v_z.place(x=50, y=220)
v_samadengan2.place(x=70, y=220)
text_boxt7.place(x=90, y=220)
v_x2.place(x=120, y=220)
v_tambah2.place(x=140, y=220)
text_boxt8.place(x=160, y=220)
v_y2.place(x=195, y=220)
tombol_hasil.place(x=50, y=250)
tombol_reset.place(x=50, y=300)
area_grafik.place(x=300, y=0)
jendela.mainloop()
