#My Official python turtle project--------------
#Old imports
import turtle
import math 
import random
#New imports
#Global Variables----------
#Old variables
width = 800; height = 8000; bgstring = ("#ffe2ca")
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"
#New Variables
screen = turtle.Screen()
t = turtle.Turtle() #Hello World
n = turtle.Turtle() #Hello World_2
r = turtle.Turtle() #border_line_
d = turtle.Turtle() #border_line_2
o = turtle.Turtle() #border_line_3
g = turtle.Turtle() #border_line_4
l = turtle.Turtle() #border_line_5
h = turtle.Turtle() #border_line_6
s = turtle.Turtle() #border_line_7
b = turtle.Turtle() #border_line_8
q = turtle.Turtle() #polygon_1
w = turtle.Turtle() #polygon_2
e = turtle.Turtle() #polygon_3
y = turtle.Turtle() #polygon_4
u = turtle.Turtle() #polygon_5
p = turtle.Turtle() #circle_1
x = turtle.Turtle() #circle_2
v = turtle.Turtle() #circle_3
m = turtle.Turtle() #circle_4
k = turtle.Turtle() #circle_5 
n.hideturtle()
t.hideturtle()
#t.hideturtle()
t.width(5)
n.width(5)
d.width(5)
r.width(5)
o.width(5)
g.width(5)
l.width(5)
h.width(5)
s.width(5)
b.width(5)
t.speed(40)
n.speed(40)
r.speed(1000)
d.speed(1000)
o.speed(1000)
g.speed(1000)
l.speed(1000)
n.speed(1000)
s.speed(1000)
b.speed(1000)
q.speed(40)
q.width(5)
w.width(5)
e.width(5)
y.width(5)
u.width(5)
p.width(5)
x.width(5)
v.width(5)
m.width(5)
k.width(5)
#uDef objects----------
def hello_world() :
	t.color("#000000")
	t.penup()
	t.goto(-100,0)
	t.pendown()
	#The H
	t.left(90)
	t.forward(50)
	t.right(180)
	t.forward(25)
	t.left(90)
	t.forward(25)
	t.right(90)
	t.forward(25)
	t.right(180)
	t.forward(50)
	t.right(180)	
	t.forward(25)
	t.left(90)
	t.penup()
	t.forward(10)
	t.pendown()
	#The e
	t.forward(25)
	t.left(90)
	t.circle(15, 90)
	t.circle(14, 90)
	t.circle(18, 90)
	t.left(90) 
	t.penup()
	t.forward(17.5)
	t.pendown()
	t.right(90)
	t.forward(15)
	t.penup()
	t.forward(1)
	t.pendown()
	#The L
	t.left(90)
	t.forward(25)
	t.right(180)
	t.forward(50)
	t.left(90)
	t.forward(23)
	t.penup()
	t.forward(5)
	t.pendown()
	#The L
	t.left(90)
	t.forward(50)
	t.right(180)
	t.forward(50)
	t.left(90)
	t.forward(23)
	t.penup()
	#The o
	t.left(90)
	t.forward(7)
	t.right(90)
	t.forward(10)
	t.pendown()
	t.circle(16, -85)
	t.circle(16, -85)
	t.circle(16, -85)
	t.circle(16, -85)
	t.circle(16, -85)
	r.penup()
	#The red marking
	n.color("#f86156")
	n.penup()
	n.left(90)
	n.forward(23)
	n.right(90)
	n.forward(9)
	n.pendown()
	n.forward(18)
	n.right(90)
	n.forward(15)
	n.left(180)
	n.forward(30)
	n.right(180)
	n.forward(15)
	n.left(90)
	n.forward(15)
	n.penup()
	n.forward(20)
	#The W
	n.color("#000000")
	n.left(90)
	n.forward(26)
	n.pendown()
	n.right(170)
	n.forward(52)
	n.right(10)
	n.left(170)
	n.forward(52)
	n.left(10)
	n.right(170)
	n.forward(52)
	n.right(10)
	n.left(170)
	n.forward(52)
	n.left(10)
	n.penup()
	#The o
	n.right(90)
	n.forward(8)
	n.right(90)
	n.forward(27)
	n.pendown()
	n.circle(16, 85)
	n.circle(16, 85)
	n.circle(16, 85)
	n.circle(16, 85)
	n.circle(16, 85)
	n.left(24)
	#the r
	n.penup()	
	n.forward(35)
	n.left(90)
	n.pendown()
	n.forward(30)
	n.right(180)
	n.forward(41)
	n.left(180)
	n.forward(34)
	n.right(240)
	n.circle(18, -85)
	n.right(34)
	n.right(90)
	n.penup()
	#The l
	n.forward(5)
	n.left(90)
	n.pendown()
	n.forward(23)
	n.right(180)
	n.forward(49)
	n.right(180)
	n.forward(24.5)
	n.right(90)
	n.penup()
	#The d
	n.forward(30)
	n.left(90)
	n.pendown()
	n.forward(24)
	n.right(180)
	n.forward(50)
	n.right(270)
	n.circle(15, -90)
	n.circle(15, -90)
	
