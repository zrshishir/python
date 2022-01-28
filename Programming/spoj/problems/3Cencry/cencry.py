import sys

def VowelPos(l):
    return 'aeiou'.find(l)
def ConsonantPos(l):
    return 'bcdfghjklmnpqrstvwxyz'.find(l)
def GetConsonant(i):
    return 'bcdfghjklmnpqrstvwxyz'[i]
def GetVowel(i):
    return 'aeiou'[i]
    
    

no_of_input = int(sys.stdin.readline())
print(no_of_input)

input = sys.stdin.readline()
print(input)
for l in input:
    if VowelPos(l) >= 0:
        print(GetConsonant(VowelPos(l)))
    else: 
        print(GetVowel(ConsonantPos(l)))

    