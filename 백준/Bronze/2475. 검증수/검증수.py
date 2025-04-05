list1 = list(map(int, input().split()))
list1 = [x**2 for x in list1]
print(sum(list1)%10)