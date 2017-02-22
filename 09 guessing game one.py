import random

guess=-1
number = random.randint(1,9)
#print(number)
num_guess=0
def get_guess():
	global guess
	guess = input("Guess the number from 1-9:")
	guess = int(guess)
	print(guess)

def checker():
	global num_guess
	if number==guess:
		print("Good guess")
		num_guess += 1
		print("It took you {} guesses to get the right answer!num_guess)


	if number<guess:
		print("Guess is larger\nTry again")
		num_guess +=1
		get_guess()
		checker()
		
  
	if number>guess:
		print("Guess is smaller\nTry again")
		num_guess+=1
		get_guess()
		checker()
		

get_guess()
checker()
