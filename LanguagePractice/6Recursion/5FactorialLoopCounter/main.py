def factorial(n, a = 1):
    if n == 0:
        return a
    a += 1
    return factorial(n - 1, a)

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