#2750번 - 삽입 정렬
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i)