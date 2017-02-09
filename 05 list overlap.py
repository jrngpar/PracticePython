import random

length_A = input("Length of 1st list:")
length_B = input("Length of 2nd list:")

length_A = int(length_A)
length_B = int(length_B)

list_A = []
list_B = []

#print(length_A)
#print(length_B)

for x in range(0,length_A):
    list_A.append(random.randint(0,99))
    
for x in range(0,length_B):
    list_B.append(random.randint(0,99))
  
print(list_A)
print(list_B)
