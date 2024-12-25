import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
list2 = list1[::-1]

dp1 = [1]*n    # increasing
dp2 = [1]*n    # decreasing
for i in range(n):
    for j in range(0, i):
        if list1[i] > list1[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if list2[i] > list2[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
             
answer = []
for i in range(len(dp1)):
    answer.append(dp1[i]+dp2[n-i-1]-1)
print(max(answer))