#1427번
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in str(n):
    arr.append(int(i))

arr.sort(reverse = True)

for i in arr:
    print(i, end="")
