#2161번
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = deque()

for i in range(n):
    arr.append(i+1)

while len(arr) > 1:
    print(arr.popleft(), end=" ")
    arr.append(arr[0])
    arr.popleft()

print(arr.popleft())




