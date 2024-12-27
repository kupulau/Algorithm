n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
newscore = [x/m*100 for x in scores]
print(sum(newscore)/n)