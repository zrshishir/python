def IsPalindrome(number):
    storeNo = number
    result = 0
    i = 0
    while number > 0:
        result = result * 10 + (number % 10)
        number = int(number / 10)
        i += 1
    return result == storeNo


def main():
    T = int(input())
    
    while(T > 0):
        lowerRange, upperRange = map(int, input().split())
        while lowerRange <= upperRange:
            if IsPalindrome(lowerRange):
                print(lowerRange, end =" ")
            lowerRange += 1
        T -= 1
        
if __name__ == "__main__":
    main()
