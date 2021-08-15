#1926번
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

visit = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        queue.append((nx, ny))
                        count += 1
    return count

ans = []
cnt = 0
Max = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            cnt += 1
            Max = max(Max, bfs(i, j))

print(cnt)
print(Max)