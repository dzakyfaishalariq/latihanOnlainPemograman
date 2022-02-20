class V2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # digunakan untuk menamahkan tiap unsur x dan x' dan y dan y'
        return V2D(self.x + other.x, self.y + other.y)


first = V2D(5, 7)
second = V2D(3, 9)
result = first + second
print(result.x)
