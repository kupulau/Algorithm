n = int(input())

list1 = []
for _ in range(n):
    list1.append(input())
    
list1 = list(set(list1))
    
list1.sort()
list1.sort(key=lambda x:len(x))

for x in list1:
    print(x)