def check_if_divisor(user_in):
  x = user_in
  divisors =[]
  my_range = range(1,x+1)
  for element in my_range:
    if(x%element==0):
      divisors.append(element)
  print(divisors)
      
my_input = input("# you want divisors for?")
my_input = int(my_input)
check_if_divisor(my_input)