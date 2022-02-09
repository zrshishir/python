from itertools import count

def majority(L):
    listString = {}
    for word in L:
        if word in listString:
            listString[word] += 1
        else:
            listString[word] = 1
    val_1st_max, arg_1st_max = max((listString[word], word) for word in listString)
    return val_1st_max, arg_1st_max

if __name__ == '__main__':
    L = 'shi shi su su su '
    print(majority(L))