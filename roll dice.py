#simulate some dice
#how many rolls?
#how many sides on the dice?
#want to roll again?

import random

def get_sides():
	sides = int(input("How many sides: "))
	return sides
	
def get_rolls():
	rolls = int(input("How many rolls: "))
	return (rolls)
	
def main(sides, rolls):
	side_number = 1
	my_die = []

	for x in range(sides):
		my_die.append(side_number)
		side_number += 1

	my_rolls = [my_die[random.randint(0,sides-1)] for n in range(rolls)]
	
	print ("You rolled the following:\n")
	print(my_rolls)
	
main(get_sides(),get_rolls())
