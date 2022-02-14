import numpy as np


class area_n:
    poin = 0
    nnn = []

    def __init__(self, nilai):
        self.nilai = nilai

    def cekKebenaran(self, masukan):
        if masukan == self.nilai:
            self.poin += 1
            print('anda benar dengan nilai {}'.format(self.poin))
        else:
            self.poin -= 1
            print('anda salah dengan nilai {}'.format(self.poin))

    def lisssss(self):
        self.nnn = np.arange(-10, 10, 1)


data = area_n(5)
data.lisssss()
print(data.nnn)
