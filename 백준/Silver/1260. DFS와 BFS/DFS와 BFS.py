from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited2[v] = 1

    while queue:
        x = queue.popleft()
        print(x, end=' ')

        for j in range(1, N+1):
            if graph[x][j] == 1 and visited2[j] == 0:
                visited2[j] = 1
                queue.append(j)

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

dfs(V)
print()
bfs(V)
