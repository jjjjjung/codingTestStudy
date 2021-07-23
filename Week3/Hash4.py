#13414번
import sys
input = sys.stdin.readline

k, l = map(int, input().split())
num1 = {}
num2 = {}
res = []

for i in range(l):
    num = map(int, input().strip())
    num1[i] = num


for i in range(k):
    print(res)