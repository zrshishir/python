def Reverse(s):
    words = s.split(' ')
    reversedString = ' '.join(reversed(words))
    return reversedString

def main():
        T = int(input())
        
        while(T > 0):
            S = input()
            print(Reverse(S))
            T -= 1
        
if __name__ == "__main__":
    main()
