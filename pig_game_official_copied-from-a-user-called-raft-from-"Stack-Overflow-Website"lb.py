import random
def roll_dice():
    return random.randint(1,6)
#Global variables
pigs = ['human', 'computer'] #list reasearch
random.shuffle(pigs)
points = {'human': 0, 'computer': 0} #list dictionary
'''
A while loop that proceeds with the first turn for the Ai and assigns variables such as the input choices and dice_value/roll_dice/dice_value. Such allows the game to know when to end and as to what the 6
random dice roles mean.
'''
while True:
    for i in pigs:
        if i == 'human':
            choice = input("You are pig 1, Roll(r) or Hold(h)?: ")
            turn_score = 0
            final_score = 0
            if (choice=='r'):
                while(turn_score<=5):
                    dice_value = roll_dice()
                    turn_score += dice_value
                    if (dice_value==1):
                        turn_score = 0
                        print("-rolled a ",dice_value)
                        print("Greedy Pig!")
                        break
                    print("Turn score is: ",turn_score)
                    final_score += turn_score
                    print("Your final score is: ",final_score)
                    if (final_score>100):
                        break
#This allows the second player to commence their turn and so forth until one of them has reached the final score
        else:
            turn_score=0
            print("It is " +  str(i) + "'s turn.")
            while(turn_score<5):
                dice_value = roll_dice()
                if (dice_value==1):
                    turn_score = 0
                    points[i] +=0
                    print("- rolled a ",dice_value)
                    print("Greedy Pig!")
                    break
                else:
                    turn_score+=dice_value
                    print("-rolled a ",dice_value)
        points[i] += turn_score
        print("Turn score is: ",turn_score)
        print('{} score: {} {} score: {}'.format(pigs[0], points[pigs[0]], pigs[1], points[pigs[1]]))
        if points[i]>100:
            break
    if points[i]>100:
        break
#Prints the victor with the score and statistics such as number of players with a final comment
victor = [victor for victor in points if points[victor] == max(points.values())]
print(str(victor) + " is the victor!")
