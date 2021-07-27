#2231번
import sys
input = sys.stdin.readline

n = int(input())
num = 0
res = 0

for i in range(1, n+1):
    num = list(map(int, str(i)))
    ans = i + sum(num)
    if ans == n:
        res = i

print(res)