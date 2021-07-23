#10928번
from hashlib import sha1

s = input()

ans = sha1(s.encode())

print(ans.hexdigest())