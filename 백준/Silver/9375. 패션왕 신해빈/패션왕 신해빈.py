import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        _, category = input().split()   # 옷 이름은 필요없음
        if category in clothes.keys():
            clothes[category] += 1
        else:
            clothes[category] = 1
        
    answer = 1
    for c in clothes.values():
        answer *= (c+1)
        
    print(answer-1)    # 아무것도 입지 않은 케이스 제외