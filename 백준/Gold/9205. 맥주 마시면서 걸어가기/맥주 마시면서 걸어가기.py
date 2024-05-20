import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(home)

    while queue:
        x, y = queue.popleft()
        if abs(x - rockFestival[0]) + abs(y - rockFestival[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if visited[i] == 0:
                disX, disY = convenienceList[i]
                if abs(x - disX) + abs(y - disY) <= 1000:
                    queue.append(convenienceList[i])
                    visited[i] = 1
    print('sad')
    return


t = int(sys.stdin.readline())

for j in range(t):
    n = int(sys.stdin.readline())
    home = [0, 0]
    convenienceList = [[0, 0] for _ in range(n)]
    rockFestival = [0, 0]

    home[0], home[1] = map(int, sys.stdin.readline().split())
    for i in range(n):
        convenienceList[i][0], convenienceList[i][1] = map(int, sys.stdin.readline().split())
    rockFestival[0], rockFestival[1] = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(n + 2)]
    bfs()



