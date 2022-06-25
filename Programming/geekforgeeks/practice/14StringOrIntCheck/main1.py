def isNumber(s):
    if s.isnumeric() :
        return True
    else:
        return False

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
