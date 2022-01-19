from unittest import result


def Fibo(n):
    result = []
    a, b = 0, 1
    
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result;
    
    
print(Fibo(10))