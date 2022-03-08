from re import A


class aplikasi:
    hasil = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def jumlah(self):
        self.hasil = self.a + self.b
        return self.hasil
