from string import ascii_lowercase


def conversion(char_set: str, string: str)->str:
    # hasing for new char set 
    hash_char = dict()

    for alphabet, new_char in zip(ascii_lowercase, char_set):
        hash_char[new_char] = alphabet
    
    string1 = ''
    for i in string:
        string1 += hash_char[i]
    
    return string1

def main():
    T = int(input())
    
    while(T > 0):
        char_set = input()
        string = input()
        print(conversion(char_set, string))
        T -= 1
        
if __name__ == "__main__":
    main()
