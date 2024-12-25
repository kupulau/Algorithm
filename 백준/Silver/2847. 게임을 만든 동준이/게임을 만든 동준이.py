import sys
input = sys.stdin.readline

n = int(input())

scores = []
for i in range(n):
    scores.append(int(input()))

scores = scores[::-1]  

answer = 0  

for i in range(1, n): 
    if scores[i] >= scores[i - 1]:  
        decrease = scores[i] - scores[i - 1] + 1
        scores[i] -= decrease  
        answer += decrease  

print(answer)