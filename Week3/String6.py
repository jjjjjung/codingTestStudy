#2908번
a, b = input().split()

res1 = ''.join(reversed(a))

res2 = ''.join(reversed(b))

if res1 >= res2:
    print(res1)
else: print(res2)
