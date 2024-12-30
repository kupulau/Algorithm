n = int(input())

list1 = []
for _ in range(n):
    age, name = input().split()
    list1.append([int(age), name])
    
list1.sort(key=lambda x:x[0])
    
for x in list1:
    print(*x)