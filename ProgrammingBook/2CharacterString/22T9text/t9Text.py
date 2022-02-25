t9 = "22233344455566677778889999"
# abcdefghijklmnopqrstuvwxyzmapping on the phone

def LetterToDigit(l):
    assert 'a' <= l <= 'z'
    return t9[ord(l) - ord('a')]

def CodeWord(word):
    return ''.join(map(LetterToDigit, word))

def PredictiveWord(dict):
    totalWeight = {}
    for word, weight in dict:
        prefix = ''
        for x in word:
            prefix += x
            if prefix in totalWeight:
                totalWeight[prefix] += weight
            else:
                totalWeight[prefix] = weight
    prop = {}
    for prefix in totalWeight:
        code = CodeWord(prefix)
        if code not in prop or totalWeight[prop[code]] < totalWeight[prefix]:
            prop[code] = prefix
    return prop

def Propose(prop, seq):
    if seq in prop:
        prop[seq]
    return None

def main():
        T = int(input())
        print(T)
        while(T > 0):
            wordInput = int(input())
            dict = {}
            while(wordInput > 0):
                word, weight = map(str, input().split())
                dict = word, int(weight)
                wordInput -= 1
            print(dict)
            prop = PredictiveWord(dict)
            keyInput = int(input())
            while keyInput > 0:
                print(int(input()))
                keyInput -= 1
            # S = [x for x in input().strip().split()]
            T-=1
        
if __name__ == "__main__":
    main()
