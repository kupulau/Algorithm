import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
candy = list(map(int, input().split()))

dict1 = defaultdict(int)

left = 0
right = 0
max_length = 0
while right < n:
    dict1[candy[right]] += 1
   
    while len(dict1) > 2:
        dict1[candy[left]]-= 1
        if dict1[candy[left]]==0:
            del dict1[candy[left]]
        left += 1
        
    max_length = max(max_length, right-left+1)
    right += 1
    
print(max_length)