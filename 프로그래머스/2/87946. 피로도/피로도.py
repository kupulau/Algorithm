import itertools

def solution(k, dungeons):
    all = list(itertools.permutations(dungeons))
    
    no_of_visits = []
    for a in all:
        b = list(a)
        cnt = 0
        now = k
        for i in range(len(b)):
            if b[i][0] > now:
                pass
            else:   # b[0] <= k
                this = now - b[i][1]
                if this < 0:
                    pass            
                else:   # now > 0
                    cnt += 1
                    now = this
        no_of_visits.append(cnt)
        
    return max(no_of_visits)