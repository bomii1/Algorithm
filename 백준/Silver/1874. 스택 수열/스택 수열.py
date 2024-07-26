import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = deque()
arrIndex = 0
result = []
def makeSequence(s, arrIndex):
    for i in range(1, n+1):
        stack.append(i)
        result.append('+')
        while len(stack) != 0 and stack[-1] == arr[arrIndex]:
            stack.pop()
            result.append('-')
            arrIndex += 1
    return 0 if len(stack) != 0 else 1

if makeSequence(stack, arrIndex):
    for x in result:
        print(x)
else:
    print('NO')