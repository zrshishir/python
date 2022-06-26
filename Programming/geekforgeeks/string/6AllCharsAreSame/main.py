from curses.ascii import isdigit


def IsAllCharSame(s):
    for i in range(len(s)) :
        if s[i] != s[0]:
            return False
    return True

def main():
    T = int(input())
    
    while(T > 0):
        S = input()

        if IsAllCharSame(S):
            print("Yes")
        else:
            print("No")

        T -= 1
        
if __name__ == "__main__":
    main()