def border_line() :
	r.color("#f86156")
	r.penup()
	r.left(90)
	r.forward(24)
	r.right(90)
	r.forward(26)
	r.left(90)
	r.forward(200)
	r.left(115) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		r.forward(a)
		a = a + 1
		r.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				r.forward(5)
				r.right(10)
				r.pendown()
				r.color("#f86156")
			for i in range(5):
				r.forward(5)
				r.left(10)
				r.pendown()
				r.color("#FEF24E")
			for i in range(5):
				r.forward(5)
				r.right(10)
				r.pendown()
				r.color("#AD07B9")
			for i in range(5):
				r.forward(5)
				r.left(10)
				r.pendown()
				r.color("#f86156")
				
def border_line_2() :
	d.penup()
	d.left(90)
	d.forward(24)
	d.right(90)
	d.forward(26)
	d.left(90)
	d.forward(200)
	d.right(65) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		d.forward(a)
		a = a + 1
		d.pendown()
		for i in range(3): #The more number numbers the more wiggle
			for i in range(5):
				d.forward(5)
				d.right(10)
				d.pendown()
				d.color("#FF0092")
			for i in range(5):
				d.forward(5)
				d.left(10)
				d.pendown()
				d.color("#FDA50F")
			for i in range(5):
				d.forward(5)
				d.right(10)
				d.pendown()
				d.color("#0036AD")
			for i in range(5):
				d.forward(5)
				d.left(10)
				d.pendown()
				d.color("#B3E885")
				
def border_line_3() :
	o.color("#f86156")
	o.penup()
	o.right(90)
	o.forward(24)
	o.left(90)
	o.forward(26)
	o.right(90)
	o.forward(200)
	o.left(115) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		o.forward(a)
		a = a + 1
		o.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				o.forward(5)
				o.right(10)
				o.pendown()
				o.color("#80ffbf")
			for i in range(5):
				o.forward(5)
				o.left(10)
				o.pendown()
				o.color("#ff99cc")
			for i in range(5):
				o.forward(5)
				o.right(10)
				o.pendown()
				o.color("#ffff66")
			for i in range(5):
				o.forward(5)
				o.left(10)
				o.pendown()
				o.color("#ccff99")
				
				
def border_line_4() :
	g.color("#f86156")
	g.penup()
	g.right(90)
	g.forward(24)
	g.left(90)
	g.forward(26)
	g.right(90)
	g.forward(200)
	g.right(65) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		g.forward(a)
		a = a + 1
		g.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				g.forward(5)
				g.right(10)
				g.pendown()
				g.color("#2e3338")
			for i in range(5):
				g.forward(5)
				g.left(10)
				g.pendown()
				g.color("#45174f")
			for i in range(5):
				g.forward(5)
				g.right(10)
				g.pendown()
				g.color("#4c4c4c")
			for i in range(5):
				g.forward(5)
				g.left(10)
				g.pendown()
				g.color("#8000b2")
				
				
				
def border_line_5() :
	l.color("#f86156")
	l.penup()
	l.right(180)
	l.forward(24)
	l.left(90)
	l.forward(26)
	l.right(90)
	l.forward(200)
	l.left(115) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		l.forward(a)
		a = a + 1
		l.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				l.forward(5)
				l.right(10)
				l.pendown()
				l.color("#e08f4c")
			for i in range(5):
				l.forward(5)
				l.left(10)
				l.pendown()
				l.color("#1ae6b2")
			for i in range(5):
				l.forward(5)
				l.right(10)
				l.pendown()
				l.color("#ff99a3")
			for i in range(5):
				l.forward(5)
				l.left(10)
				l.pendown()
				l.color("#e8d1ab")
				
			
