from unittest import result


def IsPalindrome(number):
    
    storeNo = number
    result = 0
    i = 0
    while number / 10 > 0:
        print(result, number, i)
        result = result * (10 ** i) + (number % 10)
        number = int(number / 10)
        i += 1
    return result

def main():
    T = int(input())
    print(T)
    while(T > 0):
        lowerRange, upperRange = map(int, input().split())
        print(IsPalindrome(134))
        # while lowerRange <= upperRange:
            
        #     lowerRange += 1
        T -= 1
        
if __name__ == "__main__":
    main()
