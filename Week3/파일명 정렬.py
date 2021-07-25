import re
def solution(files):
    arr = []
    
    for i in files:
        arr.append(re.split(r"([0-9]+)", i))
        
    arr.sort(key = lambda x:(x[0].lower(), int(x[1])))
             
    for i in range(len(arr)):
        arr[i] = ''.join(arr[i])
        
    return arr