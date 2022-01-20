from array import array


# https://practice.geeksforgeeks.org/problems/c-arrays-sum-of-array-set-14805/1/?category[]=Arrays&category[]=Arrays&page=1&query=category[]Arrayspage1category[]Arrays

def ArraySum(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum
    
    
arr = [1, 2, 3, 4, 5, 6]
print(ArraySum(arr))