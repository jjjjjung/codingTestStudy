#1620번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict1 = {}
dict2 = {}

for i in range(n):
    monster = input().strip()
    dict1[i] = monster
    dict2[monster] = i

for i in range(m):
    ans = input().strip()
    if ans.isdigit() == True:
        print(dict1[int(ans)-1])
    else: 
        print(dict2[ans]+1)





