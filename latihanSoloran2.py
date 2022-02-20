class Player:
    def __init__(self, nama, level):
        self.nama = nama
        self.level = level

    def intro(self):
        print(self.nama + "(Level " + self.level + ")")


nama = input()
level = input()
nilai = Player(nama, level)
nilai.intro()
