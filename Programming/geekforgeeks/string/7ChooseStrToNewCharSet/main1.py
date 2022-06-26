from pickletools import string1
from string import ascii_lowercase


def conversion(alphabets: str, char_set: str, string: str)->str:
    string1 = ''

    for i in string:
        string1 += alphabets[char_set.index(i)]
    
    return string1

def main():
    T = int(input())
    
    while(T > 0):
        alphabets = input()
        char_set = input()
        string = input()
        print(conversion(alphabets, char_set, string))
        T -= 1
        
if __name__ == "__main__":
    main()
