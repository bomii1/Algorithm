import sys
from collections import deque
input = sys.stdin.readline

d = deque()

N = int(input())
for i in range(N):
    cmd = input().rstrip()

    if cmd == '3':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif cmd == '4':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif cmd == '5':
        print(len(d))
    elif cmd == '6':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif cmd == '7':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif cmd == '8':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    else:
        num = int(cmd[2:])
        if cmd[0] == '1':
            d.appendleft(num)
        else:
            d.append(num)
