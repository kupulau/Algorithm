n = int(input())

roomno = 1
cnt = 1
while n > roomno:
    roomno += 6*cnt
    cnt += 1
    
print(cnt)