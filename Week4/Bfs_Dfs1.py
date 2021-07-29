#1260번
import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
check = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(node):
    check[node] = 1
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(1, n+1):
            if graph[node][i] == 1 and check[i] == 0:
                queue.append(i)
                check[i] = 1

def dfs(node):
    check[node] = 1
    print(node, end=' ')

    for i in range(1, n+1):
        if graph[node][i] == 1 and check[i] == 0:
            dfs(i)

dfs(v)
check = [0 for _ in range(n+1)]
print()
bfs(v)
