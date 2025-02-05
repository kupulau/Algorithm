import sys
input = sys.stdin.readline

n = int(input())

list1 = []
for _ in range(n):
    a, b = map(int, input().split())
    list1.append((a,b))
    
ranklist = []
for i in range(n):
    list2 = [x for x in list1 if x[0] > list1[i][0] and x[1]>list1[i][1]]
    rank = len(list2)+1
    ranklist.append(rank)

print(*ranklist)