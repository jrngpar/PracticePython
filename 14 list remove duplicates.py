#removes duplicates
import random


def get_list_len():
	length = input("List length: ")
	return int(length)

def create_list(list_length):
	my_list = []
	for x in range(0,list_length):
		my_list.append(random.randint(0,100))
	return my_list

print(create_list(get_list_len()))