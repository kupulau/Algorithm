import sys
input = sys.stdin.readline

n = int(input())
word = input().strip()

dict1 = {chr(x+97):x+1 for x in range(26)}

hashlist = [dict1[v]*31**i for i, v in enumerate(word)]

hash = sum(hashlist)%1234567891

print(int(hash))