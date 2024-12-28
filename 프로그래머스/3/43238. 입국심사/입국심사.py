def solution(n, times):
    answer = 0
    tmin = 1
    tmax = max(times)*n
    while tmin <= tmax:
        mid = (tmin + tmax)//2
        people = 0
        for t in times:
            people += mid//t   
            if people >= n:
                break
        # 이진 탐색 시작
        if people >= n:
            answer = mid
            tmax = mid - 1
        else:   # people < n
            tmin = mid + 1
            
    return(answer)