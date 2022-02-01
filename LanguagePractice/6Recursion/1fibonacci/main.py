def fibonacci(n):
    if n < 1:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    testcases = int(input())
    # Loop for testcases
    while(testcases > 0):
        nTerms = int(input())
        for i in range(nTerms):
            print(fibonacci(i), end=' ')
        testcases -= 1
        print('')
        
if __name__ == '__main__':
    main()     