import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = deque()
waitingNum = 1

for x in arr:
    stack.append(x)
    while stack and stack[-1] == waitingNum:
        stack.pop()
        waitingNum += 1

if len(stack) == 0:
    print('Nice')
else:
    print('Sad')
