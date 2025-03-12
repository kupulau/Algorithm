n = int(input())
m = int(input())
s = input()

check = 'IO'*n+'I'

cnt = 0
i = 0
while i+len(check) <= m:
    if s[i:i+len(check)] == check:
        cnt += 1
    i += 1

print(cnt)