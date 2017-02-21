#other tries for rock paper scissors

def game():
	player_moves=[]
	for a in [0,1]:
		try1=input("P1 rock(1), paper(2), or scissors(3)")
		player_moves.append(try1)
	#print(player_moves)

	play1 = player_moves[0]
	play2 = player_moves[1]
	print(play1)
	print(play2)

	#tries
	#p1=rock
	#0=tie -1=lose -2=win
	#p1=paper
	#0=tie 



game()