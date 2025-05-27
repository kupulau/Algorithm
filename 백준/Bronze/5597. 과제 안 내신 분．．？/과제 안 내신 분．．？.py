import sys
input = sys.stdin.readline

students = [x+1 for x in range(30)]

for _ in range(28):
    no = int(input())
    students.remove(no)
    
students.sort()
print(students[0])
print(students[1])