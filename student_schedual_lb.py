# your code goes here
'''
Assingment 4: Student Schedule
In this assignment you will draw a student schedule by using a while loop. 
You will ask the user for their first and last names, 
and then a list of their classes and room numbers.
The loop should stop when they enter STOP for their next class.
'''
fn = input("What is your first name? ")
ln = input("What is your last name? ")
id = int(input("Student ID: "))
longL = "*************************************************" 
openL = "*                                               *" 
print(longL)  
print(openL)
print("*\t" + ln + ", " + fn+ "\t\tID: " + str(id) + "\t*")
print(openL)
print(longL)  
print(openL)
sub = " "
room = 0
c = 1
while (sub != "STOP" ):
	sub = input ("Enter the next class, STOP to end: ")
	if (sub != "STOP"):
		room = int(input("Enter the room number: "))
		print("*\tBlock " + str(c) + ": " + sub + "\tRoom: " + str(room) +" \t*")
		c = c + 1
print(openL)
print(longL)  
print(openL)
print(longL)  
