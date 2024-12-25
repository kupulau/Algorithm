import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    list1 = list(input().split())
    answer = [list1[0]]
    for j in range(n-1):
        if answer[0] == list1[j+1]:
            answer = [list1[j+1]] + answer
        else:
            str1 = answer[0]+list1[j+1]
            if str1 == ''.join(sorted(str1)):
                answer.append(list1[j+1])
            else:
                answer = [list1[j+1]] + answer
            
    print(''.join(answer))