def border_line_6() :
	h.color("#f86156")
	h.penup()
	h.right(180)
	h.forward(24)
	h.left(90)
	h.forward(26)
	h.right(90)
	h.forward(200)
	h.right(65) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		h.forward(a)
		a = a + 1
		h.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				h.forward(5)
				h.right(10)
				h.pendown()
				h.color("#8c9f9f")
			for i in range(5):
				h.forward(5)
				h.left(10)
				h.pendown()
				h.color("#ab5cff")
			for i in range(5):
				h.forward(5)
				h.right(10)
				h.pendown()
				h.color("#e099c2")
			for i in range(5):
				h.forward(5)
				h.left(10)
				h.pendown()
				h.color("#6699c2")
#These two are uneeded				
'''
def border_line_7() :
	s.color("#f86156")
	s.penup()
	s.right(90)
	s.forward(24)
	s.left(90)
	s.forward(26)
	s.right(90)
	s.forward(200)
	s.left(115) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		s.forward(a)
		a = a + 1
		s.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				s.forward(5)
				s.right(10)
				s.pendown()
				s.color("#f86156")
			for i in range(5):
				s.forward(5)
				s.left(10)
				s.pendown()
				s.color("#FEF24E")
			for i in range(5):
				s.forward(5)
				s.right(10)
				s.pendown()
				s.color("#AD07B9")
			for i in range(5):
				s.forward(5)
				s.left(10)
				s.pendown()
				s.color("#f86156")

def border_line_8() :
	b.color("#f86156")
	b.penup()
	b.right(90)
	b.forward(24)
	b.left(90)
	b.forward(26)
	b.right(90)
	b.forward(200)
	b.left(115) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 3 :
		b.forward(a)
		a = a + 1
		b.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				b.forward(5)
				b.right(10)
				b.pendown()
				b.color("#f86156")
			for i in range(5):
				b.forward(5)
				b.left(10)
				b.pendown()
				b.color("#FEF24E")
			for i in range(5):
				b.forward(5)
				b.right(10)
				b.pendown()
				b.color("#AD07B9")
			for i in range(5):
				b.forward(5)
				b.left(10)
				b.pendown()
				b.color("#f86156")
				'''
#11 sides and 35 length is correct		
def polygon_1() :
	q.penup()
	q.color("#a6a6a6")
	q.right(180)
	q.forward(425)
	q.pendown()
	q.right(90)
	q.forward(130)
	q.color("#00ff00")
	#numberOfSides = int(input('Enter the number of sides of a polygon: '))
	#lengthOfSide = int(input('Enter the length of a side of a polygon: '))
	numberOfSides = int(11)
	lengthOfSide = int(35)
	exteriorAngle = 360/numberOfSides
	for i in range(numberOfSides):
		q.forward(lengthOfSide)
		q.right(exteriorAngle)


def polygon_2() :
	q.penup()
	q.color("#a6a6a6")
	q.pendown()
	q.right(180)
	q.forward(110)
	q.right(180)
	q.color("#ffff00")
	#numberOfSides = int(input('Enter the number of sides of a polygon: '))
	#lengthOfSide = int(input('Enter the length of a side of a polygon: '))
	numberOfSides = int(9)
	lengthOfSide = int(35)
	exteriorAngle = 360/numberOfSides
	for i in range(numberOfSides):
		q.forward(lengthOfSide)
		q.right(exteriorAngle)
	
def polygon_3() :
	q.penup()
	q.color("#a6a6a6")
	q.pendown()
	q.right(180)
	q.forward(87.5)
	q.right(180)
	q.color("#ff0000")
	#numberOfSides = int(input('Enter the number of sides of a polygon: '))
	#lengthOfSide = int(input('Enter the length of a side of a polygon: '))
	numberOfSides = int(7)
	lengthOfSide = int(35)
	exteriorAngle = 360/numberOfSides
	for i in range(numberOfSides):
		q.forward(lengthOfSide)
		q.right(exteriorAngle)
	
def polygon_4() :
	q.penup()
	q.color("#a6a6a6")
	q.pendown()
	q.penup()
	q.pendown()
	q.right(180)
	q.forward(71.5)
	q.right(180)
	q.color("#ff00ff")
	#numberOfSides = int(input('Enter the number of sides of a polygon: '))
	#lengthOfSide = int(input('Enter the length of a side of a polygon: '))
	numberOfSides = int(5)
	lengthOfSide = int(35)
	exteriorAngle = 360/numberOfSides
	for i in range(numberOfSides):
		q.forward(lengthOfSide)
		q.right(exteriorAngle)

