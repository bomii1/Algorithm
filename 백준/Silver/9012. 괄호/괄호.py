import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = deque()
    PS = input().rstrip()
    answer = 'YES'
    for x in PS:
        if x == '(':
            s.append(x)
        elif x == ')':
            if len(s) == 0:
                answer = 'NO'
                break
            else:
                s.pop()
    if len(s) != 0:
        answer = 'NO'
    print(answer)