import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

Q = deque()

for i in range(N):
    command = input().rstrip()
    num = 0
    if command == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif command == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif command == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])
    elif command == 'size':
        print(len(Q))
    elif command == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    else:
        Q.append(int(command[4:]))
