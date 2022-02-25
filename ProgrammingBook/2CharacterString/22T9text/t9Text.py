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
        return prop[seq]
    return ''

def main():
        T = int(input())
        
        while(T > 0):
            wordInput = int(input())
            d = []
            while wordInput > 0:
                word, weight = input().split()
                d.append((word, int(weight)))
                wordInput -= 1
            
            prop = PredictiveWord(d)
            
            keyInput = int(input())
            while keyInput > 0:
                seq = 0
                for n in input():
                    seq = seq * 10 + int(n)
                    res = Propose(prop, str(seq))
                    if res != '':
                        print(res)
                    else:
                        print("MANUALLY")
                keyInput -= 1
            T-=1
        
if __name__ == "__main__":
    main()
