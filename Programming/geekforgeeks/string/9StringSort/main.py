from string import ascii_lowercase


def stringSort(s):
    return ''.join(sorted(s))

def main():
    T = int(input())
    
    while(T > 0):
        s = input()
        print(stringSort(s))
        T -= 1
        
if __name__ == "__main__":
    main()
