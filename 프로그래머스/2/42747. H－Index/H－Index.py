def solution(citations):
    n = len(citations)
    candidates = []
    for i in range(len(citations)+1):
        condition = [x for x in citations if x >=i]
        if len(condition) >= i:
            candidates.append(i)
    answer = max(candidates)
    return answer