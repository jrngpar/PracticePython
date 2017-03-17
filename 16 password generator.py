#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

#Extra:

#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

#use random numbers. If random number is in a range, create one digit out of a specific set of characters(numbers, letters, symbols)
#ask user for password length and loop to make that length
import random, string

# def get_parameters():
#     generator_input = input("Want to make a password?\nEnter 'quit' to quit: ")
#     main(get_length())
                    
    
def gen_symbol():
    symbol_list = ["!","@","%","^","&","/","(",")",":","~",";"]
    rand_symbol = random.choice(symbol_list)
    return (rand_symbol)
    
    
def get_length():
    pass_length = input("How many characters:")
    return int(pass_length)

def gen_rand_number():
	rand_num = string.digits
	return (random.choice(rand_num))

def gen_rand_letter():
	rand_digit = string.ascii_letters
	return (random.choice(rand_digit))

#print(gen_rand_number())
def main(length):
    password = []
    generator_input = input("How strong?\n(1)Strong\n(2)Average\n(3)Weak\n")
    if generator_input == "1":
        for x in range(0,length):
            digit = random.randint(1,4)
            if digit == 1:
                password.append(gen_symbol())
            elif digit ==3:
                password.append(gen_rand_number())
            else:
                password.append(gen_rand_letter())
    elif generator_input == "2":
        for x in range(0,length):
            digit = random.randint(1,3)
            if digit == 1:
                password.append(gen_rand_number())
            else:
                password.append(gen_rand_letter())
        #print("average")
    elif generator_input == "3":
        for x in range(0,length):
            password.append(gen_rand_letter())
        #print("weak")
    else:
        print("Please enter a valid selection")
        get_strength()
    print("".join(password))

main(get_length())

    