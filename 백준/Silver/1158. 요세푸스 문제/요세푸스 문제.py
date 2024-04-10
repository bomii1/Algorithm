from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

queue = deque()
for i in range(n):
    queue.append(i+1)

print("<", end="")
while len(queue) != 0:
    for _ in range(k-1):
        queue.append(queue.popleft())
    if len(queue) == 1:
        print(queue.popleft(), end="")
    else:
        print(queue.popleft(), end=", ")
print(">")
