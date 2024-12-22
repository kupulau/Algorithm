string = input()
string = string.lstrip()
string = string.rstrip()
list1 = string.split(' ')
if '' in list1:
    list1.remove('')
print(len(list1))