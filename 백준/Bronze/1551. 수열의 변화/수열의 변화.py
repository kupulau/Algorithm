n, k = map(int, input().split())
list1 = list(map(int, input().split(',')))

for _ in range(k):
    list2 = []
    for i in range(len(list1)-1):
        list2.append(list1[i+1]-list1[i])
    list1 = list2
        
print(','.join(map(str, list1)))