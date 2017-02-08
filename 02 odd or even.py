number = input("What is your number?")
number=int(number)

if(number%2==1):
  print("{} is odd".format(number))
  
else:
  print("{} is even".format(number))
  
if(number%4==0):
  print("{} is a multiple of 4\n".format(number))
  
else:
  print("{} isn't a multiple of 4\n".format(number))

  
multiple = input("Give multiple")
multiple = int(multiple)

factor = input("Give factor")
factor = int(factor)
#print()
def check_factor(mult,fact):
  x=int(mult)
  y=int(fact)
  if(x%y==0):
    print("{} is a multiple of {}".format(x,y))
  else:
    print("{} isn't a multiple of {}".format(x,y))
    
check_factor(multiple,factor)