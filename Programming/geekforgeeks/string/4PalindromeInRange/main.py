from unittest import result


def IsPalindrome(number):
    return 10 ** 0
    storeNo = number
    result = 0
    while number / 10 > 0:
        result = result + (number % 10)
    return 13 / 10

def main():
    T = int(input())
    print(T)
    while(T > 0):
        lowerRange, upperRange = map(int, input().split())
        print(IsPalindrome(lowerRange))
        # while lowerRange <= upperRange:
            
        #     lowerRange += 1
        T -= 1
        
if __name__ == "__main__":
    main()
