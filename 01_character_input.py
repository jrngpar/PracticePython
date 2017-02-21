
import time
import datetime
#name = input("What is your name? ")

age = input("How old are you in years? ")
age = int(age)

now = datetime.datetime.now()
#print("Current year: %d"%now.year)
print()
print("Current year: {:}".format(now.year))
print()
print("You are {:}".format(age))
#print("{:_>5}".format("test"))

years_to_hundred = 100-age
year_at_hundred = years_to_hundred + now.year
print()
def print_time():
	print("It will be {} years until you are 100 in the year {}\n".format(years_to_hundred,year_at_hundred))
print_time()


repeat = input("How many times do you want to hear it?\n")
repeat=int(repeat)

while(repeat>=1):
	print_time()
	repeat=repeat-1
