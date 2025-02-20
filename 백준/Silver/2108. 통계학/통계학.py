import sys
input = sys.stdin.readline

n = int(input())

list1 = []
for _ in range(n):
    list1.append(int(input()))
    
list1.sort()

cnt = {}
for x in list1:
    if x in cnt.keys():
        cnt[x] += 1
    else:
        cnt[x] = 1
    
maxcnt = max(cnt.values())
maxlist = [k for k, v in cnt.items() if v==maxcnt]
maxlist.sort()

# mean
print(round(sum(list1)/n))
# median
if n%2==1:
    print(list1[n//2])
else:
    print((list1[n/2-1]+list1[n/2])/2)
# mode
if len(maxlist) >= 2:
    print(maxlist[1])
else:
    print(maxlist[0])
# range
print(max(list1)-min(list1))