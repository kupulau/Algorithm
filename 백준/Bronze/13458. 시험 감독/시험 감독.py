import sys
input = sys.stdin.readline

n = int(input())     
students = list(map(int, input().split()))
b, c = map(int, input().split())      

answer = 0
for s in students:
    answer += 1
    if s < b:
        pass
    else:
        s -= b  
        if s%c == 0:
            answer += s//c
        else:
            answer += (s//c + 1)
        
print(answer)