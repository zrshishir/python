import sys


def search(arr, value):
    if value in arr:
        return arr.index(value)
    else:
        return -1
    
noOfInput = int(sys.stdin.readline())

for i in range(0, noOfInput):
    arraySize = int(sys.stdin.readline())
    inputArray = list(map(int, sys.stdin.readline().split()))
    searchedValue = int(sys.stdin.readline())
    print(search(inputArray, searchedValue))
