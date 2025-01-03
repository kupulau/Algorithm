import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
for _ in range(n):
    homepage, password = input().split()
    dict[homepage.rstrip()] = password.rstrip()
    
for _ in range(m):
    q = input().rstrip()
    print(dict[q])