from string import ascii_lowercase


def nearest_multiple(n):
    # hasing for new char set 
    a = (n // 10) * 10
    b = a + 10

    if n - a > b - n:
        return b
    
    return a

def main():
    T = int(input())
    
    while(T > 0):
        n = int(input())
        print(nearest_multiple(n))
        T -= 1
        
if __name__ == "__main__":
    main()
