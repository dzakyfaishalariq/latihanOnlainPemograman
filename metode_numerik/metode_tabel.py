# pembuatan metode tabel untuk meyelesaikan persamaan nonlinear
# oleh : Dzaky Faishalariq
from asyncio import events
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.system('cls')
# definisikan fungsi yang akan dihitung
# mengambil imputan sistem persamaan non linier


def f(x):
    y = x**2 - 9
    return y


x = np.linspace(-6, 6, 100)
a = 1
while a < len(x):
    if f(x[a])*f(x[a-1]) < 0:
        print('akar ketemu')
        print((int(x[a]+x[a-1])/2))
    a += 1
fig, ax = plt.subplots()
ax.plot(x, f(x), 'r')
ax.add_line(plt.axhline(y=0, color='g'))
ax.add_line(plt.axvline(x=0, color='g'))
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.axis([-6, 6, -10, 10])
plt.grid()
plt.show()
