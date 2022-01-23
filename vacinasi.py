import numpy as np
import os
os.system('cls')
# mencari rata rata orang yang vaksinasi
vac_nums = [
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3
]
""" 
0 => tidak pernah
1 => satu kali
2 => dua kali
3 => tiga kali
"""
print(np.var(vac_nums))