def polygon_5() :
	q.penup()
	q.color("#a6a6a6")
	q.pendown()
	q.pendown()
	q.right(180)
	q.forward(40)
	q.right(190)
	q.color("#0000ff")
	#numberOfSides = int(input('Enter the number of sides of a polygon: '))
	#lengthOfSide = int(input('Enter the length of a side of a polygon: '))
	numberOfSides = int(3)
	lengthOfSide = int(35)
	exteriorAngle = 360/numberOfSides
	for i in range(numberOfSides):
		q.forward(lengthOfSide)
		q.right(exteriorAngle)
	q.color("#a6a6a6")
	q.right(190)
	q.forward(20)
	q.right(20)
	q.forward(20)
	q.right(20)
	q.forward(20)
	q.left(20)
	q.left(220)
	q.forward(400)
	q.right(90)
	q.forward(40)
	q.right(180)
	q.forward(40)
	q.right(90)
	q.forward(140)
	q.right(90)
	q.forward(47.5)
	q.left(90)
	
def circle_1() :
	q.penup()
	q.pendown()
	q.right(180)
	q.color("#00ffff")
	q.circle(65)
	q.color("#a6a6a6")
	q.left(90)
	q.forward(300)
	
def circle_2() :
	q.penup()
	q.pendown()
	q.color("#66ff33")
	q.circle(35)
	q.color("#a6a6a6")
	q.forward(200)
	q.right(90)
	q.color("#ff6666")
	q.circle(55)
	q.color("#a6a6a6")
	q.left(90)
	q.forward(200)
	q.color("#3399ff")
	q.circle(45)
	q.color("#a6a6a6")
	q.right(180)
	q.forward(748)
	q.left(90)
	q.forward(650)
	q.left(90)
	q.color("#ffff99")
	q.circle(65)
	q.color("#a6a6a6")
	q.forward(300)
	q.color("#9966ff")
	q.circle(35)
	q.color("#a6a6a6")
	q.forward(300)
	q.left(90)
	q.color("#3333cc")
	q.circle(55)
	q.color("#a6a6a6")
	q.right(90)
	q.forward(300)
	q.color("#00ffcc")
	q.circle(45)
	q.color("#a6a6a6")
	q.right(180)
	q.forward(400)
	q.right(90)
	q.penup()
	q.forward(325)
	q.right(180)
	
'''
	
def circle_3() :
	q.penup()
	
def circle_4() :
	q.penup()
	
def circle_5() :
	q.penup()
	
'''

def finisher_red() :
	q.pendown()
	q.color("#ff0000")
	q.penup()
	q.left(90)
	q.forward(24)
	q.right(90)
	q.forward(26)
	q.left(90)
	q.forward(200)
	q.left(115) #116 degrees/Higher number means lower ange
	global a
	a = 0
	a = a + 1
	while a < 100 :
		q.forward(a)
		a = a + 1
		q.pendown()
		for i in range(3): #The more number numbers the more wiggle/equal for is a straight line/ odd is a circle
			for i in range(5):
				q.forward(5)
				q.right(10)
				q.pendown()
				q.color("#ff0000")
			for i in range(5):
				q.forward(5)
				q.left(10)
				q.pendown()
				q.color("#ff0000")
			for i in range(5):
				q.forward(5)
				q.right(10)
				q.pendown()
				r.color("#ff0000")
	
#Main and execute--------
def main():
	try:
		#Old main
		turtle.TurtleScreen._RUNNING = True
		#get width and height globally
		turtle.screensize(canvwidth=width, canvheight=height, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		w = turtle.Screen()
		hello_world()
		border_line()
		border_line_2()
		border_line_3()
		border_line_4()
		border_line_5()
		border_line_6()
		#border_line_7()
		#border_line_8()
		polygon_1()
		polygon_2()
		polygon_3()
		polygon_4()
		polygon_5()
		circle_1()
		circle_2()
		#circle_3()
		#circle_4()
		#circle_5()
		finisher_red()
		w.exitonclick()
		#new main

	finally:		
			turtle.Terminator()
			
main()

'''
    five circles (done)
    five polygons (done)
    five line commands (done)
    two for loops (done)
    one global variable (done)
    one while loop (done)
    !!!change the code so that it does not look like Coleman's!!!S (done)
    
    for i in range(3): #The more number numbers the more wiggle
			for i in range(5):
				r.forward(5)
				r.right(10)
				r.pendown()
				r.color("#f86156")
			for i in range(5):
				r.forward(5)
				r.left(10)
				r.pendown()
				r.color("#f86156")
			for i in range(5):
				r.forward(5)
				r.left(10)
				r.pendown()
				r.color("#f86156")

'''
#End of code-----------
