#User function Template for python3

from turtle import right


class Solution:
    #Complete the below function
    def maxIntervalIntersect(S):
        B = ([(left, +1) for left in S] + [(right, -1) for right in S])
        B.sort()
        print(B)
        c = 0
        best = (c, None)
        for x, d in B:
            c += d
            if best[0] < c:
                best = (c, x)
        return best

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
        S = [2006, 2009]
        print(Solution.maxIntervalIntersect(S))
        # T=int(input())
        # print(T)
        # S = list()
        # while(T>0):
        #     x, y = map(int, input().split())
        #     S = S.push([x, y])
        #     # print(Solution.maxIntervalIntersect({x, y}))
        #     T -= 1
        # print(S)

if __name__ == "__main__":
    main()
# } Driver Code Ends