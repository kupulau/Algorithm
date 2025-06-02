c1 = int(input())

cnt = 1
answer = c1
while answer !=1:
    if answer%2 == 0:
        answer /= 2
    else:   # answer%2 == 1
        answer = 3*answer + 1
    cnt += 1
    
print(cnt)