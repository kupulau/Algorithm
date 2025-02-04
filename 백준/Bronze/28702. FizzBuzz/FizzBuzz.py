a = input()
b = input()
c = input()

list1 = [a, b, c]
list2 = [(i, int(v)) for i, v in enumerate(list1) if v.isdigit()==True]

if list2[0][0]==0:
    answer = list2[0][1]+3
elif list2[0][0]==1:
    answer = list2[0][1]+2
elif list2[0][0]==2:
    answer = list2[0][1]+1
    
if answer%3==0 and answer%5==0:
    print("FizzBuzz")
elif answer%3==0 and answer%5!=0:
    print("Fizz")
elif answer%3!=0 and answer%5==0:
    print("Buzz")
elif answer%3!=0 and answer%5!=0:
    print(answer)