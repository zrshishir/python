def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    testcases = int(input())
    # Loop for testcases
    while(testcases > 0):
        number = int(input())
        print(factorial(number))
        testcases -= 1
        
if __name__ == '__main__':
    main()     