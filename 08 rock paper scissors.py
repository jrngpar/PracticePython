# #Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# x=5
# while (x>0):
# 	print(x)
# 	x=x-1
#2 players, rock, paper, scissors. Ask both players if they want to continue.

def rps():
	player1=input("Player 1 choose rock, paper, or scissors:")
	while player1!="rock" and player1!="paper" and player1!="scissors":
		player1=input("Player 1 please choose rock, paper, or scissors:")

	player2=input("Player 2 choose rock, paper, or scissors:")
	while player2!="rock" and player2!="paper" and player2!="scissors":
		player2=input("Player 2 please choose rock, paper, or scissors:")

	#print(player1)



	while player1=="rock":
		if player2=="rock":
			print("\nTie")
			break
		elif player2=="paper":
			print("\nP2 wins")
			break
		else:
			print("\nP1 wins")
			break
	while player1=="paper":
		if player2=="rock":
			print("\nP1 wins")
			break
		elif player2=="paper":
			print("\nTie")
			break
		else:
			print("\nP2 wins")
			break
	while player1=="scissors":
		if player2=="rock":
			print("\nP2 wins")
			break
		elif player2=="paper":
			print("\nP1 wins")
			break
		else:
			print("\nTie")
			break
	
	quit = input("Do you want to play again? Yes or no:")
	while quit == "yes":
		rps()

rps()