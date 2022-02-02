def countTimes(n, a = 0):
    a += 1
    if n == 1:
        return a
    elif n % 2 != 0:
        return countTimes(3 * n + 1, a)
    else:
        return countTimes(n / 2, a)

#{ 
#Driver Code Starts.

# Driver Code
def main():
    while True:
        try:
            output = 0 
            outputResult = 0
            first, second = map(int, input().split())
        except EOFError:
            break
        print(first, second)
        while (second <= first):
            print(second, first)
            
            second -= 1
            print(first, second, output)
        
        
if __name__ == '__main__':
    main()