import os
os.system('cls')


def most_frequent(data: list) -> str:
    der = {}
    for d in data:
        if d in der:
            der[d] += 1
        else:
            der[d] = 1
    lis = []
    for e in der:
        lis.append(der[e])
    masimal = max(lis)
    nilai = 0
    for e in der:
        if masimal == der[e]:
            nilai = e
    return nilai


if __name__ == "__main__":
    print('Example : ')
    print(most_frequent(['a', 'b', 'c', 'a', 'b', 'c']))
    print(most_frequent(["a", "b", "c", "a", "b", "a"]) == "a")
    print(most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi")
    print("Done")
