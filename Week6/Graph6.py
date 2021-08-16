#2665번
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

arr = [list(map(int, input().strip())) for _ in range(n)]

visit = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visit[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0:
                    if arr[nx][ny] == 0:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append((nx, ny))
                    else:
                        visit[nx][ny] = visit[x][y]
                        queue.appendleft((nx, ny))

bfs()
print(visit[n-1][n-1]-1)