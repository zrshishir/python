import sys

totalInput, qoutient = map(int, sys.stdin.readline().split())
count = 0

for _ in range(totalInput):
    input = int(sys.stdin.readline())
    if input % qoutient == 0:
        count += 1

print(count)
