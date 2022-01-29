from gettext import find
import sys

vowel = 'aeiou'
vowelLenth = len(vowel)
consonant = 'bcdfghjklmnpqrstvwxyz'
consLenth = len(consonant)

def VowelPos(l):
    return vowel.find(l)

def ConsonantPos(l):
    return consonant.find(l)

def GetConsonant(l, charPos, input):
    charCount = CharCount(l, charPos, input)
    if charCount == 1:
        conPos = vowel.find(l)
    else:
        conPos = ((charCount - 1) * vowelLenth) % consLenth
    return consonant[conPos]

def GetVowel(l, charPos, input):
    charCount = CharCount(l, charPos, input)
    if charCount == 1:
        vowPos = consonant.find(l)
        if vowPos >= vowelLenth:
            vowPos = vowPos % vowelLenth
    else:
        vowPos = ((charCount - 1) * consLenth) % vowelLenth
    return vowel[vowPos]

def CharCount(l, charPos, input):
    if charPos > len(input):
        return input[:len(input)].count(l)
    else:
        return input[:charPos].count(l)
        
no_of_input = int(input())
for _ in range(no_of_input):
    inputText = input()
    output = ''
    for i in range(len(inputText)):
        charPos = VowelPos(inputText[i])
        if charPos >= 0:
            output = output + GetConsonant(inputText[i], i+1, inputText)
        else: 
            output = output + GetVowel(inputText[i], i+1, inputText)
    print(output)
    