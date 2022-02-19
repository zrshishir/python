from functools import lru_cache

@lru_cache(maxsize=None)
def FiboDP(n):
    if n <= 1:
        return n
    return FiboDP(n - 2) + FiboDP(n - 1)

print(FiboDP(32))