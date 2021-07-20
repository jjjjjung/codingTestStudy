#1157번
word = input()
word = word.upper()
alp = {}

for i in word:
    if i in alp:
        alp[i] += 1
    else:
        alp[i] = 1

max = 0
res = 0

for i in alp:
    if alp[i] > max:
        max = alp[i]
        res = i
    elif alp[i] == max:
        res = '?'
    
print(res)