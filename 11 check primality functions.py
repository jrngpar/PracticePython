def get_int():
    return int(input("Enter number to check if prime:\n"))

am_i_prime = get_int()

def check_divisors(my_int):
    my_num=my_int
    my_range=(1,my_int+1)
    for x in my_range:
        if (my_num%x==0):
            print("Number isn't prime")
            break
        else:
            print("Prime")
        
check_divisors(am_i_prime)

#need to exclude 1 and the number
