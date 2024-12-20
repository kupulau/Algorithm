class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        init = [0 for x in range(len(s))]
        for i in range(len(s)):
            #init[i] = s[indices[i]]
            init[indices[i]] = s[i]
        
        answer = ''.join(init)
        return answer