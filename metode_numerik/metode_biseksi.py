import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# memebuat metode biseksi
# langkah nya
# definisi fungsi
import os
os.system('cls')


def f(x):
    y = x*np.exp(-x) + 1
    return y


def bisecsion(f, a, b, tol=1e-4):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        print('Tidak ada solusi dalam rentang [a,b]')
        return
    c = (a+b)/2
    fc = f(c)
    while abs(fc) > tol:
        if fa*fc < 0:
            b = c
        else:
            a = c
        c = (a+b)/2
        fc = f(c)
    return c


# menentukan rentang untuk x yang berupa batas bawah dan batas atas atau a dan b
a = int(input("Masukkan batas bawah: "))
b = int(input("Masukkan batas atas: "))
akar = bisecsion(f, a, b)
print("Nilai akar dari fungsi f(x) adalah: ", akar)
fig, ax = plt.subplots()
ax.plot(np.arange(a, b, 0.1), f(np.arange(a, b, 0.1)))
ax.scatter(akar, f(akar), c='g', s=100)
# garis x
ax.add_line(plt.axvline(x=0, color='r'))
# garis y
ax.add_line(plt.axhline(y=0, color='r'))
ax.grid()
plt.show()
