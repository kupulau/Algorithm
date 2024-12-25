import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
list1 = list(map(int, input().split()))
list1.sort()

offset = []
for i in range(len(list1)-1):
    offset.append(list1[i+1]-list1[i])
    
offset.sort(reverse=True)

answer = sum(offset[k-1:])

print(answer)