t9 = "22233344455566677778889999"
# abcdefghijklmnopqrstuvwxyzmapping on the phone

def letter_to_digit(l):
    assert 'a' <= l <= 'z'
    return t9[ord(l) - ord('a')]

def code_word(word):
    return ''.join(map(letter_to_digit, word))

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
        # T = int(input())
        
        # while(T > 0):
        #     S = int(input())
            # S = [x for x in input().strip().split()]
            # T-=1
        print(letter_to_digit('b'))
        
if __name__ == "__main__":
    main()
