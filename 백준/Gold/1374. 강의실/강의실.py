import sys
import heapq
input = sys.stdin.readline

n = int(input())

lectures = []
for i in range(n):
    no, start, end = map(int, input().split())
    lectures.append([start, end])
    
lectures.sort(key=lambda x:x[0])

rooms = []

heapq.heappush(rooms, lectures[0][1])     

for i in range(1, n):
    if lectures[i][0] < rooms[0]:      
        heapq.heappush(rooms, lectures[i][1])     
    else:    
        heapq.heappop(rooms)       
        heapq.heappush(rooms, lectures[i][1])    
        
print(len(rooms))