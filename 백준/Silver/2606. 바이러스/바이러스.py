import sys

n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수

graph = [[] for i in range(n+1)] # 1번 컴퓨터를 인덱스 1로 쓰기 위해 (n+1)
visited = [0] * (n+1) # 컴퓨터를 방문했는지 (0: 미방문 / 1: 방문)
# 그래프 생성
for _ in range(v):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)


