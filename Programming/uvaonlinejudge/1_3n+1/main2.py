import sys

def countTimes(n):
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2

    return count

def callingCountTimes(first, second, output = 0):
    sys.setrecursionlimit(5000)
    if second < first:
        return output
    else:
        output = max(output, countTimes(second))
        second -= 1
        
        return callingCountTimes(first, second, output)

def Main():
    for line in sys.stdin:        
        first, second = map(int, line.split()[:2])
        print(first, second, callingCountTimes(first, second))
    
if __name__ == '__main__':
    Main()