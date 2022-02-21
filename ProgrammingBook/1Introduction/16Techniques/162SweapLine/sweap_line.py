#User function Template for python3

from turtle import right


class Solution:
    #Complete the below function
    def maxIntervalIntersect(S):
        B = ([(left, +1) for left in S] + [(right, -1) for right in S])
        B.sort()
        
        c = 0
        best = (c, None)
        for x, d in B:
            c += d
            print(c, d)
            if best[0] < c:
                best = (c, x)
        return best

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
        T=int(input())
        print(T)
        while(T>0):
            x, y = map(int, input().split())
            print(Solution.maxIntervalIntersect({x, y}))
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends