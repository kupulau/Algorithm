a = input().strip()
b = input().strip()

joint = ""
for i in range(len(a)):
    joint += a[i]
    joint += b[i]

answer = joint
while len(answer) > 2:
    answer1 = ""
    for i in range(len(answer)-1):
        now = answer[i:i+2]
        sum1 = eval(now[0]+"+"+now[1])
        if sum1 >= 10:
            sum1 -= 10
        answer1 += str(sum1)
    answer = answer1

print(answer)