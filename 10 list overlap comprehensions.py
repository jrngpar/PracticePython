import random

def get_int():
    length = int(input())
    return length

ls_A = []
ls_B = []

#length = 5
print("Length listA?")
length1 = get_int()
print("\nLength of listB?")
length2 = get_int()

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
