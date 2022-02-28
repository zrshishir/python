def Palindrome(s):
    last = len(s) - 1
    mid = last // 2
    start = 0
    flag = 0
    
    while start <= mid:
        if s[start] == s[last]:
            start += 1
            last -= 1
        else:
            flag = 1
            break
        
    return flag

def main():
        T = int(input())
        print(T)
        while(T > 0):
            S = input()
            if (Palindrome(S)):
                print("Palindrome")
            else:
                print("This is not palindrome")
            T-=1
        
if __name__ == "__main__":
    main()
