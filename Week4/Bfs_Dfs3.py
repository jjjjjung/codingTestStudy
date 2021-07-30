#2667번
import sys
input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().strip()))) 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return False # 입력 값이 잘못된 경우

    if graph[x][y] == 1: # 집이 있을 때
        global cnt
        cnt += 1
        graph[x][y] = 0 # 방문하면 집을 없애줌
        for i in range(4): # 상하좌우 검사
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny) # 인접한 집이 있으면 그 집 기준으로 또 검사
        return True # 인접한 집이 없으면 True로 return
    
    return False # 집이 없을 때

res = []
cnt = 0

for i in range(n):
    for j in range(n): # 이중 반복문을 돌면서 모든 집 검사
        if dfs(i, j) == True:
            res.append(cnt)
            cnt = 0

print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])