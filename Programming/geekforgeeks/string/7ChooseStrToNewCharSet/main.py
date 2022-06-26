def conversion(char_set: str, string: str)->str:
    print(char_set, string)
    return True

def main():
    T = int(input())
    
    while(T > 0):
        char_set = input()
        string = input()
        conversion(char_set, string)
        T -= 1
        
if __name__ == "__main__":
    main()
