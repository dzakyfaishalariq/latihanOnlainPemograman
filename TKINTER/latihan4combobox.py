from tkinter .ttk import *
import os
import tkinter
os.system('cls')
jendela = tkinter.Tk()

# judul aplikasi
jendela.title("Latihan 4")
jendela.geometry("500x500")
# atribut dalam jendela
label_text = tkinter.Label(
    jendela,
    text="Pilih instansi anda",
    font=(
        "Arial Italic",
        10
    )
)
# membuat combo box
combo_Box = Combobox(jendela)
# isi dari combo box
combo_Box['values'] = (
    'Polri',
    'Kementrian Agama',
    'Kementrian Pertanian',
    'Penyuluh Pertanian',
    'Universitas Bengkulu',
    'Universitas Padang',
    'Universitas Indonesia'
)
# tampilkan atribut di jendela
label_text.grid(row=0, column=0)
combo_Box.grid(row=0, column=1)
jendela.mainloop()
