from concurrent.futures import BrokenExecutor
def countTimes(n):
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2

    return count

def callingCountTime(x, y):
    x, y = min(x, y), max(x, y)
    return max(countTimes(n) for n in range(x, y + 1))

while True:
    try:
        x, y = map(int, input().split())        
    except EOFError: 
        break
    print(x, y, callingCountTime(x, y))