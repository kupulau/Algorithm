a = input()
b = input()

aandb = ""  # A & B
aorb = ""   # A | B
ab = "" # A ^ B
nota = ""    # ~A
notb = ""    # ~B
for i in range(len(a)):
    if a[i] == "1" and b[i] == "1":
        aandb += "1"
    else:
        aandb += "0"
    
    if a[i] == "0" and b[i] == "0":
        aorb += "0"
    else:
        aorb += "1"
        
    if a[i] == b[i]:
        ab += "0"
    else:
        ab += "1"
        
    if a[i] == "1":
        nota += "0"
    else:
        nota += "1"
        
    if b[i] == "1":
        notb += "0"
    else:
        notb += "1"
    
print(aandb)
print(aorb)
print(ab)
print(nota)
print(notb)