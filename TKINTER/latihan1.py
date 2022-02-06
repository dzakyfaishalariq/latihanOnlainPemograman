import os
import tkinter
os.system('cls')
jendela = tkinter.Tk()
label = tkinter.Label(
    jendela, text="Ini adalah Tkainter pertama saya", font=("Arial Italic", 50))
# menampilkan label
label.grid(row=20, column=10)
# menyesuaikan judul label dengan ukuran yang tepat
jendela.geometry("1000x400")
# nama aplikasi
jendela.title("Latihan 1")
jendela.mainloop()
