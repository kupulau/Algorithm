import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dnas = []
for _ in range(n):
    dnas.append(input().strip())
    
answer = ""
dist = 0
for i in range(m):
    cnt = {"A":0, "C":0, "G":0, "T":0}
    for j in range(n):
        cnt[dnas[j][i]] += 1
    maxcnt = max(cnt.values())
    maxs = sorted([k for k, v in cnt.items() if v == maxcnt])
    answer += maxs[0]
    dist += (n - maxcnt)
        
print(answer) 
print(dist)