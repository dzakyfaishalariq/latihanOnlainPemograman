nilai = [1, 2, 3, 4, 5]
# tambah data
nilai.append(input("Masukkan nilai: "))
# hapus data
nilai.remove(int(input("Masukkan nilai yang akan dihapus: ")))
# tampilkan data
print(nilai)
nilai.extend([6, 7, 8, 9, 10])
nilai.reverse()
nilai.pop(2)
print(nilai)
