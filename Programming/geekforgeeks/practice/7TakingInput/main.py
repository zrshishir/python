def inPutCat():
    a = input()##complete this
    b = input()##complete this
    c = input()##complete this
    print(a, b, c) ## comma is used as it automatically separates the variables by a space. 
    ## + can also be used to concatenate but it would require manual spaces to print the words with spaces between them.


#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutCat() #the function that gets things done
        testcases-=1
        


if __name__=='__main__':
    main()