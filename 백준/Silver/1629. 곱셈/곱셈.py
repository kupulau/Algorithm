a, b, c = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a%c
    X = solution(a, b//2, c)
    if b%2==0:
        return X*X%c
    else:
        return a*X*X%c
    
print(solution(a, b, c))