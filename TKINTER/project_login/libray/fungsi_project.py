from tkinter import messagebox


class login:
    def __init__(self):
        pass

    def tombol(self, kelik1, kelik2):
        if kelik1 == 'Dzaky' and kelik2 == '123':
            messagebox.showinfo('Login', 'Login Berhasil')
        else:
            messagebox.showinfo('Login', 'Login Gagal')
