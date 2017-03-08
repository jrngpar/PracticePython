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

def remove_dup_with_loop(input_list):
	no_duplicates = []
	for x in range(0,len(input_list)):
		#print("it printed")
		if input_list[x] not in no_duplicates:
			no_duplicates.append(input_list[x])
	return no_duplicates

def remove_dup_with_set(in_list):
	make_set = set(in_list)
	return make_set

#print (check_list)


#print (remove_dup_with_loop(check_list))

def which_sort(in_list):
	check_list = in_list
	#print(check_list)
	pick = input("How would you like to sort: Loop(1) or Set(2):")

	if pick == "1":
		print(check_list)
		print (remove_dup_with_loop(check_list))
	elif pick =="2":
		print(check_list)
		print (remove_dup_with_set(check_list))
	elif pick =="exit":
		print ()
	else:
		print ("Not a valid choice. please try again or type 'exit' to exit")
		which_sort(check_list)

check_list = create_list(get_list_len())
which_sort(check_list)