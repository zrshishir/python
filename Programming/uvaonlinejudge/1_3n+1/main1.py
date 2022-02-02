def countTimes(n, a = 0):
    a += 1
    if n == 1:
        return a
    elif n % 2 != 0:
        return countTimes(3 * n + 1, a)
    else:
        return countTimes(n / 2, a)

def callingCountTimes(first, second, output = 0):
    outputResult = 0
    if second < first:
        return output
    outputResult = countTimes(second)
    output = outputResult if outputResult >= output else output
    return callingCountTimes(first, second - 1, output)

def main():
    while True:
        try:
            first, second = map(int, input().split())
        except EOFError:
            break
        print(first, second, callingCountTimes(first, second))
        
if __name__ == '__main__':
    main()