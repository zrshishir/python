from re import L
from wsgiref.handlers import read_environ


def MinDifSort(L):
    assert len(L) >= 2
    L.sort()
    valMin, argMin = min((L[i] - L[i - 1], i) for i in range(1, len(L)))
    return L[argMin - 1], L[argMin], valMin
    
    
L = [4, 3, 90, 76, 43]

print(MinDifSort(L))