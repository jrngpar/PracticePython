import random

number = random.randint(1,9)
print(number)

guess = input("Guess the number from 1-9:")
guess = int(guess)
print(guess)

if number==guess:
  print("Same")
  
if number<guess:
  print("Guess is larger")
  
if number>guess:
  print("Guess is smaller")
