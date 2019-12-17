#Official Pig Game
#Pig Set Variables
'''
This code will need to be changed for originality
'''
import random
humanscore = 0
computerscore = 0
#While hscore or hscore turn is less (<) than 100
while (humanscore < 100 and computerscore < 100):
	#Roll and display
	humanRound = 0
	rollagain = "R"
	roll = 2
	
	#human turn
	humanturns = 0
	while (roll !=1 and rollagain == "R"):
		roll = random.randint(1,6)
		#print roll
		if (roll != 1):
			humanturns = humanturns + roll
			message = ("You rolled a " + str(roll) + "\n\nEnter R to roll again\n\nYour turn is: ")
			message = message + str(humanturns) + "\nYour score is: " + str(humanscore)
			message = message + " Computer score is: " + str(computerscore)
			
			rollagain = input(message)
			if (rollagain == "R"):
				humanscore = humanscore + humanturns
				humanturns = 0
				
	#computers turn			
	computerturns = 0
	#computers score
	crollagain = 2
	roll = 9
	
	# computer does not roll a 1 and therefore may roll again
	while (roll != 1 and crollagain == 2):
		roll = random.randint(1,6)
		print("Computer rolled: " + str(roll))
    
		# anthing but 1 will add points
		if (roll != 1):
			computerturns = computerturns + roll
      
			# The computer will decide whether to roll again
			# When crollagain == 1 it will hold
			crollagain = random.randint(1,2)
			if (crollagain == 1):
				computerscore = computerscore + computerturns
				computerturns = 0 
				print ("Computer ends turn.")
			else: 
				# such means that the computer will hold
				print("Computer rolls again.")
      
# outside of main > 100 while loop
# someone scored 100, so print complete results
print("Computer Score: " + str(computerscore))
print("PLayer's Score: " + str(humanscore))
	
		

