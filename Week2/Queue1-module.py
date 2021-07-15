#10845번
import sys
import queue
input = sys.stdin.readline

n = int(input())
q = queue.Queue()

for i in range(n):
    s = input().split()
    if s[0] == 'push':
        q.put(int (s[1]))
    elif s[0] == 'pop':
        print(-1 if q.empty() else q.get())
    elif  s[0] == 'size':
        print(q.qsize())
    elif s[0] == 'empty':
        print(1 if q.empty() else 0)
    elif s[0] == 'front':
        print(q.queue[0] if not q.empty() else -1)
    elif s[0] == 'back':
        print(q.queue[-1] if not q.empty() else -1)  