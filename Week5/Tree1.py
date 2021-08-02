#11725번
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)

dfs(1, tree, parents)

for i in range(2, n+1):
    print(parents[i])

