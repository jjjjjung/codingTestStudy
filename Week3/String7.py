#1100번
import sys
input = sys.stdin.readline

cnt = 0
arr = []
for i in range(8):
    arr.append(list(map(str, input())))

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if arr[i][j] == 'F':
                cnt += 1

print(cnt)