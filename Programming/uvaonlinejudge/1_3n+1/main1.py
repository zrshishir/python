import sys

def countTimes(n, a = 0):
    a += 1
    if n == 1:
        return a
    elif n % 2 != 0:
        return countTimes(3 * n + 1, a)
    else:
        return countTimes(n // 2, a)

def callingCountTimes(first, second, output = 0):
    sys.setrecursionlimit(15000)
    if second < first:
        return output
    else:
        output = max(output, countTimes(second))
        second -= 1
        
        return callingCountTimes(first, second, output)

def main():
    
    while True:
        try:
            first, second = map(int, input().split())
            
        except EOFError:
            sys.exit(0)
            
        x, y = first, second
        if first > second:
            first, second = second, first
        print(x, y, callingCountTimes(first, second))
        
if __name__ == '__main__':
    main()