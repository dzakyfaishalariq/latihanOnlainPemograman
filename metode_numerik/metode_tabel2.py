import matplotlib.pyplot as plt  # membuat grafik
import numpy as np  # membuat lis
import pandas as pd  # membuat data
import os
os.system('cls')
# Algoritma metode tabel
# 1. Pertama, buatlah sebuah fungsi yang menghitung persamaan nonlinear yang akan dihitung.


def f(x):
    y = np.sin(x)
    return y
# 2. menetukan batas awal dan batas akhir
# 3. jumlah pembagi N
# 4.Hitung step pembagi


def metode_tabel(f, a, b, N):
    h = (b-a)/N
    x = np.linspace(a, b, N+1)
    i = 0
    hasilx = []
    hasily = []
    while i < N:
        if f(x[i])*f(x[i+1]) < 0:
            if f(x[i]) <= f(x[i+1]):
                print('akar didapat sebesar : ', x[i])
                hasilx.append(x[i])
                hasily.append(f(x[i]))
            else:
                print('akar didapat sebesar : ', x[i+1])
                hasilx.append(x[i+1])
                hasily.append(f(x[i+1]))
        i += 1
    return x, h, hasilx, hasily


# melakukan pengisian
a = -6
b = 6
N = 100
x, h, hasilx, hasily = metode_tabel(f, a, b, N)
fig, ax = plt.subplots()
ax.plot(x, f(x), 'r')  # grafik garis
ax.scatter(hasilx, hasily, color='b')  # grafik scter plot (titik)
ax.add_line(plt.axhline(y=0, color='g'))
ax.add_line(plt.axvline(x=0, color='g'))

plt.grid()
plt.show()
