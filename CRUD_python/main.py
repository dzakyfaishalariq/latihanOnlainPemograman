import os
from pakect_fungsi import fungsi_crud as fs_cr
os.system('cls')
if __name__ == "__main__":
    print("="*30)
    user = input("Masukan user anda : ")
    pasword = input("masukan password and : ")
    print("="*30)
    data = fs_cr.clas_crud(user, pasword)
    if data.user == "Dzaky" and data.passwort == "1234":
        os.system('cls')
        i = "iya"
        while i == "iya":
            os.system('cls')
            print("="*40)
            print("Selamat datang di administrasi data")
            print("Silahkan pilih menu di bawah ini:")
            print("{:>10}{:>20}".format("[1].tambah data", "[2].hapus data"))
            print("{:>10}{:>19}".format("[3].update data", "[4].cari data"))
            print("="*40)
            print("Masukan pilihan anda berupa nomor yang tertera di menu:")
            pilih = int(input("->"))
            if pilih == 1:
                os.system('cls')
                print("Silahkan masukan data anda di sini :....")
                npm = input("NPM : ")
                nama = input("Nama : ")
                kelas = input("Kelas : ")
                ttl = input("Tempat tanggal dan lahir : ")
                instansi = input("Instansi : ")
                jurusan = input("Jurusan : ")
                data.tambah_data(npm, nama, kelas, ttl, instansi, jurusan)
                print("="*127)
                print("|{:<10}|{:<20}|{:<20}|{:<30}|{:<20}|{:<20}|".format(
                    "NPM", "NAMA", "KELAS", "TTL", "INSTANSI", "JURUSAN"))
                print("="*127)
                isi = data.isi_data_dilis()
                for data_ in data.isi_data_dilis():
                    isi_ = isi.get(data_)
                    print("|{:<10}|{:<20}|{:<20}|{:<30}|{:<20}|{:<20}|".format(
                        data_, isi_[0], isi_[1], isi_[2], isi_[3], isi_[4]))
                    print("-"*127)
            elif pilih == 2:
                os.system('cls')
                print("="*127)
                print("|{:<10}|{:<20}|{:<20}|{:<30}|{:<20}|{:<20}|".format(
                    "NPM", "NAMA", "KELAS", "TTL", "INSTANSI", "JURUSAN"))
                print("="*127)
                isi = data.isi_data_dilis()
                if isi != 0:
                    for data_ in data.isi_data_dilis():
                        isi_ = isi.get(data_)
                        print("|{:<10}|{:<20}|{:<20}|{:<30}|{:<20}|{:<20}|".format(
                            data_, isi_[0], isi_[1], isi_[2], isi_[3], isi_[4]))
                        print("-"*127)
                    print("Silahkan masukan NPM yan mau di hapus : ")
                    h = input("NPM : ")
                    data.hapus_data(h)
                else:
                    print("Data masi kosong")
            elif pilih == 3:
                os.system('cls')
                isi = data.isi_data_dilis()
                if isi != 0:
                    print("="*127)
                    print("|{:<10}|{:<20}|{:<20}|{:<30}|{:<20}|{:<20}|".format(
                        "NPM", "NAMA", "KELAS", "TTL", "INSTANSI", "JURUSAN"))
                    print("="*127)
                    for data_ in data.isi_data_dilis():
                        isi_ = isi.get(data_)
                        print("|{:<10}|{:<20}|{:<20}|{:<30}|{:<20}|{:<20}|".format(
                            data_, isi_[0], isi_[1], isi_[2], isi_[3], isi_[4]))
                        print("-"*127)
                    print("Silahkan masukan data mana yang mau di ubah : ")
                    ubah = input('-> ')
                    data.ubah_data(ubah)
                else:
                    print('maaf anda belum memasukan data data di lis masi kosong')
            elif pilih == 4:
                os.system('cls')
                isi = data.isi_data_dilis()
                if isi != 0:
                    npm = input("cari data berdasarkan NPM : ")
                    if npm in isi:
                        nilai = isi.get(npm)
                        print("Nama     = {}".format(nilai[0]))
                        print("Kelas    = {}".format(nilai[1]))
                        print("TTL      = {}".format(nilai[2]))
                        print("Instansi = {}".format(nilai[3]))
                        print("Jurusan  = {}".format(nilai[4]))
                        print("Data di temukan !!")
                        print("Sukses")
                    else:
                        print("Data tidak ditemukan")
                else:
                    print("Data lis masi kosong")
            else:
                print("pilihan data tidak di temukan")
            i = input(
                "Apakah anda ingin mengulang memilih menu ?[iya/tidak] :")
    else:
        print("Maaf data anda salah")
