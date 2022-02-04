import sys
import resource
import time

def countTimes(n):
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2

    return count

def callingCountTimes(first, second, output = 0):
    sys.setrecursionlimit(5000)
    if second < first:
        return output
    else:
        output = max(output, countTimes(second))
        second -= 1
        
        return callingCountTimes(first, second, output)
start_time = time.process_time()
memory0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
def Main():
    for line in sys.stdin:        
        first, second = map(int, line.split()[:2])
        print(first, second, callingCountTimes(first, second))
    memory1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print('Memory usage: %s (kb)' % str(memory1 - memory0))
    print('Execution time: ', time.process_time() - start_time)
if __name__ == '__main__':
    Main()