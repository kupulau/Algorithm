class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key1 = []
        for k in key:
            if k in key1:
                pass
            else:
                key1.append(k)

        if ' ' in key1:
            key1.remove(' ')
        
        alphabets = [chr(i) for i in range(97, 123)]
        
        code = {}
        for i, v in enumerate(key1):
            code[v] = alphabets[i]
        code[' '] = ' '
        
        new = []
        for m in message:
            new.append(code[m])
            
        newmsg = ''.join(new)
        
        return newmsg

        