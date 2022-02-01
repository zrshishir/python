def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n -2))

#{ 
#Driver Code Starts.

# Driver Code
def main():
    testcases = int(input())
    print(testcases)
    # Loop for testcases
    while(testcases > 0):
        nTerms = int(input())
        for i in range(nTerms):
            print(fibonacci(i), end=' ')
        print('')
if __name__ == '__main__':
    main()     