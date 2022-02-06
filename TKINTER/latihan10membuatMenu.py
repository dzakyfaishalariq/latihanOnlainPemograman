import os
from tkinter import *
from tkinter import Menu as me
from turtle import bgcolor
os.system('cls')

jendela = Tk()
# membuat menu
jendela.title('Menu')
jendela.geometry('500x500')
jendela.configure(bg='lightblue')
menu = me(jendela)
list_menu = me(menu)
list_menu.add_command(label='File')
list_menu.add_command(label='Edit')
list_menu.add_command(label='Help')
menu.add_cascade(label='Tool', menu=list_menu)
jendela.config(menu=menu)

jendela.mainloop()
