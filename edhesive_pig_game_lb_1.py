import random

def main():
	hscore = 0
	cscore = 0
	rounds = 0
	
	while (humanscore < 100 and computerscore < 100):
		print("Round" + str(rounds))
		hscore = dice_roll()
		cscore = dice_roll()
		print("human Roll: " + str(hscore))
		print("computer  Roll: " + str(hscore))
		
		rounds = rounds + 1

def dice_roll():
	diceRoll = random.randit(1,6)
	return diceRoll
	
