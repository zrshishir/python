from tracemalloc import start


def Symmetry(s):
    n = len(s)
   
    flag = 0
    
    if n %  2:
        mid = n // 2 + 1
    else:
        mid = n // 2
    start1 = 0
    start2 = mid

def main():
        T = int(input())
        print(T)
        while(T > 0):
            S = input()
            if (Symmetry(S)):
                print("This is not Symmetry")
            else:
                print("This is Symmetry")
            T -= 1
        
if __name__ == "__main__":
    main()
