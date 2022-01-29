import os
os.system('cls')
p = int(input())
r = int(input())
# (y/100)*x
res = (lambda x, y: (y/100)*x)(p, r)
print(res)
