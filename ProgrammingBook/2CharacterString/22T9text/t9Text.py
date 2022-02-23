t9 = "22233344455566677778889999"
# abcdefghijklmnopqrstuvwxyzmapping on the phone

def T9Text(S):
    d = {}
    for word in S:
        s = ''.join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s] = [word]
    return [d[s] for s in d if len(d[s]) > 1]

def main():
        T = int(input())
        
        while(T > 0):
            S = int(input())
            S = [x for x in input().strip().split()]
            T-=1
        print((S))
        
if __name__ == "__main__":
    main()
