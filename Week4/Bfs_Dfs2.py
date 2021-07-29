#2606번
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
check = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

cnt = []

def dfs(node):
    check[node] = 1

    for i in range(1, n+1):
        if graph[node][i] == 1 and check[i] == 0:
            cnt.append(i)
            dfs(i)
    return len(cnt)

print(dfs(1))