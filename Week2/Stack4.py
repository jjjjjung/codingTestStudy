#9012번

t = int(input())

for i in range(t):
    vps = input()
    res = True
    stack = []

    for j in vps:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                print("NO")
                res = False
                break
            else: stack.pop()
    
    if res == True and len(stack) == 0:
        print("YES")
    elif res == True and len(stack) != 0: 
        print("NO")