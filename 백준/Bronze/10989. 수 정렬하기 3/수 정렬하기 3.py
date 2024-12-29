import sys
input = sys.stdin.readline

n = int(input())

cnt = [0]*(10000+1)

for _ in range(n):
    cnt[int(input())] += 1
    
for i in range(len(cnt)):
    if cnt[i]!=0:
        for _ in range(cnt[i]):
            print(i)