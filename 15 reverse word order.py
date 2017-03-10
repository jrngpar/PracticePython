#reverse word order
#ask for a long string with multiple words
#print it back with the words in backwards order

#remove spaces? Maybe print back with words in reverse
#2 functions, one to reverse order of words, one to reverse letters in words?
#Can call both functions to reverse order and letters if wanted

def reverse_words(sentence_in):
	swapped = sentence_in.split(" ")
	swapped = " ".join(reversed(swapped))
	return swapped

def get_sentence():
	user_sentence = input("What would you like reversed:\n")
	return user_sentence

#print(reverse_words(get_sentence()))

def reverse_sentence(s):
	backwards = s[::-1]
	return backwards
	
#print(reverse_sentence(get_sentence()))

def other_reverse(s):
  backwards = "".join(reversed(s))
  return backwards

def sentence_editor():
	user_sentence = input("Would you like to edit a sentence or quit(type 'quit')?")
	while user_sentence != "quit":
		my_sentence = input("Enter your sentence:")
		which_mod = input("Reverse words(1)\nReverse letters in words(2)\nReverse entire sentence(3)\n")
		if which_mod == "1":
			print(reverse_words(my_sentence))
			break
		elif which_mod =="2":
			print(reverse_words(other_reverse(my_sentence)))
			break
		else:
			print(reverse_sentence(my_sentence))
			break
			
sentence_editor()
