# membuat fungsi
import os
os.system('cls')


def lis_pogram(N):
    list = []
    for _ in range(N):
        name, *lis = input().split()
        if name == 'append':
            list.append(int(lis[0]))
        elif name == 'insert':
            list.insert(int(lis[0]), int(lis[1]))
        elif name == 'remove':
            list.remove(int(lis[0]))
        elif name == 'sort':
            list.sort()
        elif name == 'pop':
            list.pop()
        elif name == 'reverse':
            list.reverse()
        elif name == 'print':
            print(list)


if __name__ == "__main__":
    N = int(input())
    lis_pogram(N)
