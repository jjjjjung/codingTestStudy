#10026번
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
novisit = [[0]*n for _ in range(n)]
yesvisit = [[0]*n for _ in range(n)]
nocnt = 0
yescnt = 0

def nodfs(x, y):
    novisit[x][y] =1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if novisit[nx][ny] == 0:
                if arr[x][y] == arr[nx][ny]:
                    nodfs(nx, ny)

def yesdfs(x, y):
    yesvisit[x][y] =1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if yesvisit[nx][ny] == 0:
                if arr[x][y] == arr[nx][ny]:
                    yesdfs(nx, ny)

for i in range(n):
    for j in range(n):
        if novisit[i][j] == 0:
            nodfs(i, j)
            nocnt += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if yesvisit[i][j] == 0:
            yesdfs(i, j)
            yescnt += 1

print(nocnt, yescnt)


