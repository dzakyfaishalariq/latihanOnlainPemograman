import os
os.system('cls')


def tulisan(*a):
    n = 0
    for i in a:
        if n < len(a)-1:
            print(i, end="-")
        else:
            print(i, end=" ")
        n += 1


tulisan("I", "love", "Python", "!")
