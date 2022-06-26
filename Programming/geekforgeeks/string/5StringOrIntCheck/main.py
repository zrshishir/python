from curses.ascii import isdigit


def isNumber(s):
    for i in range(len(s)) :
        if s[i].isdigit() != True:
            return False
    return True

def main():
    T = int(input())
    
    while(T > 0):
        S = input()

        if isNumber(S):
            print("Integer")
        else:
            print("String")

        T -= 1
        
if __name__ == "__main__":
    main()
