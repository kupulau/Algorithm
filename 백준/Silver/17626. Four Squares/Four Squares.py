import math

n = int(input())

def is_square(num):
    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else:
        return False
        
no = 4   # maximum 4 squares
if is_square(n)==True:
    no = 1
else:
    for i in range(int(math.sqrt(n)), 0, -1):
        if is_square(n-i**2)==True:
            no = 2
            break
        else:
            for j in range(int(math.sqrt(n-i**2)), 0, -1):
                if is_square(n-i**2-j**2)==True:
                        no = 3
                        break
           
print(no)