#new project!
import random

rand_list = []

user_length = input("List length?: ")

print(user_length)

for x in range(0,int(user_length)):
	rand_list.append(random.randint(0 ,100))

print(rand_list)

#rand_list

# my_list = [1,2,4,5,76,4,2,0]

# new_list = []

# new_list.append(rand_list[0])
# rand_list.reverse()
# new_list.append(rand_list[0])
# print(new_list)

def get_firstandlast(in_list):
	a = in_list
	new_list=[]
	new_list.append(a[0])
	reverse=a[::-1]
	new_list.append(reverse[0])
	return new_list

print(get_firstandlast(rand_list))