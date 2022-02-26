
from re import S


def Palindrome(s):
    return len(s)
def main():
        T = int(input())
        print(T)
        while(T > 0):
            S = input()
            print(Palindrome(S))
            T-=1
        
if __name__ == "__main__":
    main()
