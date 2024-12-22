cases = int(input())

for _ in range(cases):
    h, w, n = map(int, input().split())
    a, b = n//h, n%h
    
    if b==0:
        roomnum = a
        floor = h
    else:
        roomnum = a+1  
        floor = b  

    if roomnum < 10:
        roomnum = '0'+str(roomnum)
    else:
        roomnum = str(roomnum)

    answer = str(floor)+roomnum
    print(answer)