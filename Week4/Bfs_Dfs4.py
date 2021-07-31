#1012번
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0

    for p in range(n):
        for q in range(m):
            if dfs(p, q) == True:
                cnt += 1

    print(cnt)

