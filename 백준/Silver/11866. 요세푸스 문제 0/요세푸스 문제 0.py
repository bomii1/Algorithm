from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
d = deque(x for x in range(1, N+1))

results = []
for i in range(N):
    for j in range(K):
        if j == K-1:
            results.append(d.popleft())
        else:
            d.append(d.popleft())
print('<', end='')
for i in range(N):
    if i == N-1:
        print(results[i], end='')
    else:
        print(results[i], end=', ')
print('>')
