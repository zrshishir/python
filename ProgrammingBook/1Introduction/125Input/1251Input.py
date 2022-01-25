import sys
from turtle import width

height, width = map(int, sys.stdin.readline().split())

print('result: ', height * width)
