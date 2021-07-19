#1966번
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while queue:
        Max = max(queue)
        data = queue.popleft()
        m -= 1

        if data == Max:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(data)
            if m < 0:
                m = len(queue) - 1

        