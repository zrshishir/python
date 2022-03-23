def IsPalindrome(s):
    
    return s

def main():
    T = int(input())
    print(T)
    while(T > 0):
        lowerRange, upperRange = map(int, input().split())
        while lowerRange <= upperRange:
            print(IsPalindrome(lowerRange))
            lowerRange += 1
        T -= 1
        
if __name__ == "__main__":
    main()
