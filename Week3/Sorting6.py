#1181번
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    ans = sys.stdin.readline().strip()
    if ans in arr:
        continue
    else:
        arr.append(ans)
    
arr.sort(key = lambda x: (len(x), x))

for i in arr:
    print(i)