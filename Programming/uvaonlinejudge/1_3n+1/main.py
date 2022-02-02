
def countTimes(n, a = 0):
    a += 1
    if n == 1:
        return a
    elif n % 2 != 0:
        return countTimes(3 * n + 1, a)
    else:
        return countTimes(n / 2, a)

def main():
    while True:
        try:
            output = 0 
            outputResult = 0
            first, second = map(int, input().split())
            first = first if first < second else second
            timer = second if second > first else first
        except EOFError:
            break
        
        while timer >= first:
            output = countTimes(timer)
            outputResult = output if output >= outputResult else outputResult
            timer -= 1
        print(first, second, outputResult)
        
if __name__ == '__main__':
    main()