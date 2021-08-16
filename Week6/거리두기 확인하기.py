from collections import deque

def bfs(x, y, t, places):
    visit = [[0]*5 for _ in range(5)]
    queue = deque()
    queue.append((x, y, 0))
    visit[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, t = queue.popleft() # 좌표랑 거리 넣어줌
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nt = t + 1 # 맨해튼 거리 계산

            if 0 <= nx < 5 and 0 <= ny < 5:
                if visit[nx][ny] == 0:
                    if places[nx][ny] == 'P' and nt <= 2: # 해당 위치가 P인데 거리가 2이하면 거리두기x
                        return 0
                    elif places[nx][ny] == 'O' and nt == 1: # 빈자리인데 거리가 1일때
                        queue.append((nx, ny, nt))

def solution(places):
    ans = []

    for x in places:
        check = 1 #확인
        for i in range(5):
            for j in range(5):
                if x[i][j] == 'P': # 해당 위치가 P일때
                    res = bfs(i, j, 0, x) # bfs 호출
                    if res == 0:
                        check = 0 
                        break
        ans.append(check)
    
    return ans

    
