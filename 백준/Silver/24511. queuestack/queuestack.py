import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = deque(map(int, input().split()))

inputArr = C
for i in range(N):
    if A[i] == 0:
        inputArr.appendleft(B[i])
        inputArr.pop()

for i in range(len(inputArr)):
    print(inputArr[i], end = ' ')