#10930번
from hashlib import sha256

s = input()

ans = sha256(s.encode())

print(ans.hexdigest())