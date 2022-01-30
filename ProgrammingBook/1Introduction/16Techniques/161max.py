from random import random


# n = int(input())
# tab = list(range(n))
tab = [5, 6, 1, 98, 8 , 67, 22, 45, 99]

maxNo = max((tab[index], index) for index, value in enumerate(tab))
print(maxNo)