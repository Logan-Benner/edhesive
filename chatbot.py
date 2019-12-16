# your code goes here
import random
name = (input("What is your name? "))
print ("\n"+ name +"")
print()
print ("Hi there "+name+", nice to meet you.")
help = (input("Do you need anything? "))
print("ok")
help = (input("Do you need anything? "))
print("ok")
help = (input("Do you need anything? "))
print("ok")
age = (input("How old are you? "))
print("\n"+ age +"")
if (age == age):
    print (str(age)+" is a good age")
    print ("You are old enough to drive.")
    feeling = input("So, "+name+" how are you today? ")
    if (feeling == feeling):
        choice = random.randint(1,3)
        if(choice==1):
            print ("That is great to hear.")
        elif(choice == 2):
            print ("So interesting.")
        elif(choice == 3):
            print ("Great you are happy now.")
        else:
        	print("ok")
    elif(feeling == "sad"):
        choice = random.randint(1,3)
        if(choice == 1):
            print ("That is not great to hear.")
        elif(choice == 2):
            print ("Not so interesting.")
        elif(choice == 3):
            print ("Sad that you are unhappy")
        else:
        	print("understood")
