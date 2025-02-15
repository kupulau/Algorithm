import sys
input = sys.stdin.readline

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())

if n == 0:
    print(0)
else:
    evals = []
    for _ in range(n):
        evals.append(int(input()))
    evals.sort()
    m = roundUp(n*0.15)
    
    evals = evals[m:n-m]
    
    answer = sum(evals)/(n-2*m)
    
    print(roundUp(answer))