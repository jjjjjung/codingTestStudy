#1541번
import sys
input = sys.stdin.readline

s = input().split('-')
ans = []

for i in s:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    ans.append(cnt)

res = ans[0]

for i in range(len(ans)):
    res -= ans[i]

print(res+ans[0])