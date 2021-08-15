#2468번
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
arr = []
Max = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if visit[nx][ny] == 0:
                if arr[nx][ny] > h:
                    visit[nx][ny] = 1
                    dfs(nx, ny, h)

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        Max = max(Max, arr[i][j])

ans = 0

for h in range(Max):
    visit = [[0]*n for _ in range(n)]
    area = 0

    for j in range(n):
        for k in range(n):
            if arr[j][k] > h and visit[j][k] == 0:
                area += 1
                visit[j][k] = 1
                dfs(j, k, h)
    
    ans = max(ans, area)

print(ans)