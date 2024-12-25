def repeat_string(str1, num):
    step1 = list(str1)
    step2 = [num*x for x in step1]
    step3 = "".join(step2)
    return step3

input1 = int(input())
for i in range(input1):
    a, b = input().split()
    print(repeat_string(b, int(a)))