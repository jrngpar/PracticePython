#Fibonacci calculator
#get input of how many to calculate, then list all of them

def get_input():
	a = input("How many Fibonacci numbers do you want: ")
	return int(a)

def calc_fibs(how_many):
	fib_numbers = [1]
	for x in range(0,how_many):
		fib_numbers.append(1)

	return fib_numbers

# fib_numbers = [1]

# #next = n + n-1

# n = 0
# first_before = fib_numbers[n]
# second_before = fib_numbers[n-1]
# print(first_before)
# print(second_before)
# print(first_before+second_before)

# for x in range (0,user_in):



#return fib_numbers
get_fibs = get_input()
print(calc_fibs(get_fibs))