import numpy as np
import os
os.system('cls')


def fungsi(nama, list_data):
    hasil = 0
    for i in list_data:
        if nama == i:
            for li in list_data[i]:
                hasil += li
            rata = hasil/len(list_data[i])
        else:
            continue
    return rata


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

print('{:0.2f}'.format(fungsi(query_name, student_marks)))
