a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
out = []
user_in = input("<= what")
user_in = int(user_in)
for element in a:
	if(element<=user_in):
		out.append(element)

print(out)
