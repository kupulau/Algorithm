import sys
input = sys.stdin.readline

n = int(input())

def change(money):
    if money < 2:
        answer = -1
    elif money == 2:
        answer = 1
    elif money == 3:
        answer = -1
    elif money == 4:
        answer = 2
    elif money == 5:
        answer = 1
    else:    # money >= 6
        result1 = money // 5
        result2 = money - 5*result1
        if result2 % 2 == 0:
            answer = result1 + result2/2
        else:
            while result1 > 0:
                result1 -= 1
                result3 = money - 5*result1
                if result3 %2 == 0:
                    answer = result1 + result3/2
                    break
                else:
                    answer = -1
    return int(answer)            
        
print(change(n))