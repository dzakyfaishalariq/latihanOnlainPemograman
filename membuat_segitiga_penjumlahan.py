"""
    Pembuatan segitiga dengan basis hitungan yang ada dalam python
    dengan menurut seperti barisan aritmatika     
"""
from colorama import Fore, Back, Style
import os
os.system('cls')
# membuat fungsi


def segitiga_hitung(tinggi):
    print(Fore.YELLOW)
    for i in range(tinggi):
        hasil = 0
        for j in range(i+1):
            if j < i:
                print(j+1, end='+')
            else:
                print(j+1, end=' ')
            hasil += j+1
        print("{:>10}{}".format('=', hasil))
    print(Style.RESET_ALL)


print(Fore.MAGENTA)
tinggi = int(input('Masukan angka : '))
print(Style.RESET_ALL)
print("="*20)
segitiga_hitung(tinggi)
