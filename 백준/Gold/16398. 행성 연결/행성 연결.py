import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]      # 부모 노드 기록

# 연결된 부모 노드 찾기 (with 재귀)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
 
# 행렬에서 관리 비용 입력 받기
edges = []       
for i in range(n):
    costs = list(map(int, input().split()))
    for j in range(i+1, n):              # 양방향 그래프이므로 절반만 저장 (i < j인 경우만 간선 추가)
        edges.append((costs[j], i, j))     # (비용, 노드 1, 노드 2)
        
edges.sort()   # 가장 저렴한 간선부터 선택하기 위해 비용으로 오름차순 정렬

result = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)