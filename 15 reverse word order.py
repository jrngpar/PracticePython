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

print(reverse_words(get_sentence()))
