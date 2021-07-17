#10866번
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()

for i in range(n):
    s = input().split()
    if s[0] == 'push_front':
        d.appendleft(s[1])
    elif s[0] == 'push_back':
        d.append(s[1])
    elif s[0] == 'pop_front':
        print(d.popleft() if len(d) != 0 else -1)
    elif s[0] == 'pop_back':
        print(d.pop() if len(d) != 0 else -1)
    elif s[0] == 'size':
        print(len(d))
    elif s[0] == 'empty':
        print(1 if len(d)==0 else 0)
    elif s[0] == 'front':
        print(d[0] if len(d) != 0 else -1)
    elif s[0] == 'back':
        print(d[-1] if len(d) != 0 else -1)