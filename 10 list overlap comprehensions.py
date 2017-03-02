import random

ls_A = []
ls_B = []

#length = 5
length1 = input("How long for list 1?\n")
length1 = int(length1)
length2 = input("list 2?\n")
length2 = int(length2)

for i in range(length1):
    ls_A.append(random.randint(0,9))
    
print (ls_A)

for i in range(length2):
    ls_B.append(random.randint(0,9))
    
print (ls_B)

common = []
common = [x for x in ls_A if x in ls_B and x not in common]
print(common)
common = set(common)
print(common)
