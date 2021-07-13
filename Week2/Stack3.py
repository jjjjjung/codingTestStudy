#1874번
import sys
input = sys.stdin.readline

n = int(input())
stack = []
op = []
cnt = 1
res = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        res = False
        
if res == False:
    print("NO")
else:
    for i in op:
        print(i)