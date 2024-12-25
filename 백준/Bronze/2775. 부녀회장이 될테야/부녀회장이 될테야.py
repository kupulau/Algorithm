cases = int(input())
for c in range(cases):
    floor = int(input())
    no = int(input())
    apart = [[0]*no for x in range(floor+1)]
    # 0th floor
    for n in range(no):
        apart[0][n] = n+1
    # 1st floor ~
    for f in range(floor):
        for n in range(no):
            apart[f+1][n] = sum(apart[f][0:n+1])
              
    print(apart[floor][no-1])