def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    if len(s1) > len(answers):
        s1 = s1[0:len(answers)]
    else:
        s1 = [1, 2, 3, 4, 5]*(len(answers)//5)
        s1.extend(s1[0:(len(answers)%5)])
    
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    if len(s2) > len(answers):
        s2 = s2[0:len(answers)]
    else:
        s2 = [2, 1, 2, 3, 2, 4, 2, 5]*(len(answers)//8)
        s2.extend(s2[0:(len(answers)%8)])
        
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    if len(s3) > len(answers):
        s3 = s3[0:len(answers)]
    else:
        s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answers)//10)
        s3.extend(s3[0:(len(answers)%10)])
    
    check1 = [a-b for a,b in zip(s1, answers)]
    check1 = [x for x in check1 if x==0]
    
    check2 = [a-b for a,b in zip(s2, answers)]
    check2 = [x for x in check2 if x==0]
    
    check3 = [a-b for a,b in zip(s3, answers)]
    check3 = [x for x in check3 if x==0]
    
    maxscore = max(len(check1), len(check2), len(check3))
    
    result = [[1, len(check1)], [2, len(check2)], [3, len(check3)]]
    
    result = [x for x in result if x[1]==maxscore]
    
    result.sort(key=lambda x:x[0])
    
    result1 = [x[0] for x in result]
    
    return result1