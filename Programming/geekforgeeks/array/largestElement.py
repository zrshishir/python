# https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/1/?category[]=Arrays&category[]=Arrays&page=1&query=category[]Arrayspage1category[]Arrays

def Largestnumber(arr):
    element = arr[0]
    for x in arr:
        if element < x:
            element = x
    
    return element

arr = [1, 8, 92, 56, 97]
print(Largestnumber(arr))

# Another one for largest number
maxNo = max((arr[i]) for i, value in enumerate(arr))
print(maxNo)
    