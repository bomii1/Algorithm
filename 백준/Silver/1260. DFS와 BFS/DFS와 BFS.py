import sys
from collections import deque

input = sys.stdin.readline

def dfs(n):
    visited1[n] = 1
    print(n, end=' ')
    for v in graph[n]:
        if visited1[v] == 0:
            dfs(v)

def bfs(n):
    queue = deque()
    queue.append(n)
    visited2[n] = 1  # 시작 노드 방문 체크

    while queue:
        x = queue.popleft()
        print(x, end=' ')

        for v in graph[x]:
            if visited2[v] == 0:
                visited2[v] = 1
                queue.append(v)

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for y in graph:
    graph[y].sort()

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

dfs(V)
print()
bfs(V)
