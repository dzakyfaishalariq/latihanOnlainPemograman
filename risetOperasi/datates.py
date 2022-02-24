import pandas as pd
import os
os.system('cls')

nilai = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
nilai2 = pd.DataFrame(nilai, index=['A', 'B'], columns=[
                      'A', 'B', 'C', 'D', 'E'])
nilai2['A'] = nilai2['A'] + 1
print(nilai2)
