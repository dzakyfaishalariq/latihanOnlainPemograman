"""
Lebih banyak metode ajaib untuk operator umum:
__sub__ untuk -
__mul__ untuk *
__truediv__ untuk /
__floordiv__ untuk //
__mod__ untuk %
__pow__ untuk **
__dan untuk &
__xor__ untuk ^
__atau__ untuk |

Ekspresi x + y diterjemahkan menjadi x.__add__(y).
Namun, jika x belum mengimplementasikan __add__, dan x dan y berbeda tipe, maka y.__radd__(x) dipanggil.
Ada metode r yang setara untuk semua metode ajaib yang baru saja disebutkan.
"""


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


nilai = SpecialString("Apa kabar ?,")
nilai2 = SpecialString("Saya sangat senang !")
print(nilai / nilai2)
