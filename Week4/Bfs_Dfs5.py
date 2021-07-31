#2178번
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na<0 or na>=n or nb<0 or nb>=m:
                continue       
            if graph[na][nb] == 1:
                graph[na][nb] = graph[a][b] + 1
                queue.append((na, nb))

    print(graph[n-1][m-1])

bfs(0, 0)