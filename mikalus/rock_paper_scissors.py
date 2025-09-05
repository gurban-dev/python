"""
EXERCISE: ROCK, PAPER, SCISSORS

Rock, paper, scissors is a popular hand game for two players. 
The two players simultaneously choose one of the three possible
moves and determine the winner of the game: 
rock beats scissors, paper beats rock, and scissors beats paper.
 
This exercise involves determining a game's outcome given the
moves of the two players.

Write a function called 'rpsWinner()' with 2 parameters: player1 and player2. 
These parameters are passed as one of the strings 'rock', 'paper', or
'scissors' representing the first and second player's move. 

If this results in player 1 winning, the function returns 'player one'. 
If this results in player 2 winning, the function returns 'player two'. 
Otherwise, the function returns 'tie'.

"""

def rpsWinner(player1, player2):
	if player1 == player2:
		return 'tie'
	elif (player1 == "scissors" and player2 == "paper") or \
			 (player1 == "paper" and player2 == "rock") or \
			 (player1 == "rock" and player2 == "scissor"):
		return 'player one'
	return 'player two'

print('rpsWinner("scissors", "paper"):', rpsWinner("scissors", "paper"))
print('rpsWinner("scissors", "scissors"):', rpsWinner("scissors", "scissors"))