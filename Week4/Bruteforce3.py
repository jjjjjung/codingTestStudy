#1018번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())

count = []

for i in range(n-7):
    for j in range(m-7):
        ans1 = 0
        ans2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0: #(0, 0)이 'W'일때
                    if board[k][l] != 'W':
                        ans1 += 1
                    if board[k][l] != 'B':
                        ans2 += 1   
                else: #(0, 0)이 'B'일때
                    if board[k][l] != 'B':
                        ans1 += 1
                    if board[k][l] != 'W':
                        ans2 += 1    
        count.append(min(ans1, ans2))

print(min(count))