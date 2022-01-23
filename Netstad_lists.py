import imp


import os
os.system('cls')
n = []
s = []
hasil = []
namaLis = []
h = []
if __name__ == "__main__":
    for _ in range(int(input())):
        nama = input()
        score = float(input())
        n.append(nama)
        s.append(score)
nilai_pengurutan = sorted(s)
for i in nilai_pengurutan:
    if min(s) < i:
        h.append(i)
nilai_c = min(h)
for i in range(len(n)):
    if s[i] == nilai_c:
        hasil.append([n[i], s[i]])
for a, b in hasil:
    namaLis.append(a)
for i in sorted(namaLis):
    print(i)
