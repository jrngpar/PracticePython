#removes duplicates
#check with a loop and also check with a set transformation
#check user input, ask how to sort
import random


def get_list_len():
	length = input("List length: ")
	return int(length)

def create_list(list_length):
	my_list = []
	for x in range(0,list_length):
		my_list.append(random.randint(0,100))
	return my_list

check_list = create_list(get_list_len())

def remove_dup_with_loop(input_list):
	no_duplicates = input_list
	for x in range(0,len(input_list)):
		print("it printed")
	return no_duplicates

def remove_dup_with_set(in_list):
	make_set = set(in_list)
	return make_set

print (check_list)
print (remove_dup_with_set(check_list))

print (remove_dup_with_loop(check_list))