#10773번
import sys
input = sys.stdin.readline

k=int (input())
stack = []

for i in range(k):
    n=int(input())
    if n == 0: #pop 
        if len(stack) > 0:
            stack.pop()
    else: stack.append(n) # push

print(sum(stack))

