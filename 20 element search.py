import random

def generate_list():
	length = int(input("Length of list: "))
	rand_list = []
	for x in range(length):
		rand_list.append(random.randint(0,99))
	return(sorted(rand_list))


def binary_search(search_num, my_list):

	first = 0
	last = len(my_list) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last)//2
		if my_list[midpoint] == search_num:
			found = True
		else:
			if search_num < my_list[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1

	return found


def main():

	the_list = generate_list()
	print(the_list)
	my_num = int(input("What 2 digit number should I search for:"))
	print(binary_search(my_num,the_list))

main()
