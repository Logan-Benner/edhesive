import random

def main():
	cscore = 0
	hscore = 0
	rounds = 1
	
players = ['human', 'computer']
random.shuffle(players)
points = {'human': 0, 'computer': 0}
	
	
	while True:
		for i in players:
			if i == 'human':
				hscore = 0
				cscore = 0
				rounds = 1
			while (hscore < 100 and cscore < 100):
					print("Round " + str(rounds))
					hscore = dice_roll()
					cscore = dice_roll()
					r = dice_roll
					choice = input("You are human, Roll (r)")
					if (choice=='r'):
						while (rounds < 100):
							if (rounds == 1):
								hscore = 0
								print("Rolled a", diceRoll)
								print("Greedy piggy!")
							else:
								print("Not an input")
					
								break
			
								if (hscore == cscore):
									print("Draw!")
								elif hscore > cscore:
									print("Human wins!")
								else:
									print("Computer wins!")
					else:
		
					rounds = rounds + 1

def dice_roll():
	diceRoll = random.randint(1,6)
	return diceRoll
	
main()
