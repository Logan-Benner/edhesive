import turtle
import math
import random
#global variable(s)
#define global variables here
#example:  xM = 0 

def drawing(t):
	#change global variables
        # example :  global xM = 200
     # add your code here
     t.color = ("#eb4034")
     t.setposition(0,0)
     t.setposition(0,50)

	def main():
		try:
			turtle.TurtleScreen._RUNNING = True
			turtle.screensize(canvwidth=700, canvheight=700, bg=None)
			print(turtle.Screen().screensize())
			w = turtle.Screen()
			drawing(t)
			w.exitonclick()
		finally:
			turtle.Terminator()
	
if __name__ == '__main__':
		main()
