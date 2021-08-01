#1743번
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)
    return cnt
    
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 0 
            res = dfs(i, j)
            ans = max(res, ans)

print(ans)
            