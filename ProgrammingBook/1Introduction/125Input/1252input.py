import os

instance = list(map(int, os.read(0, 0).split()))
print(instance)