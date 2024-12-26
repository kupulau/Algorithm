n, x = map(int, input().split())
list1 = list(map(int, input().split()))
answer = [y for y in list1 if y < x]
print(*answer[:])