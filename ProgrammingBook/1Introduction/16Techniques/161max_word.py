from itertools import count


def mostWords(L):
    count = {}
    for word in L:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    val_1st_max, arg_1st_max = max((count[word], word) for word in count)
    return val_1st_max, arg_1st_max

if __name__ == '__main__':
    L = 'shi shi su su su '
    print(mostWords(L))