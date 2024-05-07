import sys

x, y = map(int, sys.stdin.readline().split())

result = (x-1) + (x * (y-1))

print(result)