import sys
input = sys.stdin.readline

n, l = map(int, input().split())     # 신호등 개수, 도로의 길이
signals = [list(map(int, input().split())) for _ in range(n)]   # displacement, red, green
   
time_now = 0
dist_now = 0 
for i in range(n):
    dist = signals[i][0] - dist_now
    time_now += dist
    dist_now = signals[i][0]
    
    period = signals[i][1] + signals[i][2]
    if (time_now % period) < signals[i][1]:
        time_now += (signals[i][1]-(time_now % period))
    
print(time_now + (l - signals[-1][0]))