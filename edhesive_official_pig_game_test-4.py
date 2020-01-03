import random

def dice_roll():
	dice_roll = random.randint(1, 6)
	return dice_roll

humanroll = 0
computerroll = 0
rounds = 1
humansturn = "A"
computersturn = "B"
humanwin = 0
computerwin = 0
humanwins = 0
computerwins = 0
	
while True:
	while (humanwins < 100 and computerwins < 100):
		while (humanwins < 100 and computerwins < 100):
			choice = input("You are human. Click 'r' to roll and h to hold if you want to gamble: ")
			if (choice=='r'):
				print("Round " + str(rounds))
				humanroll = dice_roll()
				computerroll = dice_roll()
				humanwin = humanwins
				computerwin = computerwins
				print("Human rolls a " + str(humanroll))
				print("Computer rolls a " + str(computerroll))
	
				if humanroll != 1 and humanroll < 7 and humanroll > computerroll and computerroll != 1: 
					humanwins = humanwins + humanroll
					rounds = rounds + 1
					print("You Win The Round!!! With a total of " + str(humanwins) + " points.")				
				elif computerroll != 1 and computerroll < 7 and humanroll < computerroll and humanroll != 1:
					computerwins = computerwins + computerroll 
					rounds = rounds + 1
					print("Computer Wins The Round!!! With a total of " + str(computerwins)+ " points.")
				elif humanroll == 1:
					humanwins = 0
					computerwins = computerwins + 20
					computerwins = computerwins + computerroll
					rounds = rounds + 1
					print("Greedy Human Pig! Your slop now belongs to the computer. Your score is now " + str(humanwins) + ", Enjoy!")
					print("The computer gets a twenty point boost. The computer's score is now " + str(computerwins) + " points.")
				elif computerroll == 1:
					computerwins = 0
					humanwins = humanwins + 20
					humanwins = humanwins + humanroll
					rounds = rounds + 1
					print("What A Greedy Computer! The computers slops belong to you now. The computer's score is now " + str(computerwins) + ", it would feel sorrow if it had emotions.")
					print("You get a twenty point boost. Your score is now " + str(humanwins) + " points. Perhaps you deserve this.")
				elif computerroll == 1 and humanroll == 1:
					print("A Lucky Draw!!! Neither of you will be punished or rewarded.")
				else:
					print("Draw!!! No points for the human or computer.")
			if (choice=='h'):
				print("Round " + str(rounds))
				humanroll = 0
				computerroll = dice_roll()
				humanwin = humanwins
				computerwin = computerwins
				print("The human holds it's turn " + str(humanroll))
				print("Computer rolls a " + str(computerroll))
	
				if humanroll != 1 and humanroll < 7 and humanroll > computerroll and computerroll != 1: 
					humanwins = humanwins + humanroll
					rounds = rounds + 1
					print("You Win The Round!!! With a total of " + str(humanwins) + " points.")				
				elif computerroll != 1 and computerroll < 7 and humanroll < computerroll and humanroll != 1:
					computerwins = computerwins + computerroll 
					rounds = rounds + 1
					print("Computer Wins The Round!!! With a total of " + str(computerwins)+ " points.")
				elif humanroll == 1:
					humanwins = 0
					computerwins = computerwins + 20
					computerwins = computerwins + computerroll
					rounds = rounds + 1
					print("Greedy Human Pig! Your slop now belongs to the computer. Your score is now " + str(humanwins) + ", Enjoy!")
					print("The computer gets a twenty point boost. The computer's score is now " + str(computerwins) + " points.")
				elif computerroll == 1:
					computerwins = 0
					humanwins = humanwins + 20
					humanwins = humanwins + humanroll
					rounds = rounds + 1
					print("What A Greedy Computer! The computers slops belong to you now. The computer's score is now " + str(computerwins) + ", it would feel sorrow if it had emotions.")
					print("You get a twenty point boost. Your score is now " + str(humanwins) + " points. Perhaps you deserve this.")
				elif computerroll == 1 and humanroll == 0:
					humanwins == humanwins + 20
					rounds = rounds + 1
					compterroll = computerroll - 20
					print("What an impatient computer. To the patient human goes the spoils. You recieve " + str(humanwins) + " points. Good patient Piggy.")
				elif computerroll == 6 and humanroll == 0:
					computerwins = computerwins + 50
					humanwins = humanwins - 50
					rounds = rounds + 1
					print("Early bird get the worm. In this case against all odds the computer piggy traveled forward in time and ate all of your slop. You do not want to see the results on this one.")
				elif computerroll == 1 and humanroll == 1:
					print("A Lucky Draw!!! Neither of you will be punished or rewarded.")
				else:
					print("Draw!!! No points for the human or computer.")
		if humanwins > computerwins:
			print("The human wins the game!!!")
			print("Computers Final Score: " + str(computerwins))
			print("Humans Final Score: " + str(humanwins))
		elif humanwins < computerwins:
			print("Computer wins the game!!!")
			print("Computers Final Score: " + str(computerwins))
			print("Humans Final Score: " + str(humanwins))
		elif humanwins == computerwins:
			print("It is a complete draw!!!")
			print("Computers Final Score: " + str(computerwins))
			print("Humans Final Score: " + str(humanwins))
		elif humanwins == 0 and humanwins < computerwins:
			print("You were dominated by a pile of circuits")
		elif computerwins == 0 and humanwins > computerwins:
			print("You enjoy bullying machines eh?")
		
	if humanwins < 100 and computerwins < 100:
		break	



