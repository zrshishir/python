def FiboDP(n): 
    if n <= 1:
        return n
    return FiboDP(n - 1) + FiboDP(n - 2)

def FiboDPMem(n):
    mem = [0, 1]
    for i in range(2, n + 1):
        mem.append(mem[-2] + mem[-1])
    return mem[-1]

print(FiboDP(32))
print(FiboDPMem(32))