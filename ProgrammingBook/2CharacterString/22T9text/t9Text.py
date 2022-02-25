import code
from multiprocessing.spawn import prepare
from sys import prefix


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
        print(T)
        # while(T > 0):
        #     S = int(input())
            # S = [x for x in input().strip().split()]
            # T-=1
        
if __name__ == "__main__":
    main()
