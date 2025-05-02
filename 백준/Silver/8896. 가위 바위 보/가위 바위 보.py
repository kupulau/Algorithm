t = int(input())
for _ in range(t):
    n = int(input())
    robots = [(y+1, input().strip()) for y in range(n)]
    for i in range(len(robots[0][1])):
        round = [x[1][i] for x in robots]
        
        if len(round) <= 1:
            break
        
        # tie
        if set(round) == {"R", "S", "P"} or set(round) == {"R"} or set(round) == {"S"} or set(round) == {"P"}:
            pass
        # "R" wins
        elif "R" in round and "S" in round and "P" not in round:
            remove = [x for x in robots if x[1][i]=="S"]
            for r in remove:
                robots.remove(r)
        # "S" wins
        elif "R" not in round and "S" in round and "P" in round:
            remove = [x for x in robots if x[1][i] == "P"]
            for r in remove:
                robots.remove(r)
        # "P" wins
        elif "R" in round and "S" not in round and "P" in round:
            remove = [x for x in robots if x[1][i] == "R"]
            for r in remove:
                robots.remove(r)
                
    if len(robots) >= 2:
        print(0)  # tie
    elif len(robots) == 1:
        print(robots[0][0])