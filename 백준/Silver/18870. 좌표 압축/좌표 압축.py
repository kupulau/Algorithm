import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
list2 = sorted(set(list1)) 

index_map = {v: k for k, v in enumerate(list2)}  

sys.stdout.write(" ".join(str(index_map[x]) for x in list1) + "\n")