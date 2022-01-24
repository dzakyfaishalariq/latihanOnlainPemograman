import os
import numpy as np
os.system('cls')


def fungsi(nilai):
    lis_ukuran = []
    hasil1 = []
    hasil2 = []
    for i in range(len(nilai)):
        lis_ukuran.append(int(nilai[i]))
    for i in range(lis_ukuran[0]):
        matrix = input().split()
        hasil1.append(matrix)
    for l in hasil1:
        lis_b = []
        for m in l:
            lis_b.append(int(m))
        hasil2.append(lis_b)
    transpor = np.array(hasil2).T
    ratakan = np.array(hasil2).flatten()
    return transpor, ratakan


if __name__ == "__main__":
    nilai = input().split()
transport, rataan = fungsi(nilai)
print(transport)
print(rataan)
