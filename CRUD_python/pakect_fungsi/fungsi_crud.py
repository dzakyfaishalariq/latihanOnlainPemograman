import os
os.system('cls')
# membuat class


class clas_crud:
    data_siswa = {}

    def __init__(self, user, passwort):
        self.user = user
        self.passwort = passwort

    def tambah_data(self, npm, nama, kelas, ttl, instansi, jurusan):
        self.data_siswa[npm] = [
            nama,
            kelas,
            ttl,
            instansi,
            jurusan
        ]

    def hapus_data(self, npm):
        if npm in self.data_siswa:
            self.data_siswa.pop(npm)
        else:
            print("Tidak ada data yang mau di hapus")

    def ubah_data(self, npm):
        i = 1
        data_list = None
        for data in self.data_siswa.get(npm):
            print("data ke-{} : {}".format(i, data))
            ubah = input('Apakah anda ingin menguabahnya ? [y/t]')
            if ubah == 'y':
                data_list = self.data_siswa.get(npm)
                print("masukan data yang anda ingin ubah : ")
                ubh = input("-> ")
                data_list[i-1] = ubh
            else:
                print("Data di skip")
                data_list = self.data_siswa.get(npm)
                data_list[i-1] = data
            i += 1
        print("="*50)
        print('Tampilan data anda : ')
        for tm in data_list:
            print("->{}".format(tm))

    def isi_data_dilis(self):
        return self.data_siswa
