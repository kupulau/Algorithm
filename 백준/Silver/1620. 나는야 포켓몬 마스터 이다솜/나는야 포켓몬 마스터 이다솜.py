import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict1 = {}   # num : name
dict2 = {}   # name : num
for i in range(n):
    name = input().rstrip()
    dict1[i+1] = name
    dict2[name] = i+1

    
for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(dict1[int(q)])
    else:
        print(dict2[q])