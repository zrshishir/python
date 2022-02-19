import resource
from threading import Timer
import time
from functools import lru_cache

@lru_cache(maxsize=5)

def countTimes(n, a = 0):
    a += 1
    if n == 1:
        return a
    elif n % 2 != 0:
        return countTimes(3 * n + 1, a)
    else:
        return countTimes(n / 2, a)

memory0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
start_time = time.process_time()
def main():
    
    while True:
        try:
            output = 0 
            outputResult = 0
            first, second = map(int, input().split())
            if first > second:
                first, second = second, first
            timer = second
        except EOFError:
            memory1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            print('Memory usage: %s (kb)' % str(memory1 - memory0))
            print('Execution Time: ', time.process_time() - start_time)
            break
        
        while timer >= first:
            output = countTimes(timer)
            outputResult = output if output >= outputResult else outputResult
            timer -= 1
        print(first, second, outputResult)
        
if __name__ == '__main__':
    main()