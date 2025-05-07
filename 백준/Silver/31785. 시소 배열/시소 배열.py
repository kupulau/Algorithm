import sys
input = sys.stdin.readline

q = int(input())
a = []
for _ in range(q):
    query = input()
    if query[0]=='1':
        one, two = query.split(' ')
        a.append(int(two))
        
    else: # query[0]=='2'
        n = len(a)//2
        list1, list2 = a[:n], a[n:]
        sum1, sum2 = sum(list1), sum(list2)
        if sum1 > sum2:
            a = list1
            print(sum2)
        elif sum1 <= sum2:
            a = list2
            print(sum1)

print(*a)