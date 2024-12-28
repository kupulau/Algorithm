import re

badchars = '~!@#$%^&*()=+[{]}:?,<>/'

def solution(new_id):
    answer = new_id.lower()
    answer = ''.join([x for x in answer if x not in badchars])
    answer = re.sub(r'\.{2,}', '.', answer)
    
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    if len(answer)==0:
        answer = 'a'
    elif len(answer)>=16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer)<=2:
        while len(answer) < 3:
            answer += answer[-1]
        #answer = answer[0:3]
    
    return answer