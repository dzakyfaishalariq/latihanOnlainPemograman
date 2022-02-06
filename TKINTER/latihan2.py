import os
import tkinter
os.system('cls')
jendela = tkinter.Tk()
# nama aplikasi
jendela.title("Latihan 2")
# ukuran aplikasi
jendela.geometry("500x500")
label_text = tkinter.Label(
    jendela, text="Ini adalah Tkinter kedua saya", font=("Arial Italic", 20))
# fungsi untuk tombol


def ubahwarna():
    tombol1.configure(text="Warna berubah", bg='yellow', fg='red')


# membuat tombol
tombol1 = tkinter.Button(jendela, text="Tombol 1",
                         bg="blue", fg="green", font=("Arial Bold", 20), command=ubahwarna)
# tampilkan tombol di jendela
#label_text.grid(row=1, column=1)
#tombol1.grid(row=2, column=1)
# tampilakn tombol di jendela dengan pack
label_text.pack()
tombol1.pack()
jendela.mainloop()
