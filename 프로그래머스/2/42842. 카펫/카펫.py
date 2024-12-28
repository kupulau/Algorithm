def solution(brown, yellow):
    total = brown + yellow
    answer = None
    for i in range(1, total+1):
        if total%i == 0:
            a, b = i, int(total/i)
            if a+b == (brown+4)/2 and a >= b:
                answer = [a, b]
            else:
                pass
        else:
            pass
    return answer