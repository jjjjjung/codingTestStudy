#1158번
n, k = map(int, input().split())

arr = []
num = 0
ans = []

for i in range(n):
    arr.append(i+1)
print(arr)
for i in range(n):
    num += k-1
    if num >= len(arr):
        num = num % len(arr)
    ans.append(arr.pop(num))

print("<" , ", ".join(str(i) for i in ans), ">", sep='')
